from github import Github
import flake8.main
import sys
from contextlib import contextmanager
import requests

g = Github('username', 'password')
repo = g.get_repo('pulp/pulp')


@contextmanager
def redirected(stdout):
    saved_stdout = sys.stdout
    sys.stdout = open("tmp/err_" + stdout, 'w')
    yield
    sys.stdout = saved_stdout

for pr in repo.get_pulls():
    for fp in pr.get_files():
        resp = requests.get(fp.raw_url)
        with redirected(fp.filename.replace('/', '__')):
            print fp.filename
            test = flake8.main.check_code(resp.content)
