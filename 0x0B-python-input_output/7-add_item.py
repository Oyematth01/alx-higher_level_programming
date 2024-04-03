#!/usr/bin/python3
import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_item_to_list(item):
    # Load existing items from file or initialize an empty list
    if path.exists('add_item.json'):
        items = load_from_json_file('add_item.json')
    else:
        items = []

    # Add new item to the list
    items.append(item)

    # Save the updated list to file
    save_to_json_file(items, 'add_item.json')


if __name__ == "__main__":
    # Iterate over command line arguments and add them to the list
    for arg in sys.argv[1:]:
        add_item_to_list(arg)
