import check_domain_age
import check_domain_registrant
import crawl_website_pages
import detect_firewall
import scan_subdomain
import track_ip_location
import track_website_information
from colors import R, G, Y, RESET, BOLD
from error_handler import handle

import requests
import argparse
import ipaddress
import re

# Function to validate URL format
def validate_url(url):
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(url_pattern, url)

# Custom type for URL validation
def validate_url_type(url):
    if not validate_url(url):
        raise argparse.ArgumentTypeError(f"'{url}' is not a valid URL (e.g: https://example.com)")
    return url

# Function to validate domain format
def validate_domain(domain):
    domain_pattern = re.compile(
        r'^([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$')
    return re.match(domain_pattern, domain)

# Custom type for domain validation
def validate_domain_type(domain):
    if not validate_domain(domain):
        raise argparse.ArgumentTypeError(f"'{domain}' is not a valid domain (e.g: example.com)")
    return domain

def validate_ip_type(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{ip}' is not a valid IP address")
    return ip

parser = argparse.ArgumentParser(description='Command line interface for website analysis')

def banner():
    print(f"""{R}
            ______  ___     _______                         
            ___   |/  /_______  __ \___  __________________ 
            __  /|_/ /_  ___/  / / /  / / /  _ \  _ \_  __ ╲
            _  /  / / / /__ / /_/ // /_/ //  __/  __/  / / /
            /_/  /_/  \___/ \___\_\\__,_/ \___/\___//_/ /_/ 
          
            {Y}{BOLD}# A collection of information-gathering tools
    {RESET}""")

def display_menu():
    print(f'{R}[{G}01{R}]{RESET} Track Website Information{RESET}')
    print(f'{R}[{G}02{R}]{RESET} Trace IP Address Location{RESET}')
    print(f'{R}[{G}03{R}]{RESET} Check Domain Age{RESET}')
    print(f'{R}[{G}04{R}]{RESET} Find Domain Owner{RESET}')
    print(f'{R}[{G}05{R}]{RESET} Scan Subdomains{RESET}')
    print(f'{R}[{G}06{R}]{RESET} Crawl Pages{RESET}')
    print(f'{R}[{G}07{R}]{RESET} Detect Website Firewall{RESET}')
    command = input(f'\n{R}[{G}-{R}]{RESET} Choose: ')

parser = argparse.ArgumentParser(description='Command line interface for information-gathering tools')

# Add arguments
parser.add_argument('-i', '--info', help="Track website information", metavar="URL", type=validate_url_type)
parser.add_argument('-p', '--page', help="Crawl website pages", metavar="URL", type=validate_url_type)
parser.add_argument('-f', '--firewall', help="Detect website firewall", metavar="URL", type=validate_url_type)
parser.add_argument('-a', '--age', help="Check domain age", metavar="DOMAIN", type=validate_domain_type)
parser.add_argument('-s', '--subdomain', help="Scan subdomains", metavar="DOMAIN", type=validate_domain_type)
parser.add_argument('-o', '--owner', help="Find domain owner", metavar="DOMAIN", type=validate_domain_type)
parser.add_argument('-l', '--location', help="Trace IP address location", metavar="IP", type=validate_ip_type)

args = parser.parse_args()

banner()
try:
    if args.info:
        track_website_information.run(args.info)
    elif args.page:
        crawl_website_pages.run(args.page)
    elif args.firewall:
        detect_firewall.run(args.firewall)
    elif args.age:
        check_domain_age.run(args.age)
    elif args.subdomain:
        scan_subdomain.run(args.subdomain)
    elif args.owner:
        check_domain_registrant.run(args.owner)
    elif args.location:
        track_ip_location.run(args.location)
    else:
        display_menu()
except requests.exceptions.ConnectionError as e:
    handle(label = "Connection Error", error = e)
except requests.exceptions.Timeout as e:
    handle(label = "Timeout", error = e)
except Exception as e:
    handle(error = e)