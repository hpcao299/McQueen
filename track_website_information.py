import socket
from requests import get
from urllib.parse import urlparse
import dns.resolver
from error_handler import handle

def get_ip_details(ip):
    response = get(f'https://ipinfo.io/{ip}/json')
    ip_details = response.json()
    
    return ip_details

def run(url = None):
    try:
        resolver = dns.resolver.Resolver()

        if url is None:
            url = input('Enter Website: ')

        parsed_url = urlparse(url)
        hostname = parsed_url.netloc

        addresses = socket.getaddrinfo(hostname, None)
        ip_addresses = list(set([addr[4][0] for addr in addresses]))
        ipv4_addresses = [addr for addr in ip_addresses if ":" not in addr]
        ipv6_addresses = [addr for addr in ip_addresses if ":" in addr]

        ip = socket.gethostbyname(hostname)

        nameservers = resolver.resolve(hostname, 'NS')

        if ip != '127.0.0.1': 
            print('IPv4 Address:')
            for ip in ipv4_addresses:
                print(f"   - {ip}")
            print('IPv6 Address:')
            for ip in ipv6_addresses:
                print(f"   - {ip}")
            print('Nameservers:')
            for nameserver in nameservers:
                print(f"   - {nameserver}")


            ip_details = get_ip_details(ip)

            print(f"Country: {ip_details['country']}")
            print(f"Region: {ip_details['region']}")
            print(f"City: {ip_details['city']}")
            print(f"Latitude / Longitude: {ip_details['loc']}")
            print(f"Timezone: {ip_details['timezone']}")
            print(f"Origin: {ip_details['org']}")
            print(f"Postal: {ip_details['postal']}")
        else:
            handle(label = "No Data Found")
    except dns.resolver.NoAnswer as e:
        handle(label = "No Answers From DNS Resolver", error = e)
