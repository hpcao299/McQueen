from McQueen import check_domain_age
from McQueen import check_domain_registrant
from McQueen import crawl_website_pages
from McQueen import detect_firewall
from McQueen import scan_subdomain
from McQueen import track_ip_location
from McQueen import track_website_information
from McQueen.colors import R, G, Y, RESET, BOLD
from McQueen.error_handler import handle
from McQueen.validations import validate_url, validate_domain, validate_ip_address

import requests
import argparse
import os

# Custom type for URL validation
def validate_url_type(url):
    if not validate_url(url):
        raise argparse.ArgumentTypeError(f"'{url}' is not a valid URL (e.g: https://example.com)")
    return url

# Custom type for domain validation
def validate_domain_type(domain):
    if not validate_domain(domain):
        raise argparse.ArgumentTypeError(f"'{domain}' is not a valid domain (e.g: example.com)")
    return domain

def validate_ip_type(ip):
    if not validate_ip_address(ip):
        raise argparse.ArgumentTypeError(f"'{ip}' is not a valid IP address (e.g: 8.8.8.8)")
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

def clear_terminal():
    """Clears the terminal screen."""
    
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    while True:
        banner()

        print(f'{R}[{G}01{R}]{RESET} Track Website Information{RESET}')
        print(f'{R}[{G}02{R}]{RESET} Trace IP Address Location{RESET}')
        print(f'{R}[{G}03{R}]{RESET} Check Domain Age{RESET}')
        print(f'{R}[{G}04{R}]{RESET} Find Domain Owner{RESET}')
        print(f'{R}[{G}05{R}]{RESET} Scan Subdomains{RESET}')
        print(f'{R}[{G}06{R}]{RESET} Crawl Pages{RESET}')
        print(f'{R}[{G}07{R}]{RESET} Detect Website Firewall{RESET}')
        command = input(f'\n{R}[{G}+{R}]{RESET} Choose: ')

        clear_terminal()
        banner()

        try:
            if command == '01':
                track_website_information()
            elif command == '02':
                track_ip_location()
            elif command == '03':
                check_domain_age()
            elif command == '04':
                check_domain_registrant()
            elif command == '05':
                scan_subdomain()
            elif command == '06':
                crawl_website_pages()
            elif command == '07':
                detect_firewall()
            else:
                print(f'{R}{BOLD}[error]{RESET} Wrong Command{RESET}')
        except requests.exceptions.ConnectionError as e:
            handle(label = "Connection Error", error = e)
            break
        except requests.exceptions.Timeout as e:
            handle(label = "Timeout", error = e)
            break
        except Exception as e:
            handle(error = e)
            break

        input(f'\n{R}[{G}+{R}]{RESET} Press "ENTER" To Continue: ')
        clear_terminal()

def parse_args():
    parser = argparse.ArgumentParser(description='Command line interface for information-gathering tools')

    # Add arguments
    parser.add_argument('-i', '--info', help="Track website information", metavar="URL", type=validate_url_type)
    parser.add_argument('-p', '--page', help="Crawl website pages", metavar="URL", type=validate_url_type)
    parser.add_argument('-f', '--firewall', help="Detect website firewall", metavar="URL", type=validate_url_type)
    parser.add_argument('-a', '--age', help="Check domain age", metavar="DOMAIN", type=validate_domain_type)
    parser.add_argument('-s', '--subdomain', help="Scan subdomains", metavar="DOMAIN", type=validate_domain_type)
    parser.add_argument('-o', '--owner', help="Find domain owner", metavar="DOMAIN", type=validate_domain_type)
    parser.add_argument('-l', '--location', help="Trace IP address location", metavar="IP", type=validate_ip_type)

    return parser.parse_args()

def main(args = None):
    try:
        if args.info:
            banner()
            track_website_information(args.info)
        elif args.page:
            banner()
            crawl_website_pages(args.page)
        elif args.firewall:
            banner()
            detect_firewall(args.firewall)
        elif args.age:
            banner()
            check_domain_age(args.age)
        elif args.subdomain:
            banner()
            scan_subdomain(args.subdomain)
        elif args.owner:
            banner()
            check_domain_registrant(args.owner)
        elif args.location:
            banner()
            track_ip_location(args.location)
        else:
            display_menu()
    except requests.exceptions.ConnectionError as e:
        handle(label = "Connection Error", error = e)
    except requests.exceptions.Timeout as e:
        handle(label = "Timeout", error = e)
    except Exception as e:
        print(e)

def interactive():
    args = parse_args()
    main(args)

if __name__ == "__main__":
    interactive()