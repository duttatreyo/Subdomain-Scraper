import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

# Extended list of subdomains to check
subdomains_list = [
    'www', 'mail', 'ftp', 'webmail', 'admin', 'blog', 'dev', 'wiki', 
    'api', 'ns1', 'ns2', 'smtp', 'pop', 'imap', 'forum', 'support', 
    'shop', 'store', 'blogs', 'm', 'mobile', 'beta', 'kb', 'knowledgebase'
]

# User-Agent string to use in requests
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

def find_subdomains(domain):
    found_subdomains = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_subdomain, domain, subdomain) for subdomain in subdomains_list]
        for future in futures:
            result = future.result()
            if result:
                found_subdomains.append(result)
    return found_subdomains

def check_subdomain(domain, subdomain):
    for protocol in ['http://', 'https://']:
        url = f'{protocol}{subdomain}.{domain}'
        try:
            # Respect robots.txt and don't scrape disallowed pages
            robots_url = f'{protocol}{subdomain}.{domain}/robots.txt'
            robots_response = requests.get(robots_url, headers={"User-Agent": user_agent}, timeout=5)
            if 'Disallow: /' in robots_response.text:
                # Quietly skip due to robots.txt restrictions
                continue

            response = requests.get(url, headers={"User-Agent": user_agent}, timeout=5)
            if response.ok:
                soup = BeautifulSoup(response.content, 'html.parser')
                title = soup.find('title')
                title = title.get_text(strip=True) if title else "No Title Found"
                return {'url': url, 'title': title}
        except requests.RequestException:
            # Silent failure, do not print any error messages to the console
            continue
    return None

if __name__ == "__main__":
    domain = input("Enter the domain: ")
    
    # Validate input
    parsed = urlparse(f'http://{domain}')  # add scheme to properly parse the domain
    if not parsed.netloc:
        print("Invalid domain format")
        exit(1)

    domain = parsed.netloc  # use parsed netloc as the domain

    print(f"Searching for subdomains of {domain} and scraping public data...")
    subdomains = find_subdomains(domain)
    if subdomains:
        print("Found subdomains:")
        for subdomain in subdomains:
            print(f"URL: {subdomain['url']} - Title: {subdomain['title']}")
    else:
        print("No subdomains found.")
