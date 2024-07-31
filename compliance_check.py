import re
from github import Github
import os

# GitHub token and repo info
GITHUB_TOKEN = os.getenv('')
REPO_NAME = ''




import re
from github import Github
import os
from datetime import datetime

# GitHub token and repo info
GITHUB_TOKEN = os.getenv('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')
REPO_NAME = 'mntlst934/ansible-playbook'
JIRA_PROJECT_KEY = 'SPOCKT'  # Replace with your JIRA project key

# Define the JIRA ticket pattern (example: PROJECT-123)
jira_ticket_pattern = re.compile(rf'\b{JIRA_PROJECT_KEY}-\d+\b')

# Initialize GitHub client
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# Fetch recent commits (adjust `per_page` for more commits if needed)
commits = repo.get_commits(per_page=100)

# Evaluate commit messages and generate the report
report = []
for commit in commits:
    message = commit.commit.message.split('\n')[0]
    author = commit.commit.author.name
    date = commit.commit.author.date
    date_str = date.strftime("%Y-%m-%d %H:%M:%S")
    match = jira_ticket_pattern.search(message)
    
    if match:
        jira_ticket_id = match.group(0)
        compliance_status = "Compliant"
    else:
        jira_ticket_id = "N/A"
        compliance_status = "Non-Compliant"
    
    report.append({
        "author": author,
        "date": date_str,
        "jira_ticket_id": jira_ticket_id,
        "message": message,
        "status": compliance_status
    })

# Output the report
for entry in report:
    print(f"{entry['author']} | {entry['jira_ticket_id']} | {entry['date']} | {entry['status']}")

# Optionally, save the report to a file
with open("commit_compliance_report.txt", "w") as f:
    for entry in report:
        f.write(f"{entry['author']} | {entry['jira_ticket_id']} | {entry['date']} | {entry['status']}\n")

