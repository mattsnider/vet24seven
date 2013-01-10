from __future__ import with_statement
import os
from fabric.api import local, cd, run as remote_run, env, get, abort


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
PYTHON = os.path.join(ROOT_DIR, '..', 'bin', 'python')
IS_DEV = not ('/ubuntu/' in ROOT_DIR) # are we running these fab commands on a dev box? TODO: Not a great/tight check.


def prod():
    env.user = 'ubuntu'

def bounce_webserver(memcached=1):
    """
    Bounces the webserver and memcached (by default).
    """
    bounce_gunicorn()

def bounce_gunicorn():
    """
    Stops and restarts green unicorn webserver.
    """
    local('sudo stop vet24seven')
    local('sudo start vet24seven')

def purge_pyc():
    """
    Removes all *.pyc files from the current directory and descendants.
    """
    with cd(ROOT_DIR):
        if IS_DEV:
            local('find . -name "*.pyc" | xargs rm')
        else:
            local('sudo find . -name "*.pyc" | xargs sudo rm')
    
def git_rebase():
    """
    Rebases the code.
    """
    with cd(ROOT_DIR):
        local('git fetch origin', False)
        local('git rebase origin/master', False)

def git_push():
    """
    Pushes the code.
    """
    git_rebase()
    with cd(ROOT_DIR):
        local('git push origin master', False)

def upload_static():
    STATIC_DIRS = ('css', 'files', 'img', 'js', 'scss',)
    with cd(ROOT_DIR):
        for static_dir in STATIC_DIRS:
            local('mkdir -p %s/static/%s' % (ROOT_DIR, static_dir))
        local('./manage.py collectstatic --noinput -l', False)
        local('./manage.py combinestatic', False)
        local('./manage.py upload_to_s3', False)

def deploy(memcached=1):
    """
    Redeploys the web app.
    """
    with cd(ROOT_DIR):
        local('pip install -r requirements.pip')
    upload_static()
    local('sudo stop vet24seven')
    with cd(ROOT_DIR):
        local('./manage.py migrate')
    local('sudo start vet24seven')