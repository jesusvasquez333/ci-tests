#!/usr/bin/env python3

import os
import git
from github import Github

repo_slug=os.environ.get('TRAVIS_REPO_SLUG')
pr_number=os.environ.get('TRAVIS_PULL_REQUEST')

ghRepo=f"https://github.com/{repo_slug}"
print(f"repository: {ghRepo}")

gh = Github()
remRepo = gh.get_repo(ghRepo)

print(f"PR#{pr_number}")
req = remRepo.get_pull(pr_number)
labels = req.get_labels()

print(labels)