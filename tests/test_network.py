#!/usr/bin/env python


import mock
import unittest
import salteval


class TestNetwork(unittest.TestCase):

    @mock.patch('psutil.net_if_addrs')
    def test_interface_present(self, mock_network):
        '''
        Test network interface is present
        '''
        snic = mock.MagicMock(
            family=2,
            address='192.168.0.1',
            netmask='255.255.255.0',
            broadcast='192.168.0.255'
        )

        mock_network.return_value = {'eth0': [snic]}

        self.assertTrue(
            salteval.network.iface_present(
                'eth0', '192.168.0.1', '255.255.255.0', '192.168.0.255'
            )
        )
        self.assertFalse(
            salteval.network.iface_present(
                'eth1', '192.168.0.1', '255.255.255.0', '192.168.0.255'
            )
        )

    @mock.patch('psutil.net_connections')
    def test_listening(self, mock_connections):
        '''
        Test network service is listening on a port
        '''
        sconn = mock.MagicMock(
            fd=11,
            family=2,
            type=1,
            laddr=('0.0.0.0', 22),
            raddr=(),
            status='LISTEN',
            pid=1987
        )

        mock_connections.return_value = [sconn]

        self.assertTrue(
            salteval.network.is_listening(22, 'tcp')
        )
        self.assertFalse(
            salteval.network.is_listening(23, 'udp')
        )

    def test_route_present(self):
        '''
        Test a route present
        '''
        route_table = [
            'Iface\tDestination\tGateway\tFlags\tRefCnt\tUse\tMetric\tMask\tMTU\tWindow\tIRTT',
            'eth1\t00000000\t0101000A\t0003\t0\t0\t0\t00000000\t0\t0\t0'
        ]

        route_table = '\n'.join(route_table)

        with mock.patch('salteval.network.open', mock.mock_open(read_data=route_table), create=True) as mock_open:
            mock_open.return_value.__iter__.return_value = route_table.splitlines()

            self.assertTrue(
                salteval.network.route_present('0.0.0.0', '10.0.1.1', 'eth1')
            )
            self.assertFalse(
                salteval.network.route_present('0.0.0.0', '10.0.1.2', 'eth0')
            )

    def test_convert(self):
        '''
        Test convert big indian
        '''
        
        self.assertEqual(
            salteval.network.convert('0101000A'), '10.0.1.1'
        )
        self.assertEqual(
            salteval.network.convert('0101000B'), '11.0.1.1'
        )
        self.assertEqual(
            salteval.network.convert('0101000C'), '12.0.1.1'
        )
