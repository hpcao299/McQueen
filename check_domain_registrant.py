from bs4 import BeautifulSoup
from requests import get
from validations import validate_domain
from colors import R, RESET

def run(hostname = None):
    if hostname is None:
        hostname = input('Enter Domain: ')

    if not validate_domain(hostname):
        return print(f'{R}[Invalid Domain]{RESET} Given Domain Is Invalid')

    whois_link = "https://who.is/whois/"

    print('Searching domain registrant...')
    
    res = get(f"{whois_link}{hostname}").text
    doc = BeautifulSoup(res, "html.parser")

    registrant_strong = doc.find('strong', text='Registrant Contact Information:')
    info_wrapper = registrant_strong.parent.find_next_sibling('div')

    updated_divs = doc.select(selector='div:-soup-contains("Information Updated:")')
    updated_info = updated_divs[len(updated_divs) - 1]

    info_rows = info_wrapper.find_all('div', class_ = "row")

    print(f'\n{hostname} registrant info:')
    for row in info_rows:
        key_element = row.find('strong')
        value_element = key_element.parent.find_next_sibling('div')
        print(f'- {key_element.text}: {value_element.text}') if bool(value_element.text) else print(f'- {key_element.text}: None')

    info = updated_info.text.split(': ')
    print('\nInformation updated: {date_updated}'.format(date_updated=info[1]))
