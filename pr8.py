#!/usr/bin/env python

from github import Github
import flake8.main
import requests
import sys

try:
    repo_name = sys.argv[1]
    pull_number = int(sys.argv[2])
except IndexError:
    print("<user/repo>, <pr number (int)>")

g = Github()
repo = g.get_repo(repo_name)
print "Got repo"

pr = repo.get_pull(pull_number)
print "got pr"
for fp in pr.get_files():
    print "\n\n\nworking with file{a}".format(a=fp.filename)
    resp = requests.get(fp.raw_url)
    flake8.main.check_code(resp.content)

sys.exit(1)
# Next filter out all lines that are not "additions"
