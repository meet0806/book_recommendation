from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Books
import pandas as pd
import numpy as np
import random as r


# Create your views here.
# def Load(request):
#     return redirect(Main)

obj_list = []


def Main(request):
    # editing
    bookdf = pd.read_csv('books.csv')
    ratedf = pd.read_csv('ratings.csv')
    dropdf = bookdf.drop(columns=['title', 'average_rating', 'ratings_count', 'language_code', 'id', 'best_book_id', 'work_id', 'books_count', 'isbn', 'ratings_1', 'ratings_2', 'ratings_3',
                                  'ratings_4', 'ratings_5', 'authors', 'work_text_reviews_count', 'isbn13', 'original_publication_year', 'work_ratings_count'])
    # print(dropdf.columns)

    # print("getting book of bookid till 10000")
    nndf = dropdf[dropdf['book_id'] <= 10000]
    newdf = nndf.dropna()

    # nameerr=newdf['original_title']
    # print(list(nameerr))

    mergedf = pd.merge(dropdf, ratedf)
    # print(mergedf.head(5))
    # print(mergedf.columns)
    listindex = list(mergedf['book_id'].unique())
    # ---------------------
    # Size = int(input("Enter number of Books: "))
    # print(Size)

    Size = 10

    inx = []
    list_book = []

    while True:
        if len(inx) == Size:
            break
        else:
            rannum = r.choice(listindex)
            if rannum not in inx:
                inx.append(rannum)

    # -----------------
    for i in range(len(inx)):
        # print(inx[i])
        new_df = mergedf.loc[inx[i], ['original_title', 'image_url']]
        bList = list(new_df)
        list_book.append(bList)

    # print('book display')
    # print(list_book)
    # sent

    obj = Books()
    obj.id = 0
    obj.name = list_book[0][0]
    obj.img = list_book[0][1]

    obj1 = Books()
    obj1.id = 1
    obj1.name = list_book[1][0]
    obj1.img = list_book[1][1]

    obj2 = Books()
    obj2.id = 2
    obj2.name = list_book[2][0]
    obj2.img = list_book[2][1]

    obj3 = Books()
    obj3.id = 3
    obj3.name = list_book[3][0]
    obj3.img = list_book[3][1]

    obj4 = Books()
    obj4.id = 4
    obj4.name = list_book[4][0]
    obj4.img = list_book[4][1]

    obj5 = Books()
    obj5.id = 5
    obj5.name = list_book[5][0]
    obj5.img = list_book[5][1]

    obj6 = Books()
    obj6.id = 6
    obj6.name = list_book[6][0]
    obj6.img = list_book[6][1]

    obj7 = Books()
    obj7.id = 7
    obj7.name = list_book[7][0]
    obj7.img = list_book[7][1]

    obj8 = Books()
    obj8.id = 8
    obj8.name = list_book[8][0]
    obj8.img = list_book[8][1]

    obj9 = Books()
    obj9.id = 9
    obj9.name = list_book[9][0]
    obj9.img = list_book[9][1]

    global obj_list
    obj_list = [obj, obj1, obj2, obj3, obj4,
                obj5, obj6, obj7, obj8, obj9]

    return render(request, 'base.html', {'book': obj_list})


def Sum(request):

    def get_simi_book(bookname, user_rat):
        simi_rating = item_simi[bookname]*(user_rat-2.5)
        simi_rating = simi_rating.sort_values(ascending=False)
        return simi_rating

    global obj_list

    var0 = request.POST.get('rating0', False)
    var1 = request.POST.get('rating1', False)
    var2 = request.POST.get('rating2', False)
    var3 = request.POST.get('rating3', False)
    var4 = request.POST.get('rating4', False)
    var5 = request.POST.get('rating5', False)
    var6 = request.POST.get('rating6', False)
    var7 = request.POST.get('rating7', False)
    var8 = request.POST.get('rating8', False)
    var9 = request.POST.get('rating9', False)

    var_list = [var0, var1, var2, var3, var4, var5, var6, var7, var8, var9]

    name_list = []
    for i in range(len(obj_list)):
        name_list.append(obj_list[i].name)

    titleandrate = []
    # forming list of list

    for chkspace in range(len(var_list)):
        randomlist = []
        if(var_list[chkspace] != ''):
            title = name_list[chkspace]
            rate_got = int(var_list[chkspace])
            randomlist = [(title, rate_got)]
            titleandrate.append(randomlist)

    # print(titleandrate)

    # get name of those books whose our user  have rated

    # algo for recommmendation

    book_df = pd.read_csv('books.csv')
    rating_df = pd.read_csv('ratings.csv')
    # print(rating_df.head())
    book_df = book_df.drop(columns=['title', 'average_rating', 'ratings_count', 'language_code', 'id', 'best_book_id', 'work_id', 'books_count', 'isbn', 'ratings_1', 'ratings_2', 'ratings_3',
                                    'ratings_4', 'ratings_5', 'authors', 'work_text_reviews_count', 'isbn13', 'original_publication_year', 'work_ratings_count'], axis=1)
    # --------------------

    # print(book_df.columns)
    # print("getting book of bookid till 10000")

    nndf = book_df[book_df['book_id'] <= 10000]
    # print(list(nndf['original_title']))

    # print(nndf.isnull().sum())
    # print(nndf.shape)
    # print(nndf.dropna())
    newdf = nndf.dropna()
    # print('newdf')
    # print(newdf.head())
    # print(newdf.shape)

    # --------------------
    # print(book_df.shape)
    merge_df = pd.merge(book_df, rating_df)
    # print(merge_df.head())
    user_rating = merge_df.pivot_table(index=['user_id'], columns=['original_title'], values='rating')
    user_rating = user_rating.dropna(thresh=10, axis=1).fillna(0)
    item_simi = user_rating.corr(method='pearson')
    # print(item_simi.head(10))

    # recommendation

    # enter book title and it rating
    simi_book = pd.DataFrame()

    for i in range(len(titleandrate)):
        for book, rating in titleandrate[i]:
            simi_book = simi_book.append(get_simi_book(book, rating), ignore_index=True)

    # print(simi_book.sum().sort_values(ascending=True).head(10))

    # print('hey1')
    export_names = simi_book.sum().sort_values(ascending=False).head(10)
    # print(export_names)
    # # name collection and related img urls
    exportnames = list(export_names.keys())
    # print(exportnames)
    imageandtitle = merge_df.drop(columns=['book_id', 'small_image_url', 'user_id', 'rating']).drop_duplicates()
    # print(imageandtitle)

    # now img and link sending
    imgdislist = []

    for i in exportnames:
        tt=list(imageandtitle[imageandtitle['original_title']==i]['image_url'])
        # print(tt)
        imgdislist.append(tt)


    # print("final")
    # print(imgdislist)


    # object
    ob = Books()
    ob.name = exportnames[0]
    ob.img = imgdislist[0][0]

    ob1 = Books()
    ob1.name = exportnames[1]
    ob1.img = imgdislist[1][0]

    ob2 = Books()
    ob2.name = exportnames[2]
    ob2.img = imgdislist[2][0]

    ob3 = Books()
    ob3.name = exportnames[3]
    ob3.img = imgdislist[3][0]

    ob4 = Books()
    ob4.name = exportnames[4]
    ob4.img = imgdislist[4][0]

    ob5 = Books()
    ob5.name = exportnames[5]
    ob5.img = imgdislist[5][0]

    ob6 = Books()
    ob6.name = exportnames[6]
    ob6.img = imgdislist[6][0]

    ob7 = Books()
    ob7.name = exportnames[7]
    ob7.img = imgdislist[7][0]

    ob8 = Books()
    ob8.name = exportnames[8]
    ob8.img = imgdislist[8][0]

    ob9 = Books()
    ob9.name = exportnames[9]
    ob9.img = imgdislist[9][0]
    
    ob_list=[ob,ob1,ob2,ob3,ob4,ob5,ob6,ob7,ob8,ob9]
    # -----------
# render(request, 'algoresult.html', {'book_details': exportnames})
    return render(request, 'algoresult.html', {'books':ob_list})
