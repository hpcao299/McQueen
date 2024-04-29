from urllib.parse import urlparse
from requests import get
import re
import os

# Pattern to get 
pattern = r"<loc>(.*?)</loc>"

def run():
    try:
        # url = input('Enter website url (https://example.com): ')
        url = "https://fullstack.edu.vn/sitemap.xml/abc/abc/acb"

        parsed_uri = urlparse(url)
        sitemap_url = '{uri.scheme}://{uri.netloc}/sitemap.xml'.format(uri=parsed_uri)

        res = get(sitemap_url)
        xml_data = res.text

        # Handle users' choices when primary sitemap.xml file is the collection of other .xml files
        if xml_data.find('<sitemapindex') != -1 and xml_data.find('<urlset') == -1:
            sitemap_urls = re.findall(pattern, xml_data)

            print(f"Found {len(sitemap_urls)} .xml files:")
            print("   " + '\n   '.join(sitemap_urls))
            print()

            command = input('Do you want to crawl all these files (press "01" to agree): ')

            if command == '01':
                # Create folder to store crawled files
                folder_name = parsed_uri.netloc
                os.makedirs(folder_name, exist_ok=True)
                os.chdir(folder_name)


                for url in sitemap_urls:
                    print()
                    print(f'Start crawling {url}')

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

                    print(f'{len(found_urls)} crawled pages is written in: {file_name}.txt')
                    
            else:
                print('Exited!')

        # Collect URLs when the primary sitemap.xml file is the collection of URLs
        elif xml_data.find('<sitemapindex') == -1 and xml_data.find('<urlset') != -1:
            urls = re.findall(pattern, xml_data)

            try:
                f = open(f"{parsed_uri.netloc}.txt", "x")
                f.write('\n'.join(urls))
                f.close()

                print(f'{len(urls)} crawled pages is written in: {parsed_uri.netloc}.txt')
            except Exception as e:
                print(e)
                if str(e).find('File exists') != -1:
                    command = input(f'File "{parsed_uri.netloc}.txt" has been exists. Press "01" to override existed file: ')
                    if command == '01':
                        f = open(f"{parsed_uri.netloc}.txt", "w")
                        f.write('\n'.join(urls))
                        f.close()

                        print(f'{len(urls)} crawled pages is written in: {parsed_uri.netloc}.txt')
                    else:
                        print('Exited!')
        else:
            print('No valid sitemap or URLs found.')
    except Exception as e:
        print(e)
        print('\nExited!')

run()

