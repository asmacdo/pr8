from github import Github
import flake8.main
import sys
from contextlib import contextmanager
import requests

# Login to gi
g = Github()
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
            config = "flake8.cfg"
            flake8_style = flake8.engine.get_style_guide(
                config_file=config,
                ignore=['.tox', '.docs/*']
            )
            flake8_style.input_file(None, lines=resp.content.splitlines(True))

    # Next filter out all lines that are not "additions"
