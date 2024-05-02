from datetime import datetime
from bs4 import BeautifulSoup
from requests import get
from McQueen.error_handler import handle
from McQueen.validations import validate_domain
from McQueen.colors import R, G, BOLD, RESET

def run(hostname = None):
    if hostname is None:
        hostname = input(f'{R}[{G}+{R}]{RESET} Enter Domain: ')

    # While loop to validate input
    while True:
        if not validate_domain(hostname):
            print(f'{R}[Invalid Domain]{RESET} Given Domain Is Invalid')
            print()
            hostname = input(f'{R}[{G}+{R}]{RESET} Enter Domain (e.g: example.com): ')
        else:
            break

    whois_link = "https://who.is/whois/"

    print('Checking domain age...')

    res = get(f"{whois_link}{hostname}").text
    doc = BeautifulSoup(res, "html.parser")

    registered_on_key = doc.find('div', text='Registered On')

    registered_on_value = registered_on_key.find_next_sibling('div', class_='queryResponseBodyValue').text.strip()

    if registered_on_value:
        given_date = datetime.strptime(registered_on_value, "%Y-%m-%d")

        # Current date
        current_date = datetime.now()

        # Calculate the difference
        difference = current_date - given_date

        years = difference.days // 365
        months = difference.days % 365 // 30
        days = difference.days % 365 % 30

        print()
        print(f"{R}[{G}+{R}]{RESET} {BOLD}Registered On:{RESET}", given_date.strftime("%d/%m/%Y"))
        print(f"{R}[{G}+{R}]{RESET} {BOLD}Domain age:{RESET} {years} years, {months} months and {days} days")
    else:
        handle(label="No Data Found")