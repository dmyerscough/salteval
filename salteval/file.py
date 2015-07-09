# -*- coding: utf-8 -*-
'''
Library for testing file attributes
'''

import stat
import pwd
import grp
import os


def __is_type(name, _type='FILE'):
    '''
    Check the file type on `name`
    '''
    FILE_TYPES = {
        'FILE': 'S_ISREG',
        'DIRECTORY': 'S_ISDIR',
        'BLOCK': 'S_ISBLK',
        'FIFO': 'S_ISFIFO',
        'SYMLINK': 'S_ISLNK',
        'SOCKET': 'S_ISSOCK'
    }
    if os.path.exists(name):
        mode = os.lstat(name)

        return getattr(stat, FILE_TYPES[_type])(mode.st_mode)

    return False


def is_file(name):
    '''
    Check `name` is a file
    '''
    return __is_type(name, 'FILE')


def is_dir(name):
    '''
    Check `name` is a directory
    '''
    return __is_type(name, 'DIRECTORY')


def is_socket(name):
    '''
    Check `name` is a socket
    '''
    return __is_type(name, 'SOCKET')


def is_block(name):
    '''
    Check `name` is a block device
    '''
    return __is_type(name, 'BLOCK')


def is_symlink(name):
    '''
    Check `name` is a symlink
    '''
    return __is_type(name, 'SYMLINK')


def is_fifo(name):
    '''
    Check `name` is a FIFO
    '''
    return __is_type(name, 'FIFO')


def is_perms(name, mode):
    '''
    Check the permissions of `name`
    '''
    if os.path.exists(name):
        perms = oct(stat.S_IMODE(os.stat(name).st_mode))

        if perms.endswith(mode):
            return True
        else:
            return False

    return False


def is_owner(name, owner):
    '''
    Check the owner of `name`
    '''
    if os.path.exists(name):
        uid = os.lstat(name).st_uid

        if isinstance(owner, int):
            return owner == uid
        else:
            return owner == pwd.getpwuid(uid).pw_name

    return False


def is_group(name, group):
    '''
    Check the group of `name`
    '''
    if os.path.exists(name):
        gid = os.lstat(name).st_gid

        if isinstance(group, int):
            return group == gid
        else:
            return group == grp.getgrgid(gid).gr_name

    return False
