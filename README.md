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

## Setup

1. Clone this repository to your local machine.
```sh
git clone <repository-url>

cd <project-directory>
pip install -r requirements.txt
