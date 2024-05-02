## About McQueen

McQueen is an advanced command-line interface (CLI) toolkit crafted in Python, designed to empower users with information-gathering capabilities. It serves as a solution for investigating variety of Internet informations including website, IP address, email address or phone number.

## Installation

Get Python downloaded on computer: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Latest release on GitHub

```
git clone https://github.com/hpcao299/McQueen.git
cd McQueen
pip3 install -r requirements.txt
python3 McQueen/main.py
```

### Lastest release on PyPI

```
pip3 install McQueen
```

## Usage

| Short Form | Long Form   | Description                    |
| ---------- | ----------- | ------------------------------ |
| -h         | --help      | Show the help message and exit |
| -i         | --info      | Track website information      |
| -p         | --page      | Crawl website pages            |
| -f         | --firewall  | Detect website firewall        |
| -a         | --age       | Check domain age               |
| -s         | --subdomain | Scan subdomains                |
| -o         | --owner     | Find domain owner              |
| -l         | --location  | Trace IP address location      |

### Examples

-   To list all the basic options and switches use -h switch:

`mcqueen -h`

-   To track website information (IP, ports, nameservers,...):

`mcqueen -i https://example.com`

-   To crawl all available pages of a website:

`mcqueen -p https://example.com`

-   To detect a website's firewall:

`mcqueen -f https://example.com`

-   To check domain age and registered date:

`mcqueen -a example.com`

-   To enumerate subdomains of a domain:

`mcqueen -s example.com`

-   To find domain's registrant contact information:

`mcqueen -o example.com`

-   To trace IP address location:

`mcqueen -l 8.8.8.8`

### Using McQueen as a module in your python scripts

#### Example

```
from McQueen import track_website_information

details = track_website_information('https://example.com')
```

#### Functions

-   **track_website_information**: Get website information (IP, ports, nameservers,...).
-   **crawl_website_pages**: Crawl all available pages of a website through its sitemaps.
-   **detect_firewall**: Detect firewall usage of website.
-   **check_domain_age**: Investigate registered date and age of a domain.
-   **scan_subdomain**: Enumerate subdomains of a domain.
-   **check_domain_registrant**: Search domain's registrant / administrative contact information.
-   **track_ip_location**: Trace IP address details and location.

## Resources

McQueen uses variety of available and legal resources on the Internet. Taking a look at these tools and resources in order for more advanced and technical purposes.

-   WhoIs ([https://who.is](https://who.is))
-   IPinfo ([https://ipinfo.io](https://ipinfo.io))
-   DNSDumpster ([https://dnsdumpster.com](https://dnsdumpster.com))
-   ip-api ([https://ip-api.com](https://ip-api.com))

## License

McQueen is licensed under the MIT license. Take a look at the [LICENSE](https://github.com/hpcao299/McQueen/blob/main-python/LICENSE) for more information.

## Contributions

This tool is open for everyone and feel free to contribute if you have any development ideas.
