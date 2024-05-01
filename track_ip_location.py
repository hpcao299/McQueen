from requests import get

def run(ip_address = None):
    if ip_address is None:
        ip_address = input('Enter IP address: ')

    response = get(f"http://ip-api.com/json/{ip_address}")
    details = response.json()

    print(f"IP Address: {ip_address}")
    print(f"Country: {details['country']}")
    print(f"Region: {details['regionName']}")
    print(f"City: {details['city']}")
    print(f"ZIP Code: {details['zip']}")
    print(f"Latitude: {details['lat']}")
    print(f"Longitude: {details['lon']}")
    print(f"Timezone: {details['timezone']}")
    print(f"Organization: {details['org']}")
    print(f"ASN: {details['as']}")
        