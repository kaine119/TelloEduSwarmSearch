import sys
from datetime import datetime
from typing import List
from scapy.all import srp, Ether, ARP, conf

# Last 3 bytes of the MAC address of each Tello.
# Identified by the SSID printed on the
# back of the head unit (RMTT-______)
# Separate every 2 characters with a colon.
test_macs = [
    # "10:9b:b4",
    # "f2:48:dc",
    # "d3:91:ca",
    # "9a:ec:c6",
    # "33:14:9c",
    # "d2:71:04",
    # "9b:6f:6c",
    # "9a:ec:dc",
    # "10:b1:7c",
    # "10:ac:0a",
    # "33:21:26",
    # "33:14:9a",
    # "f2:3b:1a",
    # "33:09:aa",
    # "10:a9:9c",
    "33:21:26",
    "9b:6f:6c",
    "33:14:9c",
    "10:9b:b4",
    "d3:91:ca",
    "d2:71:04",
    "10:b1:7c",
    "33:14:9a",
    "f2:43:0e",
]


def find_ips_by_mac(test_numbers: List[int]) -> dict[str, str]:
    """
    Returns a map of MAC addresses to IPs.
    """
    found_clients = arp_scan()
    ips = {}
    num = 0
    print(found_clients)
    for number, mac in zip(test_numbers, get_mac_addr_from_num(test_numbers)):
        mac = mac.lower()
        if found_clients.get(mac) is None:
            num += 1
            print(f"Drone not found: {number}")
        else:
            ips[mac] = found_clients[mac]
    print(f"{num} drones not found")
    return ips


def arp_scan():
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
    ips = find_ips_by_mac(test_macs)
    print(ips)
