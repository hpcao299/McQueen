import socket
from requests import get
from urllib.parse import urlparse
import dns.resolver
from McQueen.error_handler import handle
from McQueen.validations import validate_url
from McQueen.colors import R, G, BOLD, RESET

def get_ip_details(ip):
    response = get(f'https://ipinfo.io/{ip}/json')
    ip_details = response.json()
    
    return ip_details

def run(url: str = None):
    try:
        resolver = dns.resolver.Resolver()

        if url is None:
            url = input(f'{R}[{G}+{R}]{RESET} Enter Website: ')

        # While loop to validate input
        while True:
            if not validate_url(url):
                print(f'{R}[Invalid URL]{RESET} Given Url Is Invalid')
                print()
                url = input(f'{R}[{G}+{R}]{RESET} Enter Website (e.g: https://example.com): ')
            else:
                break

        parsed_url = urlparse(url)
        hostname = parsed_url.netloc

        addresses = socket.getaddrinfo(hostname, None)
        ip_addresses = list(set([addr[4][0] for addr in addresses]))
        ipv4_addresses = [addr for addr in ip_addresses if ":" not in addr]
        ipv6_addresses = [addr for addr in ip_addresses if ":" in addr]

        ip = socket.gethostbyname(hostname)

        nameservers = resolver.resolve(hostname, 'NS')

        print()
        if ip != '127.0.0.1': 
            if len(ipv4_addresses) > 0:
                print(f'{R}[{G}+{R}]{RESET} {BOLD}IPv4 Address:{RESET}')
                for ip in ipv4_addresses:
                    print(f"   - {ip}")    

            if len(ipv6_addresses) > 0:
                print(f'{R}[{G}+{R}]{RESET} {BOLD}IPv6 Address:{RESET}')
                for ip in ipv6_addresses:
                    print(f"   - {ip}")
            
            if len(nameservers) > 0:
                print(f'{R}[{G}+{R}]{RESET} {BOLD}Nameservers:{RESET}')
                for nameserver in nameservers:
                    print(f"   - {nameserver}")

            ip_details = get_ip_details(ip)

            print(f"{R}[{G}+{R}]{RESET} {BOLD}Country:{RESET} {ip_details['country']}")
            print(f"{R}[{G}+{R}]{RESET} {BOLD}Region:{RESET} {ip_details['region']}")
            print(f"{R}[{G}+{R}]{RESET} {BOLD}City:{RESET} {ip_details['city']}")
            print(f"{R}[{G}+{R}]{RESET} {BOLD}Latitude / Longitude:{RESET} {ip_details['loc']}")
            print(f"{R}[{G}+{R}]{RESET} {BOLD}Timezone:{RESET} {ip_details['timezone']}")
            print(f"{R}[{G}+{R}]{RESET} {BOLD}Origin:{RESET} {ip_details['org']}")
            print(f"{R}[{G}+{R}]{RESET} {BOLD}Postal:{RESET} {ip_details['postal']}")
        else:
            handle(label = "No Data Found")
    except dns.resolver.NoAnswer as e:
        handle(label = "No Answers From DNS Resolver", error = e)
