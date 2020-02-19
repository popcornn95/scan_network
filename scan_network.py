# FInding mac address usinf Address resolution protocol (ARP)
#!usr/bin/nav/env python
import scapy.all as scapy


def scan(ipadress):
    # instance of an ARP - creating a packet

    # below code prints the variable names inside the class of arp_request
    # scapy.ls(scapy.ARP())

    arp_request = scapy.ARP()
    # creating a packet with the ipaddress
    arp_request.pdst = ipadress
    # print(arp_request.summary())

    #create a ether object and pass the mac address of broadcast
    # scapy.ls(scapy.Ether())
    broadcast = scapy.Ether()
    broadcast.dst = "ff:ff:ff:ff:Ff:ff"
    # print(broadcast.summary())

    # combining both arp_request and broadcast
    arp_request_broadcast = broadcast/arp_request
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show  ()

    # sending the packet , verbose is to remover the header from the result(formatting)
    answered_list = scapy.srp(arp_request_broadcast, timeout =1, verbose = False)[0]
    # answered_list  for ips that are in the network
    # print(answered_list.summary())

    client_list =[]
    for element in answered_list:
          client_dict = {"ip":element[1].psrc ,"mac":element[1].hwsrc}
          client_list.append(client_dict)
        # print (element[1].show())
        # printing source ip and mac
        # print (element[1].psrc + "\t\t"+element[1].hwsrc)
    return client_list


def print_result(resultlist):
    print("IP\t\t\t\tMAC Address\n.................................")
    for client in resultlist:
        print(client["ip"] + "\t\t"+client["mac"])


scan_result= scan("10.0.2.1/24")
print_result(scan_result)