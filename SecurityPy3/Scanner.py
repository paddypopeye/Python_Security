#!/usr/bin/python3
import nmap
nm = nmap.PortScanner()
nm.scan('192.168.1.0/24', '1-1024', '-v')
print(nm.scaninfo())
print(nm.csv())
