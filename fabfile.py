#
# general setting
#
USER_NAME =         'coldsheep'
CONTAINER_BASE =    'news_backend'
CONTAINER_NAME =    'news-backend'

#
#
#
from os.path import dirname, join
from fabric.api import lcd, run, task, env, local, settings
from fabric.colors import green, magenta, red, yellow
from fabric.context_managers import shell_env

IMAGE_BASE =        '%s/%s' % (USER_NAME, CONTAINER_BASE)

@task
def build_no_cache():
    local('docker build --no-cache -t %s .' % (IMAGE_BASE))

@task
def build():
    local('docker build -t %s .' % (IMAGE_BASE))

@task
def up(mode='-t'):
    down()
    local('docker run %s --name %s ' % (mode, CONTAINER_BASE) +
          ' -v news_data:/root/data -v news_test:/root/_posts ' +
          IMAGE_BASE)

@task
def down():
    with settings(warn_only=True):
        local('docker kill %s' % CONTAINER_BASE)
        local('docker rm %s' % CONTAINER_BASE)
