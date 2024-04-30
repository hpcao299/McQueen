import check_domain_age
import check_domain_registrant
import crawl_website_pages
import detect_firewall
import scan_subdomain
import track_ip_location
import track_website_information
from colors import R, G, RESET


def banner():
    print(f"""{R}
            ______  ___     _______                         
            ___   |/  /_______  __ \___  __________________ 
            __  /|_/ /_  ___/  / / /  / / /  _ \  _ \_  __ ╲
            _  /  / / / /__ / /_/ // /_/ //  __/  __/  / / /
            /_/  /_/  \___/ \___\_\\__,_/ \___/\___//_/ /_/ 
          
            # A collection of information-gathering tools
    {RESET}""")

def display_menu():
    print(f'[{R}01{RESET}] {G}Track Website Information{RESET}')
    print(f'[{R}02{RESET}] {G}Trace IP Address Location{RESET}')
    print(f'[{R}03{RESET}] {G}Domain Age Checker{RESET}')
    print(f'[{R}04{RESET}] {G}Find Domain Owner{RESET}')
    print(f'[{R}05{RESET}] {G}Scan Subdomains{RESET}')
    print(f'[{R}06{RESET}] {G}Crawl Pages{RESET}')
    print(f'[{R}07{RESET}] {G}Detect Website Firewall{RESET}')
    command = input(f'\n[{R}-{RESET}] Choose: ')

banner()
display_menu()