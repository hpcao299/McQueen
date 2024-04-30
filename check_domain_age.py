from datetime import datetime
from bs4 import BeautifulSoup
from requests import get

# hostname = input('Enter a domain (e.g: example.com): ')
hostname = 'saigonnguyen.online'

whois_link = "https://who.is/whois/"

result = get(f"{whois_link}{hostname}").text
doc = BeautifulSoup(result, "html.parser")

registered_on_key = doc.find('div', text='Registered On')


print(result)

if registered_on_key:
    registered_on_value = registered_on_key.find_next_sibling('div', class_='queryResponseBodyValue').text.strip()

    given_date = datetime.strptime(registered_on_value, "%Y-%m-%d")

    # Current date
    current_date = datetime.now()

    # Calculate the difference
    difference = current_date - given_date

    # Extract the number of days from the difference
    days_difference = difference.days

    years = difference.days // 365
    months = difference.days % 365 // 30
    days = difference.days % 365 % 30

    print("Registered On:", given_date.strftime("%d/%m/%Y"))
    print("Domain age:", years, "years,", months, "months and", days, "days")
else:
    print("Data not found.")