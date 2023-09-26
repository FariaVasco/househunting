import os
import config as cfg


def add_new_houses(new_links):

    existing_houses = open(os.path.join(cfg.root_dir, 'helpers/existing_houses.txt'), 'a')

    for house in new_links:
        existing_houses.write("\n" + house['url'])

    return None
