import sys
from datetime import datetime
from typing import List
from scapy.all import srp, Ether, ARP, conf
from serial_mapper import get_mac_addr_from_num

# Last 3 bytes of the MAC address of each Tello.
# Identified by the SSID printed on the
# back of the head unit (RMTT-______)
# Separate every 2 characters with a colon.
test_macs = [
    7,
    8,
    9,
    10
]


def find_ips_by_mac(target_macs: List[str], mode=0) -> dict[str, str]:
    """
    Returns a map of MAC addresses to IPs.
    """
    found_clients = arp_scan(mode)
    ips = {}
    num = 0
    print(found_clients)
    for mac in target_macs:
        mac = mac.lower()
        if found_clients.get(mac) is None:
            num += 1
            print(f"Drone not found: {mac}")
        else:
            ips[mac] = found_clients[mac]
    print(f"{num} drones not found")
    return ips


def find_ips_by_number(test_numbers: List[int], mode=0) -> dict[str, str]:
    """
    Returns a map of MAC addresses to IPs.
    """
    found_clients = arp_scan(mode)
    ips = {}
    num = 0
    print(found_clients)
    print('test_numbers', test_numbers)
    for number, mac in zip(test_numbers, get_mac_addr_from_num(test_numbers)):
        mac = mac.lower()
        if found_clients.get(mac) is None:
            num += 1
            print(f"Drone not found: {number}")
        else:
            ips[mac] = found_clients[mac]
    print(f"{num} drones not found")
    return ips


def all_drones_ready(test_numbers: List[int], mode=0) -> bool:
    found_clients = arp_scan(mode)
    ips = {}
    num = 0
    print(found_clients)
    print('test_numbers', test_numbers)
    for number, mac in zip(test_numbers, get_mac_addr_from_num(test_numbers)):
        mac = mac.lower()
        if found_clients.get(mac) is None:
            num += 1
            print(f"Drone not found: {number}")
        else:
            ips[mac] = found_clients[mac]
    return num == 0


def arp_scan(mode=0):
    if mode == 0:
        target_ip = "192.168.50.1/24"
    elif mode == 1:
        target_ip = "192.168.0.1/24"
    elif mode == 2:
        target_ip = "192.168.69.1/24"
    target_ip = "192.168.50.1/24"
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3)[0]

    clients = {}

    for sent, received in result:
        clients[received.hwsrc[-8:].lower()] = received.psrc
    return clients


if __name__ == "__main__":
    ips = find_ips_by_number(test_macs)
    print(ips)
