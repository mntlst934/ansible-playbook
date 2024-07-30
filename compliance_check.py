import re
from github import Github
import os

# GitHub token and repo info
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = 'your_username/your_repo'

# Define the JIRA ticket pattern (example: PROJECT-123)
jira_ticket_pattern = re.compile(r'\bPROJECT-\d+\b')

# Initialize GitHub client
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# Fetch recent commits (adjust `per_page` and `since` for desired range)
commits = repo.get_commits(per_page=100)

# Evaluate commit messages
report = []
for commit in commits:
    message = commit.commit.message.split('\n')[0]
    if jira_ticket_pattern.search(message):
        report.append(f"Compliant: {message}")
    else:
        report.append(f"Non-Compliant: {message}")

# Output the report (for now, we'll print it; you can change this to save to a file or database)
for entry in report:
    print(entry)
