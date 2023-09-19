from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import config as cfg


def funda(existing_houses):

    has_balcony = True
    available = 'beschikbaar'
    new_funda_houses = []
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    # Load the search results page with Selenium WebDriver
    url = f'https://www.funda.nl/huur/{cfg.location}/{available}/0-{str(cfg.max_price)}/{cfg.min_rooms}+kamers/{"" if has_balcony else "-"}balkon/'
    # driver.get(url)

    response = requests.get(url)

    print('We got the data')
    # Wait for the search results to load
    # cookie_acceptance_dialog = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'didomi-popup-view')))
    # accept_button = cookie_acceptance_dialog.find_element(By.ID, "didomi-notice-agree-button")
    # accept_button.click()
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.search-result')))

    # Get the HTML content of the page
    html_content = driver.page_source
    html_content = response.text

    # Use Beautiful Soup to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the listings on the page
    listings = soup.find_all('div', class_='search-content-output')

    new_titles = []

    # Loop through the listings and filter based on the specified criteria
    apartments = listings[0].find('ol', class_='search-results')
    section = apartments.find('li', class_='search-result')
    apartment = section.find('div', class_='search-result-main')

    link = apartment.find('div', class_='search-result-thumbnail-container').find('div', class_='search-result-media').find('a').attrs['href']

    specific_information = apartment.find('div', class_='search-result-content').find('div', class_='search-result-content-inner')

    address = specific_information.find('div')

    if details:
        details_text = details.text.strip()

        if details_text not in existing_houses:
            new_titles.append(details_text)

    # Close the browser
    driver.quit()

    return new_funda_houses
