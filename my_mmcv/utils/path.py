# -*-coding:utf-8-*-
import os
import os.path as osp
from pathlib import Path

from .misc import is_str


def check_file_exist(filename, msg_tmpl='file "{}" does not exist'):
    if not osp.isfile(filename):
        raise FileNotFoundError(msg_tmpl.format(filename))