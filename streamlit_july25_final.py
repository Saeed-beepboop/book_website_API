import streamlit as st

import numpy as np
import pandas as pd
import requests
import csv
import numpy as np
import pandas as pd
import ast
import seaborn as sns
import matplotlib.pyplot as plt

from functions import get_book_list, get_book_info, make_df

st.markdown("""# Parse Virtual Bookstore
#### by providing search parameters and receive datasets
#### Live Demo
###### Source: https://openlibrary.org/""")

options =["key",
     "redirects",
     "title",
     "subtitle",
     "alternative_title",
     "alternative_subtitle",
     "cover_i",
     "ebook_access",
     "edition_count",
     "edition_key",
     "format",
     "by_statement",
     "publish_date",
     "lccn",
     "ia",
     "oclc",
     "isbn",
     "contributor",
     "publish_place",
     "publisher",
     "first_sentence",
     "author_key",
     "author_name",
     "author_alternative_name",
     "subject",
     "person",
     "place",
     "time",
     "has_fulltext",
     "title_suggest",
     "publish_year",
     "language",
     "number_of_pages_median",
     "ia_count",
     "publisher_facet",
     "author_facet",
     "first_publish_year",
     "ratings_count",
     "readinglog_count",
     "want_to_read_count",
     "currently_reading_count",
     "already_read_count"]

params = st.multiselect(
    'Select the parameter categories to search by', options) # Check the output type. Has to be list of strings

user_text = st.text_area('Enter the search terms, in the same order as parameters chosen above, separated by comma') # Check the output type. Has to be list of strings
user_text = [item.strip() for item in user_text.split(',')]

fields = st.multiselect(
    'Select the fields to include in the result - leave empty to view all of the fields', options)

submitted = st.button("Submit", key="submit_button")
if submitted:
    if user_text:
        st.success('Parameters, search terms, and fields submitted successfully!')
        parameters = {}
        for p, t in zip(params, user_text):
            parameters[p] = t
        if not fields:
                fields = 'all'
        st.write("Results:")
        with st.spinner('Calculating...'):
            if fields == 'all':
                fields = options
            book_list_result = get_book_list(parameters)
            book_info_result = get_book_info(book_list_result, fields)
            try:
                book_df_result = make_df(book_info_result, fields)
                for column in book_df_result.columns:
                    book_df_result[column] = book_df_result[column].astype(str)
                try:
                    book_df_result = book_df_result.fillna('')
                    st.dataframe(book_df_result)
                except NameError as e:
                    st.write("None found. Search terms may be incorrect.")
            except KeyError as e:
                st.write("None found. Search terms may be incorrect.")
    else:
        st.write("Please enter a search term.")
