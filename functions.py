# Importing necessaries libraries
import requests
import csv
import numpy as np
import pandas as pd
import ast
import seaborn as sns
import matplotlib.pyplot as plt

def get_book_list(params):
    """
    Function to receive a URL (string) and parameters (dictionary) to search by.
    The output is a list of dictionaries, each being one book from the website's
    result.
    """
    response = requests.get('https://openlibrary.org/search.json', params=params).json()
    return response['docs']

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
            # I used "try-except" to avoid errors.
            try:
                book_dict[column] = book[column]
            except KeyError as e:
                book_dict[column] = ''
                continue
        book_list_selected.append(book_dict)
    return book_list_selected

def create_csv(file_path_name:str, cleanedup_list):
    """
    Function to receive a path to where to file is going to be created, including
    its name, (string) and a list of books, list of dictionaries, (list) to
    create a csv file.
    The output is a csv file created in the designated location.
    """
    with open(f'{file_path_name}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=cleanedup_list[0].keys())
        writer.writeheader()
        for book in cleanedup_list:
            writer.writerow(book)
        return book

def read_csv(file_path_name):
    """
    Function to receive a path to where to file is saved (string) to read the
    csv file.
    The output is the csv file opened.
    """
    file = pd.read_csv(f'{file_path_name}.csv')
    return file


def make_df(book_list:list, fields:list):
    df = pd.DataFrame(book_list)
    df_sorted = df[fields]
    return df_sorted
