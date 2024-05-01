from datetime import datetime
from bs4 import BeautifulSoup
from requests import get
from error_handler import handle
from validations import validate_domain
from colors import R, RESET

def run(hostname = None):
    if hostname is None:
        hostname = input('Enter Domain: ')

    if not validate_domain(hostname):
        return print(f'{R}[Invalid Domain]{RESET} Given Domain Is Invalid')

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

        print("Registered On:", given_date.strftime("%d/%m/%Y"))
        print("Domain age:", years, "years,", months, "months and", days, "days")
    else:
        handle(label="No Data Found")