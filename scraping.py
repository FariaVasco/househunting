from get_data import get_data
from scraping_websites.scraping_vbt import vbt
from scraping_websites.scraping_funda import funda
from scraping_websites.scraping_pararius import pararius
from send_email import send_email
from new_houses import add_new_houses


customers = get_data('customers')
brokers = get_data('brokers')
existing_houses = get_data('existing_houses')

new_houses = []

# new_houses.extend(funda(existing_houses))
# new_houses.extend(pararius(existing_houses))
new_houses.extend(vbt(existing_houses))

links_to_send = []

for customer in customers:
    # customer_links = tailoring(new_houses, customer)
    # if customer_links:
    for link in new_houses:
        links_to_send.append(link)
    if links_to_send:
        send_email(links_to_send, customer)

add_new_houses(new_houses)
