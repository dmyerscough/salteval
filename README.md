
=========
salteval
=========

[![build status](https://magnum.travis-ci.com/dmyerscough/salteval.svg?token=dJXbRwpjXC8gnoYqRo5q&branch=master)](https://magnum.travis-ci.com/dmyerscough/salteval)

Perform functional testing after your configuration management system has run.



File
====

Check to see if an object is a file

```yaml
checking_file:
  file.is_file:
    - name: /etc/passwd
```

Check to see if an object is a directory

```yaml
testing_directory:
  file.is_dir:
    - name: /etc
```

Check to see if an object is a socket

```yaml
testing_socket:
  file.is_socket:
    - name: /var/run/mysql.sock
```

Check to see if an object is a block device

```yaml
testing_block_device:
  file.is_block:
    - name: /dev/sda1
```

Check to see if an object is a symlink

```yaml
testing_symlink:
  file.is_symlink:
    - name: /etc/named.conf
```

Checking to see if an object is a FIFO pipe

```yaml
testing_fifo:
  file.is_fifo:
    - name: /var/run/myfifo
```

Check the permissions of a file

```yaml
testing_file_perms:
  file.is_perms:
    - name: /etc/passwd
    - mode: 644
```

Check the owner of a file

```yaml
testing_file_owership:
  file.is_owner:
    - name: /etc/passwd
    - owner: root
```

Check the group ownership of the file

```yaml
testing_file_group:
  file.is_group:
    - name: /etc/passwd
    - group: root
```


Network
=======

Check a port is open

``` yaml
check_sshd_running:
  network.is_listening:
    - port: 22
    - protocol: tcp
```

Check an interface is present

``` yaml
testing_eth0:
  network.iface_present:
    - nic: eth0
    - ip: 192.168.0.1
    - netmask: 255.255.255.0
    - broadcast: 192.168.0.255
```

Check a route is present

``` yaml
testing_route:
  network.route_present:
    - destination: 192.168.0.0
    - gateway: 192.168.0.1
    - interfae: eth0
```

Process
=======

Check a process is running

``` yaml
testing_sshd_running:
  process.is_running:
    - name: '^sshd$'
```
