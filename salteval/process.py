# -*- coding: utf-8 -*-
'''
Library for verifying processes
'''

import psutil
import re


def is_running(name):
    '''
    Filter process names
    '''
    process_regex = re.compile(name)

    process = [
        i for i in psutil.process_iter() if process_regex.match(i.name())
    ]

    if process:
        return True

    return False
