import streamlit as st

import numpy as np
import pandas as pd

from functions import get_book_list, get_book_info, make_df

# st.write('Welcome to my app')

st.markdown("""# Parsing Virtual Bookstore
#### Providing parameters and receiving datasets
#### Live Demo""")

# with st.sidebar:
    # genre_entry = st.sidebar.text

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
    'Select the parameter category to search on https://openlibrary.org/', options) # Check the output type. Has to be list of strings

# Text input field
user_text = st.text_area('Enter the search terms, in the same order as parameters chosen above, separated by comma') # Check the output type. Has to be list of strings
user_text = [item.strip() for item in user_text.split(',')]

fields = st.multiselect(
    'Select the fields to include in the result - leave empty to view all of the fields', options)

# sort_by = st.selectbox(
#     'Select the field to sort by (leave empty if sorting is not desired)',
#     ["",
#      "key",
#      "redirects",
#      "title",
#      "subtitle",
#      "alternative_title",
#      "alternative_subtitle",
#      "cover_i",
#      "ebook_access",
#      "edition_count",
#      "edition_key",
#      "format",
#      "by_statement",
#      "publish_date",
#      "lccn",
#      "ia",
#      "oclc",
#      "isbn",
#      "contributor",
#      "publish_place",
#      "publisher",
#      "first_sentence",
#      "author_key",
#      "author_name",
#      "author_alternative_name",
#      "subject",
#      "person",
#      "place",
#      "time",
#      "has_fulltext",
#      "title_suggest",
#      "publish_year",
#      "language",
#      "number_of_pages_median",
#      "ia_count",
#      "publisher_facet",
#      "author_facet",
#      "first_publish_year",
#      "ratings_count",
#      "readinglog_count",
#      "want_to_read_count",
#      "currently_reading_count",
#      "already_read_count"])

submitted = st.button("Submit", key="submit_button")
if submitted:
    if user_text:
        st.success('Parameters, search terms, and fields submitted successfully!')
        parameters = {}
        for p, t in zip(params, user_text):
            parameters[p] = t

        # parameters['sort'] = sort_by
        # st.write(f"Result of {parameters} and viewing {fields} fields, sorted by {sort_by}:")
        if not fields:
                fields = 'all'
        st.write(f"Result of {parameters} and viewing {fields} fields:")
        # st.write(f'user_text type is {type(user_text)}')
        # st.write(f'params type is {type(params)}')
        st.write(f'parameters are {parameters}')

        with st.spinner('Calculating...'):
            if fields == 'all':
                fields = options
            book_list_result = get_book_list(parameters)
            book_info_result = get_book_info(book_list_result, fields)
            book_df_result = make_df(book_info_result, fields)
            for column in book_df_result.columns:

                # if book_df_result[column].dtype != 'O':
                #     book_df_result[column] = book_df_result[column].apply(lambda x: x if isinstance(x, str) else str(x))
                # if 'isbn' in df.columns:

                book_df_result[column] = book_df_result[column].astype(str)
            book_df_result = book_df_result.fillna('')
            st.dataframe(book_df_result)
    else:
        st.write("Please enter a search term.")




### ADD SORT, PUBLISH ON STREAMLIT CLOUD



# years = st.slider('For how many years are you planning your anime to run?', 1, 20)

# result = st.markdown("There's a ***(from saved model) certainty that your
# anime would contribute {result from passing the entry through the model} percent
# to the visits to japan.")



# outcome = tidy_text(user_text)

#     # Submit button
#     if st.button("Submit Search Terms"):
#         # Process the entered text when the submit button is clicked
#         if user_text:
#             st.success('Categories and subcategories submitted successfully!')
#             st.write(f"List of questions and responses containing the following categories and subcategories:")

#             catsubcat_dict = {}
#             for cats in outcome:
#                 catsubcat_dict[cats[0]] = cats[1:]

#             listkeys_catsubcat_dict = []
#             for key in catsubcat_dict.keys():
#                 listkeys_catsubcat_dict.append(key)

#             for num in range(0,len(catsubcat_dict.keys())):
#                 st.write(f"**Category {num+1}**: {listkeys_catsubcat_dict[num]}")
#                 for n in range(0,len(catsubcat_dict[listkeys_catsubcat_dict[num]])):
#                     st.markdown(f"**Subcategory {n+1}**: {catsubcat_dict[listkeys_catsubcat_dict[num]][n]}")

#                     phrase_i, phrase_p = separate_interview_sentences(catsubcat_dict[listkeys_catsubcat_dict[num]][n], lines)
#                     # Display each item of the first list
#                     # st.write(f"List of questions and responses containing '{user_text}':")
#                     for idx, (item1, item2) in enumerate(zip(phrase_i, phrase_p), start=1):
#                         st.markdown(f"- Instance {idx}")
#                         st.write(f"Question: {item1}")
#                         st.write(f"Response: {item2}")

#         else:
#             st.write("Please enter a category and a subcategory.")
