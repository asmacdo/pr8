from github import Github
import flake8.main
import requests

g = Github()
repo = g.get_repo('pulp/pulp')


pr = repo.get_pull(1355)
for fp in pr.get_files():
    resp = requests.get(fp.raw_url)
    flake8.main.check_code(resp.content)

# Next filter out all lines that are not "additions"
