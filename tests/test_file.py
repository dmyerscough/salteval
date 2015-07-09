#!/usr/bin/env python

import salteval
import unittest
import mock


class TestFileFunctions(unittest.TestCase):
    '''
    Testing the functionality of the Salteval file module
    '''

    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.lstat')
    def test_is_file(self, mock_stat, mock_path):
        '''
        Test the is_file
        '''
        mock_stat.return_value.st_mode = 33188
        self.assertTrue(
            salteval.file.is_file('/etc/resolv.conf')
        )

        mock_stat.return_value.st_mode = 123
        self.assertFalse(
            salteval.file.is_file('/etc/resolv.conf')
        )

    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.lstat')
    def test_is_dir(self, mock_stat, mock_path):
        '''
        Test the is_dir
        '''
        mock_stat.return_value.st_mode = 16877
        self.assertTrue(
            salteval.file.is_dir('/etc')
        )

        mock_stat.return_value.st_mode = 123
        self.assertFalse(
            salteval.file.is_dir('/etc/resolv.conf')
        )

    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.lstat')
    def test_is_socket(self, mock_stat, mock_path):
        '''
        Test the is_socket
        '''
        mock_stat.return_value.st_mode = 49590
        self.assertTrue(
            salteval.file.is_socket('/etc/mysocket')
        )

        mock_stat.return_value.st_mode = 123
        self.assertFalse(
            salteval.file.is_socket('/etc/resolv.conf')
        )

    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.lstat')
    def test_is_block(self, mock_stat, mock_path):
        '''
        Test the is_block
        '''
        mock_stat.return_value.st_mode = 25008
        self.assertTrue(
            salteval.file.is_block('/etc/myblock')
        )

        mock_stat.return_value.st_mode = 123
        self.assertFalse(
            salteval.file.is_block('/etc/resolv.conf')
        )

    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.lstat')
    def test_is_symlink(self, mock_stat, mock_path):
        '''
        Test the is_symlink
        '''
        mock_stat.return_value.st_mode = 41471
        self.assertTrue(
            salteval.file.is_symlink('/etc/symlink')
        )

        mock_stat.return_value.st_mode = 123
        self.assertFalse(
            salteval.file.is_symlink('/etc/symlink')
        )

    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.lstat')
    def test_is_fifo(self, mock_stat, mock_path):
        '''
        Test the is_fifo
        '''
        mock_stat.return_value.st_mode = 4480
        self.assertTrue(
            salteval.file.is_fifo('/etc/fifo')
        )

        mock_stat.return_value.st_mode = 123
        self.assertFalse(
            salteval.file.is_symlink('/etc/fifo')
        )

    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.lstat')
    def test_is_perms(self, mock_stat, mock_path):
        '''
        Test is_perms
        '''
        mock_stat.return_value.st_mode = 33188
        self.assertTrue(
            salteval.file.is_perms('/etc/passwd', '644')
        )

        mock_stat.return_value.st_uid = 32768
        self.assertFalse(
            salteval.file.is_perms('/etc/passwd', '755')
        )

    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.lstat')
    def test_is_owner(self, mock_stat, mock_path):
        '''
        Test is_owner
        '''
        mock_stat.return_value.st_uid = 0
        self.assertTrue(
            salteval.file.is_owner('/etc/passwd', 0)
        )

        mock_stat.return_value.st_uid = 1
        self.assertFalse(
            salteval.file.is_owner('/etc/passwd', 0)
        )

    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.lstat')
    def test_is_group(self, mock_stat, mock_path):
        '''
        Test is_group
        '''
        mock_stat.return_value.st_gid = 0
        self.assertTrue(
            salteval.file.is_group('/etc/passwd', 0)
        )

        mock_stat.return_value.st_gid = 1
        self.assertFalse(
            salteval.file.is_group('/etc/passwd', 0)
        )
