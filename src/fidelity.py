"""
The task is to fetch book details and corresponding author details using two synchronysed calls.
merge the results and sort the results by book name.

import pandas as pd


def fetch_books_authors(url1, url2, thresh: 7):


    Args:
        url1: List of book names ratings, book endpoint,
        url2: author, book name names endpoint
        thresh: Min Book rating

    Returns:


    import logging
    import requests
    # psuedocode:
    # read url endpoint:
    #
    # match each author
    # filter: threshold

    import urllib3
    try:
        book_details = requests.get(url1)
        author_details = requests.get(url2)
    except:
        pass

    # thresh: 7
    # book_details=pd.DataFrame([['b1', 9], ['b2', 6]])
    book_details = pd.DataFrame(book_details) # --> url1, url2
    author_details = pd.DataFrame(author_details)
    merged_details = book_details.join(author_details, on="book_name")
    merged_details = merged_details[lambda x: x.rating>thresh for x in merged_details["ratings"]]

    return

"""