#import re
#from github import Github
#import os
#import csv
#from datetime import datetime, timedelta

# GitHub token and repo info
GITHUB_TOKEN = os.getenv('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')
REPO_NAME = 'mntlst934/ansible-playbook'

# Define the JIRA ticket pattern (example: PROJECT-123)
jira_ticket_pattern = re.compile(r'\bPROJECT-\d+\b')

# Initialize GitHub client
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# Get current time and time 24 hours ago
now = datetime.utcnow()
yesterday = now - timedelta(days=1)

# Fetch commits from the last 24 hours
commits = repo.get_commits(since=yesterday)

# Prepare CSV file
report_filename = 'commit_compliance_report.csv'
with open(report_filename, mode='w', newline='', encoding='utf-8') as report_file:
    csv_writer = csv.writer(report_file)
    csv_writer.writerow(['Username', 'JIRA Ticket ID', 'Date'])

    # Evaluate commit messages
    for commit in commits:
        message = commit.commit.message.split('\n')[0]
        author = commit.commit.author.name
        date = commit.commit.author.date.strftime('%Y-%m-%d')

        # Find JIRA ticket ID
        match = jira_ticket_pattern.search(message)
        jira_ticket_id = match.group(0) if match else 'Non-Compliant'

        # Write to CSV
        csv_writer.writerow([author, jira_ticket_id, date])

print(f"Report generated: {report_filename}")


