import requests
import json
import uuid


def vbt(existing_houses):
    new_vbt_houses = []
    result = 0
    page = 1
    while result == 0:
        url = 'https://vbtverhuurmakelaars.nl/api/properties/12/{}'.format(page)
        response = requests.get(url)
        if response.status_code != 200:
            result = 1
            continue

        houses = json.loads(response.text)['houses']

        for house in houses:
            full_link = 'https://vbtverhuurmakelaars.nl' + house['url']
            if full_link not in existing_houses:
                if house['status']['name'] == 'available':
                    if house['address']['city'] == 'Amsterdam':
                        if house['prices']['rental']['price'] <= 1750:
                            if house['rooms'] >= 3:
                                new_vbt_houses.append({'house_id': uuid.uuid4(),
                                                       'url': full_link,
                                                       'city': house['address']['city'],
                                                       'address': house['address']['house'],
                                                       'listing_type': house['prices']['category'],
                                                       'price': house['prices']['rental']['price'] if house['prices']['category'] ==
                                                                                                      'rent' else
                                                       house['prices']['purchase']['price'],
                                                       'service_costs': house['prices']['rental']['serviceCharges'] if
                                                       house['prices']['category'] ==
                                                       'rent' else house['prices']['purchase']['serviceCostsPerMonth'],
                                                       'length_type': house['prices']['rental']['type'] if house['prices'][
                                                                                                               'category'] ==
                                                                                                           'rent' else None,
                                                       'min_months': house['prices']['rental']['minMonths'] if house['prices'][
                                                                                                                   'category'] ==
                                                                                                               'rent' else None,
                                                       'status': house['status']['name'],
                                                       'house_type': house['attributes']['type']['category'],
                                                       ## 'surface': house['surface'],
                                                       'number_rooms': house['rooms'],
                                                       'image': house['image'],
                                                       'advertising_id': house['id'],
                                                       'external_url': house['source']['externalLink'],
                                                       'imported_at': house['source']['lastImported']})

        page += 1

    return new_vbt_houses
