# -*- coding: utf-8 -*-
'''
Library verifying network changes
'''

import socket
import struct
import psutil

from socket import AF_INET, AF_INET6, SOCK_STREAM, SOCK_DGRAM


def __convert(val):
    '''
    Convert little indian
    '''
    return socket.inet_ntoa(struct.pack("<L", int(val, 16)))


def is_listening(expect_port, protocol='tcp'):
    '''
    Check a port is listening on a specific interface
    '''
    __PROTOCOL_MAP = {
        (AF_INET, SOCK_STREAM): 'tcp',
        (AF_INET, SOCK_DGRAM): 'udp',
        (AF_INET6, SOCK_STREAM): 'tcp6',
        (AF_INET6, SOCK_DGRAM): 'udp6'
    }

    ports = [i for i in psutil.net_connections() if i.status == 'LISTEN']

    for port in ports:
        (interface, listening_port) = port.laddr

        if (__PROTOCOL_MAP[(port.family, port.type)] == protocol and
           expect_port == listening_port):
            return True

    return False


def iface_present(nic, ip, netmask, broadcast):
    '''
    Check the network interface is correctly configured
    '''
    interfaces = psutil.net_if_addrs()

    if interfaces.get(nic, None):
        for iface in interfaces:
            if (iface.address == ip and iface.netmask == netmask and
               iface.broadcast == broadcast):
                return True

    return False


def route_present(destination, gateway, interface):
    '''
    Check a specific route is present
    '''
    with open('/proc/net/route', 'r') as fh:
        for i in fh.readlines()[1:]:
            (iface, dest, gw, misc) = i.split('\t', 3)

            if (interface == iface and destination == __convert(dest) and
               gateway == __convert(gw)):
                return True

    return False
