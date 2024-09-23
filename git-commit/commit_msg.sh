#!/bin/sh
# This hook will make sure that the commit message contains a JIRA issue.
#
# To enable this hook, rename this file to ".git/hooks/commit-msg".
# Make sure to add execution permissions to the file.

export MESSAGE=$(<$1)
export JIRA_ISSUE_TAG='SPOCKT-([0-9]*)'

if [[ $MESSAGE =~ $JIRA_ISSUE_TAG ]]; then
  echo -e "\e[32mGreat, your commit message contains a JIRA issue!\e[0m"
  exit 0;
fi

echo -e "\e[31mOh hamburgers ... You forgot to add a JIRA issue number!\e[0m";
