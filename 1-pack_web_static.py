#!/usr/bin/python3
"""do_pack module
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder
    of AirBnB Clone v2.
    """
    # Create versions folder (if not exits)-> -p
    local("mkdir -p versions")
    # Create web_static file with date and extension .tgz
    now = datetime.now()
    name = "versions/web_static_{}".format(now.strftime("%Y%m%d%H%M%S"))
    name += ".tgz"
    # Create tgz
    compressCommand = "tar -cvzf {} web_static".format(name)
    # Return de path if the file was created
    if local(compressCommand) == 1:
        return None
    return name
