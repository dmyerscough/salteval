# -*- coding: utf-8 -*-
'''
Unit tests for process module
'''

import mock
import unittest
import salteval


class TestProcess(unittest.TestCase):
    '''
    Test functionality of process module
    '''

    @mock.patch('psutil.process_iter')
    def test_is_running(self, mock_process):
        '''
        Test processes are running
        '''
        mock_process.name.return_value = 'sshd'
        mock_process.return_value = [mock_process]

        self.assertTrue(
            salteval.process.is_running('sshd')
        )
        self.assertFalse(
            salteval.process.is_running('nginx')
        )
