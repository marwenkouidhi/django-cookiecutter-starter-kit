"""
NOTE:
    the below code is to be maintained Python 2.x-compatible
    as the whole Cookiecutter Django project initialization
    can potentially be run in Python 2.x environment
    (at least so we presume in `pre_gen_project.py`).

TODO: restrict Cookiecutter Django project initialization to
      Python 3.x environments only
"""

from __future__ import print_function

import os
import random
import shutil

try:
    # Inspired by
    # https://github.com/django/django/blob/master/django/utils/crypto.py
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

DEBUG_VALUE = "debug"


def remove_heroku_files():
    file_names = ["Procfile", "runtime.txt", "requirements.txt"]
    for file_name in file_names:
        os.remove(file_name)


def remove_docker_files():
    os.remove("docker-compose.yml")
    shutil.rmtree("docker")


def main():
    if "{{ cookiecutter.use_heroku }}".lower() == "n":
        remove_heroku_files()

    if "{{ cookiecutter.use_docker }}".lower() == "n":
        remove_docker_files()


if __name__ == "__main__":
    main()
