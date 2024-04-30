from requests import get


def run():
    def has_waf(waf: str):
        print('\nFirewall: ✅')
        print(f'Found WAF: {waf}')
    
    # url = input('Enter a website url: ')
    url = 'https://substack.com'
    
    print('Detecting firewall...')

    res = get(url)
    
    if 'Server' in res.headers and 'cloudflare' in res.headers['Server']:
        return has_waf('Cloudflare')

    if 'X-Powered-By' in res.headers and 'AWS Lambda' in res.headers['X-Powered-By']:
        return has_waf('AWS WAF')

    if 'Server' in res.headers and 'AkamaiGHost' in res.headers['Server']:
        return has_waf('Akamai')

    if 'Server' in res.headers and 'Sucuri' in res.headers['Server']:
        return has_waf('Sucuri')

    if 'Server' in res.headers and 'BarracudaWAF' in res.headers['Server']:
        return has_waf('Barracuda WAF')

    if 'Server' in res.headers and ('F5 BIG-IP' in res.headers['Server'] or 'BIG-IP' in res.headers['Server']):
        return has_waf('F5 BIG-IP')

    if 'X-Sucuri-ID' in res.headers and 'x-sucuri-cache' in res.headers['X-Sucuri-ID']:
        return has_waf('Sucuri CloudProxy WAF')

    if 'Server' in res.headers and 'FortiWeb' in res.headers['Server']:
        return has_waf('Fortinet FortiWeb WAF')

    if 'Server' in res.headers and 'Imperva' in res.headers['Server']:
        return has_waf('Imperva SecureSphere WAF')

    if 'x-protected-by' in res.headers and 'Sqreen' in res.headers['x-protected-by']:
        return has_waf('Sqreen')

    if 'x-waf-event-info' in res.headers:
        return has_waf('Reblaze WAF')

    if 'set-cookie' in res.headers and '_citrix_ns_id' in res.headers['set-cookie']:
        return has_waf('Citrix NetScaler')

    if 'x-denied-reason' in res.headers or 'x-wzws-requested-method' in res.headers:
        return has_waf('WangZhanBao WAF')

    if 'x-webcoment' in res.headers:
        return has_waf('Webcoment Firewall')

    if 'Server' in res.headers and 'Yundun' in res.headers['Server']:
        return has_waf('Yundun WAF')

    if 'x-yd-waf-info' in res.headers or 'x-yd-info' in res.headers:
        return has_waf('Yundun WAF')

    if 'Server' in res.headers and 'Safe3WAF' in res.headers['Server']:
        return has_waf('Safe3 Web Application Firewall')

    if 'Server' in res.headers and 'NAXSI' in res.headers['Server']:
        return has_waf('NAXSI WAF')

    if 'x-datapower-transactionid' in res.headers:
        return has_waf('IBM WebSphere DataPower')

    print('\nFirewall: ❌')
    print('No firewall found.')
