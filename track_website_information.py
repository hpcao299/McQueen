import socket
from requests import get
from urllib.parse import urlparse

def run():
    try:
        # url = input('Enter website url (https://example.com): ')
        # parsed_url = urlparse(url)
        # hostname = parsed_url.netloc
        hostname = "fullstack.edu.vn"

        addresses = socket.getaddrinfo(hostname, None)
        ip_addresses = list(set([addr[4][0] for addr in addresses]))
        ipv4_addresses = [addr for addr in ip_addresses if ":" not in addr]
        ipv6_addresses = [addr for addr in ip_addresses if ":" in addr]

        def get_ip_details(hostname):
            ip = socket.gethostbyname(hostname)
            response = get(f'https://ipinfo.io/{ip}/json')
            ip_details = response.json()
            
            return ip_details
            
        
        print('IPv4 Address:')
        for ip in ipv4_addresses:
            print(f"   - {ip}")
        print('IPv6 Address:')
        for ip in ipv6_addresses:
            print(f"   - {ip}")

        ip_details = get_ip_details(hostname)

        print(f"Country: {ip_details['country']}")
        print(f"Region: {ip_details['region']}")
        print(f"City: {ip_details['city']}")
        print(f"Latitude / Longitude: {ip_details['loc']}")
        print(f"Timezone: {ip_details['timezone']}")
        print(f"Origin: {ip_details['org']}")
        print(f"Postal: {ip_details['postal']}")
    except Exception as e:
        print(e)
        print('\nExited!')