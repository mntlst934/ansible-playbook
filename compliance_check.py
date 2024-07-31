import re
import os
from datetime import datetime, timedelta
from github import Github

# GitHub token and repo info
GITHUB_TOKEN = os.getenv('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')
REPO_NAME = 'mntlst934/ansible-playbook'
JIRA_PROJECT_KEY = 'SPOCKT'  # Replace with your JIRA project key

# Define the JIRA ticket pattern (example: PROJECT-123)
jira_ticket_pattern = re.compile(r'\bPROJECT-\d+\b')

# Initialize GitHub client
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# Calculate the time 24 hours ago from now
since_time = datetime.utcnow() - timedelta(days=1)

# Fetch commits from the last 24 hours
commits = repo.get_commits(since=since_time.isoformat())

# List to hold the report entries
report_entries = []

# Evaluate commit messages
for commit in commits:
    message = commit.commit.message.split('\n')[0]
    author = commit.commit.author.name
    date = commit.commit.author.date.isoformat()
    match = jira_ticket_pattern.search(message)
    jira_ticket = match.group(0) if match else "No JIRA Ticket"

    # Add to report entries
    report_entries.append(f"{author},{jira_ticket},{date},{message}")

# Generate the report file
report_filename = f"commit_report_{datetime.utcnow().strftime('%Y%m%d%H%M')}.csv"
with open(report_filename, 'w') as report_file:
    report_file.write("Username,JIRA Ticket ID,Date,Message\n")
    for entry in report_entries:
        report_file.write(entry + "\n")

print(f"Report generated: {report_filename}")

