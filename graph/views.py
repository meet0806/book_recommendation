from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import random as rd
import numpy as np

# Create your views here.


def Graph(request):
    # sending data
    return render(request, 'graph.html')


def Graph1(request):
    # sending data
    l = []
    df = pd.read_csv("books.csv")
    print(df)
    index = rd.randrange(0, 10000)
    print(index)
    df = df.drop(columns=['original_title', 'book_id', 'image_url', 'small_image_url', 'ratings_count', 'language_code', 'id', 'best_book_id',
                          'work_id', 'books_count', 'isbn', 'authors', 'work_text_reviews_count', 'isbn13', 'original_publication_year', 'work_ratings_count'])
    print(df)
    new_df = df.loc[index, ['ratings_1', 'ratings_2',
                            'ratings_3', 'ratings_4', 'ratings_5', 'average_rating']]
    print(new_df)
    print(new_df[0])
    for val in new_df:
        l.append(val)

    t = df.loc[index, ['title']]
    print(t[0])
    send = {
        'graph1data': l,
        'title': t[0]
    }
    # print(int(new_df[5])) avg rating
    return render(request, 'graph1.html', send)


# def Graph2(request):
#     # sending data
#     l = []
#     df = pd.read_csv("books.csv")
#     print(df)
#     index = rd.randrange(0, 10000)
#     print(index)
#     df = df.drop(columns=['original_title', 'book_id', 'image_url', 'small_image_url', 'ratings_count', 'language_code', 'id', 'best_book_id',
#                           'work_id', 'books_count', 'isbn', 'authors', 'work_text_reviews_count', 'isbn13', 'original_publication_year', 'work_ratings_count'])
#     print(df)
#     new_df = df.loc[index, ['ratings_1', 'ratings_2',
#                             'ratings_3', 'ratings_4', 'ratings_5', 'average_rating']]
#     print(new_df)
#     print(new_df[0])
#     for val in new_df:
#         l.append(val)

#     t = df.loc[index, ['title']]
#     print(t[0])
#     send = {
#         'graph2data': l,
#         'title': t[0]
#     }
#     # l = [1, 2, 3, 4, 5, 6]
#     return render(request, 'graph2.html', send)

def Graph2(request):
    # sending data
    l = []
    df = pd.read_csv("books.csv")
    print(df)
    index = rd.randrange(0, 10000)
    print(index)
    df = df.drop(columns=['ratings_1', 'ratings_2', 'ratings_3', 'ratings_4', 'ratings_5', 'average_rating','original_title', 'book_id', 'image_url', 'small_image_url', 'ratings_count', 'language_code', 'id', 'best_book_id',
                          'work_id', 'books_count', 'isbn', 'authors', 'isbn13', 'original_publication_year'])
    print(df)
    new_df = df.loc[index, ['work_text_reviews_count', 'work_ratings_count']]
    print(new_df)
    print(new_df[0])
    for val in new_df:
        l.append(val)

    t = df.loc[index, ['title']]
    print(t[0])
    send = {
        'graph2data': l,
        'title': t[0]
    }
    # l = [1, 2, 3, 4, 5, 6]
    return render(request, 'graph2.html', send)
