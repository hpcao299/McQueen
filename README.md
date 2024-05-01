## About McQueen

McQueen is an advanced command-line interface (CLI) toolkit crafted in Python, designed to empower users with information-gathering capabilities. It serves as a solution for investigating variety of Internet informations including website, IP address, email address or phone number.

## Installation

Get Python downloaded on computer: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Latest release on GitHub

```
git clone https://github.com/hpcao299/McQueen.git
cd McQueen
pip3 install -r requirements.txt
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

`python3 mcqueen.py -h`

-   To track website information (IP, ports, nameservers,...):

`python3 mcqueen.py -i https://example.com`

-   To crawl all available pages of a website:

`python3 mcqueen.py -p https://example.com`

-   To detect a website's firewall:

`python3 mcqueen.py -f https://example.com`

-   To check domain age and registered date:

`python3 mcqueen.py -a example.com`

-   To enumerate subdomains of a domain:

`python3 mcqueen.py -s example.com`

-   To find domain's registrant contact information:

`python3 mcqueen.py -o example.com`

-   To trace IP address location:

`python3 mcqueen.py -l 8.8.8.8`

## Resources

McQueen uses variety of available and legal resources on the Internet. Taking a look at these tools and resources in order for more advanced and technical purposes.

-   WhoIs ([https://who.is](https://who.is))
-   IPinfo ([https://ipinfo.io](https://ipinfo.io))
-   DNSDumpster ([https://dnsdumpster.com](https://dnsdumpster.com))
-   ip-api ([https://ip-api.com](https://ip-api.com))

## Contributions

This tool is open for everyone and feel free to contribute if you have any development ideas.
