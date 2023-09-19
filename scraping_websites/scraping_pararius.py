from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import uuid
import config as cfg


def pararius(existing_houses):
    new_pararius_houses = []

    url = f"https://www.pararius.nl/huurwoningen/{cfg.location}/0-{cfg.max_price}/{cfg.min_rooms}-slaapkamers"

    # Set up Selenium options
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--disable-gpu")  # Disable GPU acceleration
    options.add_argument("--no-sandbox")  # Disable sandbox mode

    # Set up Chrome driver
    driver_path = "/path/to/chromedriver"  # Replace with path to your Chromedriver executable
    driver = webdriver.Chrome(options=options)

    # Load the Pararius website
    driver.get(url)

    # Wait for page to load and execute JavaScript to show all listings
    driver.implicitly_wait(10)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Extract HTML from the page
    html = driver.page_source

    browser = webdriver.Chrome()

    # Load the webpage
    browser.get(url)

    # Wait for the page to load and activate JavaScript
    browser.execute_script("return navigator.userAgent")

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Find all listing elements and extract information
    listings = soup.find_all("li", class_="search-list__item search-list__item--listing")
    for listing in listings:
        # Extract information from listing element
        title = listing.find("h2", class_="listing-search-item__title").get_text().strip()
        price = listing.find("div", class_="listing-search-item__price").get_text().strip().replace('.', '')
        address = listing.find("div", class_="listing-search-item__sub-title'").get_text().strip()
        rooms = listing.find("li",
                             class_="illustrated-features__item illustrated-features__item--number-of-rooms").get_text().strip()
        link = listing.find("a", class_="listing-search-item__link")["href"]
        full_link = 'https://www.pararius.nl' + link

        if full_link not in existing_houses:
            if int(re.findall(r'\d+', price)[0]) <= cfg.max_price:
                if cfg.location in address.lower():
                    if int(re.findall(r'\d+', rooms)[0]) >= cfg.min_rooms:
                        new_pararius_houses.append({'house_id': uuid.uuid4(),
                                                    'url': full_link,
                                                    'address': address,
                                                    'price': price,
                                                    'number_rooms': rooms}
                                                   )

    # Quit the driver
    driver.quit()

    return new_pararius_houses
