# Subdomain-Scraper

This project is a Python script designed to find subdomains for a given domain and to scrape public, non-personal data from them. It responsibly checks each subdomain’s `robots.txt` file and skips those that disallow scraping, ensuring it abides by the website’s scraping policy. 

## Features
- Finds potential subdomains for a given domain.
- Checks `robots.txt` to respect scraping restrictions set by the website owner.
- Scrapes title from allowed web pages.
- Multi-threaded for improved performance.
- Validates user input for correct domain format.
- Handles network errors gracefully without printing them to the console.
- 5 seconds timeout for each request.

## Prerequisites
- Python 3.x
- BeautifulSoup
- requests

  
## Disclaimer
> Use this script responsibly and ethically. Make sure to comply with legal constraints and the terms of service of the websites you are interacting with. Unauthorized or aggressive scanning can lead to IP bans or legal actions.

## Setup
1. Clone this repository to your local machine.
```sh
git clone (https://github.com/duttatreyo/Subdomain-Scraper)
```



## Usage
To run the script, navigate to the project directory in the terminal and run:
```$python subdomain_finder.py```


## NOTE
``` To print restriction from 'robots.txt' add the line```
 ```print(f"Skipping {url} due to robots.txt restrictions")``` under `if 'Disallow: /' in robots_response.text:` in function `check_domain`
 
 AND
 
under `except requests.RequestException`
            ```print(f"Error accessing {url}: {str(e)}")``` 
```
## Follow the on-screen prompt and enter the domain for which you want to find subdomains and scrape public data.


