def add_new_houses(new_links):

    existing_houses = open('helpers/existing_houses.txt', 'a')

    for house in new_links:
        existing_houses.write("\n" + house['url'])

    return None
