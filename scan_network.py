# FInding mac address usinf Address resolution protocol (ARP)
#!usr/bin/nav/env python
import scapy.all as scapy


def scan(ipadress):
    scapy.arping(ipadress)


scan("10.0.2.1/24")