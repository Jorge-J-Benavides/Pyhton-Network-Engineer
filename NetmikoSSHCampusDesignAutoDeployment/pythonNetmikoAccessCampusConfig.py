#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_SW1 = {
        'device_type':'cisco_ios',
        'ip':'192.168.122.71',
        'username':'jorge',
        'password':'cisco',
}

iosv_l2_SW2 = {
        'device_type':'cisco_ios',
        'ip':'192.168.122.72',
        'username':'jorge',
        'password':'cisco',
}

iosv_l2_SW3 = {
        'device_type':'cisco_ios',
        'ip':'192.168.122.73',
        'username':'jorge',
        'password':'cisco',
}

iosv_l2_SW4 = {
        'device_type':'cisco_ios',
        'ip':'192.168.122.74',
        'username':'jorge',
        'password':'cisco',
}

iosv_l2_SW5 = {
        'device_type':'cisco_ios',
        'ip':'192.168.122.75',
        'username':'jorge',
        'password':'cisco',
}

with open('iosv_12_core') as f:
        lines = f.read().splitlines()
print lines

access_devices = [iosv_l2_SW2, iosv_l2_SW1]

for device in access_devices:
        net_connect = ConnectHandler(**device)
        output = net_connect.send_config_set(lines)
        print output

with open('iosv_12_access_campus_config') as f:
        lines = f.read().splitlines()
print lines

core_devices = [iosv_l2_SW5, iosv_l2_SW4, iosv_l2_SW3, ]

for device in core_devices:
        net_connect = ConnectHandler(**device)
        output = net_connect.send_config_set(lines)
        print output

