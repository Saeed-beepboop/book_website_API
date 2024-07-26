# Importing necessary libraries
import requests
import pandas as pd
import logging

# Setting up logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def get_book_list(params):
    """
    Function to receive a URL (string) and parameters (dictionary) to search by.
    The output is a list of dictionaries, each being one book from the website's
    result.
    """
    try:
        response = requests.get('https://openlibrary.org/search.json', params=params)
        response.raise_for_status()
        book_list = response.json()
    except requests.exceptions.RequestException as e:
        logger.error("Problem fetching book list")
        raise SystemExit(e)
    return book_list['docs']

def get_book_info(book_list:list, columns_of_interest:list):
    """
    Function to receive a list of books, list of dictionaries, (list) and names
    of columns of interest (list) to remove unnecessary information.
    The output is a list of dictionaries with only columns necessary for our need.
    """
    book_list_selected = []
    for book in book_list:
        book_dict = {}
        for column in columns_of_interest:
            # Since some entries may be missing in the columns of interest,
            # I used "try-except" to handle exceptions.
            try:
                if column in pd.DataFrame(book_list).columns:
                    book_dict[column] = book[column]
            except KeyError as e:
                book_dict[column] = ''
                # Error is minor, it can be recorded in the debug for future investigation.
                logger.debug(f"Column of interest missing. Moving on...\n{str(e)}")
                continue
        book_list_selected.append(book_dict)
    return book_list_selected

def make_df(book_list:list, fields:list):
    df = pd.DataFrame(book_list)
    df_sorted = df[fields]
    return df_sorted
