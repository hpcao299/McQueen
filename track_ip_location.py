from requests import get
import ipaddress
from colors import R, G, BOLD, RESET

def run(ip_address = None):
    if ip_address is None:
        ip_address = input(f'{R}[{G}+{R}]{RESET} Enter IP address: ')

    # While loop to validate input
    while True:
        try:
            ipaddress.ip_address(ip_address)

            break
        except ValueError:
            print(f'{R}[Invalid IP]{RESET} Given IP Address Is Invalid')
            print()
            ip_address = input(f'{R}[{G}+{R}]{RESET} Enter IP address (e.g: 8.8.8.8): ')

    response = get(f"http://ip-api.com/json/{ip_address}")
    details = response.json()

    print(f"{R}[{G}+{R}]{RESET} {BOLD}IP Address:{RESET} {ip_address}")
    print(f"{R}[{G}+{R}]{RESET} {BOLD}Country:{RESET} {details['country']}")
    print(f"{R}[{G}+{R}]{RESET} {BOLD}Region:{RESET} {details['regionName']}")
    print(f"{R}[{G}+{R}]{RESET} {BOLD}City:{RESET} {details['city']}")
    print(f"{R}[{G}+{R}]{RESET} {BOLD}ZIP Code:{RESET} {details['zip']}")
    print(f"{R}[{G}+{R}]{RESET} {BOLD}Latitude:{RESET} {details['lat']}")
    print(f"{R}[{G}+{R}]{RESET} {BOLD}Longitude:{RESET} {details['lon']}")
    print(f"{R}[{G}+{R}]{RESET} {BOLD}Timezone:{RESET} {details['timezone']}")
    print(f"{R}[{G}+{R}]{RESET} {BOLD}Organization:{RESET} {details['org']}")
    print(f"{R}[{G}+{R}]{RESET} {BOLD}ASN:{RESET} {details['as']}")
        