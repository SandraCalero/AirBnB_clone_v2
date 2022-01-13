#!/usr/bin/python3
"""Fabric script that creates and distributes an archive
to your web servers, using the function deploy
"""
from os.path import exists
from fabric.api import put, run, env
do_pack = __import__('1-pack_web_static.py').do_pack
do_deploy = __import__('2-do_deploy_web_static.py').do_deploy
env.hosts = ['35.196.20.175', '52.23.183.91']
env.user = 'ubuntu'


def deploy():
    """Fabric script that creates and distributes an archive
    to your web servers, using the function deploy
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
