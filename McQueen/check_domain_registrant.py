from bs4 import BeautifulSoup
from requests import get
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

    print('Searching domain registrant...')
    
    res = get(f"{whois_link}{hostname}").text
    doc = BeautifulSoup(res, "html.parser")

    registrant_strong = doc.find('strong', text='Registrant Contact Information:')
    info_wrapper = registrant_strong.parent.find_next_sibling('div')

    updated_divs = doc.select(selector='div:-soup-contains("Information Updated:")')
    updated_info = updated_divs[len(updated_divs) - 1]

    info_rows = info_wrapper.find_all('div', class_ = "row")

    print(f'\n{R}[{G}+{R}]{RESET} {BOLD}{hostname} registrant info:{RESET}')
    for row in info_rows:
        key_element = row.find('strong')
        value_element = key_element.parent.find_next_sibling('div')
        print(f'{R}[{G}+{R}]{RESET} {BOLD}{key_element.text}{RESET}: {value_element.text}') if bool(value_element.text) else print(f'{R}[{G}+{R}]{RESET} {BOLD}{key_element.text}{RESET}: None')

    info = updated_info.text.split(': ')
    print('\nInformation updated: {date_updated}'.format(date_updated=info[1]))
