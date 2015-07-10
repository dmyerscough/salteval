# -*- coding: utf-8 -*-
'''
Library verifying network changes
'''

import socket
import struct
import psutil

from socket import AF_INET, AF_INET6, SOCK_STREAM, SOCK_DGRAM


def convert(val):
    '''
    Convert little indian
    '''
    return socket.inet_ntoa(struct.pack("<L", int(val, 16)))


def is_listening(expect_port, protocol='tcp'):
    '''
    Check a port is listening on a specific interface
    '''
    PROTOCOL = {
        (AF_INET, SOCK_STREAM): 'tcp',
        (AF_INET, SOCK_DGRAM): 'udp',
        (AF_INET6, SOCK_STREAM): 'tcp6',
        (AF_INET6, SOCK_DGRAM): 'udp6'
    }

    ports = [i for i in psutil.net_connections() if i.status == 'LISTEN']

    for port in ports:
        (interface, listening_port) = port.laddr

        if PROTOCOL[(port.family, port.type)] == protocol and expect_port == listening_port:
            return True

    return False


def iface_present(nic, ip_addr, netmask, broadcast):
    '''
    Check the network interface is correctly configured
    '''
    interfaces = psutil.net_if_addrs()

    for iface in interfaces.get(nic, []):
        if iface.address == ip_addr and iface.netmask == netmask and iface.broadcast == broadcast:
            return True

    return False


def route_present(destination, gateway, interface):
    '''
    Check a specific route is present
    '''
    with open('/proc/net/route', 'r') as route_table:
        for i in route_table:
            if i.startswith('Iface'):
                continue

            (iface, dest, gway, _) = i.split('\t', 3)

            if interface == iface and destination == convert(dest) and gateway == convert(gway):
                return True

    return False
