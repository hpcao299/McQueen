from error_handler import handle
from urllib.parse import urlparse
from requests import get
import re
import os
from validations import validate_url
from colors import R, G, BOLD, RESET

# Pattern to get 
pattern = r"<loc>(.*?)</loc>"

def run(url = None):    
    if url is None:
        url = input(f'{R}[{G}+{R}]{RESET} Enter Website: ')

    # While loop to validate input
    while True:
        if not validate_url(url):
            print(f'{R}[Invalid URL]{RESET} Given Url Is Invalid')
            print()
            url = input(f'{R}[{G}+{R}]{RESET} Enter Website (e.g: https://example.com): ')
        else:
            break

    parsed_uri = urlparse(url)
    sitemap_url = '{uri.scheme}://{uri.netloc}/sitemap.xml'.format(uri=parsed_uri)

    print('Searching pages...')

    res = get(sitemap_url)
    xml_data = res.text

    # Handle users' choices when primary sitemap.xml file is the collection of other .xml files
    if xml_data.find('<sitemapindex') != -1 and xml_data.find('<urlset') == -1:
        sitemap_urls = re.findall(pattern, xml_data)

        print(f"\n{R}[{G}+{R}]{RESET} {BOLD}Found {len(sitemap_urls)} .xml files:{RESET}")
        print("   - " + '\n   - '.join(sitemap_urls))
        print()

        input(f'{R}[{G}+{R}]{RESET} Do you want to crawl all these files (press "ENTER" to continue): ')

        # Create folder to store crawled files
        folder_name = parsed_uri.netloc
        os.makedirs(folder_name, exist_ok=True)
        os.chdir(folder_name)


        for url in sitemap_urls:
            print()
            print(f'{R}[{G}+{R}]{RESET} Start crawling {BOLD}{url}{RESET}')

            res = get(url)
            found_urls = re.findall(pattern, res.text)

            # Split the URL by "/"
            parts = url.split("/")
            # Get the last part of the URL
            last_part = parts[-1]
            # Remove the file extension
            file_name = last_part.split(".")[0]


            f = open(f"{file_name}.txt", "w")
            f.write('\n'.join(found_urls))
            f.close()

            print(f'{R}[{G}+{R}]{RESET} {len(found_urls)} crawled pages is written in: {BOLD}{file_name}.txt{RESET}')

    # Collect URLs when the primary sitemap.xml file is the collection of URLs
    elif xml_data.find('<sitemapindex') == -1 and xml_data.find('<urlset') != -1:
        urls = re.findall(pattern, xml_data)

        try:
            f = open(f"{parsed_uri.netloc}.txt", "x")
            f.write('\n'.join(urls))
            f.close()

            print(f'\n{R}[{G}+{R}]{RESET} {len(urls)} crawled pages is written in: {BOLD}{parsed_uri.netloc}.txt{RESET}')
        except FileExistsError:
            input(f'\n{R}[{G}+{R}]{RESET} File {BOLD}"{parsed_uri.netloc}.txt"{RESET} has been exists. Press "ENTER" to override existed file: ')

            f = open(f"{parsed_uri.netloc}.txt", "w")
            f.write('\n'.join(urls))
            f.close()

            print(f'\n{R}[{G}+{R}]{RESET} {len(urls)} crawled pages is written in: {BOLD}{parsed_uri.netloc}.txt{RESET}')
    else:
        handle(label = "No Valid Sitemap Or URLs Found")