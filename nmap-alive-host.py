#!/usr/bin/env python

import nmap

#Scan hosts net and arg
nm = nmap.PortScanner()
nm.scan(hosts='172.16.0.0/24', arguments='-n -sP -PE -PA21,23,80,3389')

#All host
hosts_list = [(x,nm[x]['status']['state']) for x in nm.all_hosts()]

#Filter alive host
for host,status in hosts_list:
    print host + ': ' + status
