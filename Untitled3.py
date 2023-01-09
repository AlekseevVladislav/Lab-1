#!/usr/bin/env python
# coding: utf-8

# In[192]:


import pandas as pd
import numpy as np
import random
import csv

def search_book(a):
    books = set()
    for i in range(len(train2)):
        if train2["Автор"][i] == a and float(train2["Цена поступления"][i]) >= 200:
            print(train2["Название"][i])

f = open('result.txt','w')
a = []

with open('books.csv','r') as csvfile:
    table = csv.reader(csvfile, delimiter = ';')
    for row in table:
        a.append(row)
        
col = a[0]
a = a[1:len(a)]
a = pd.DataFrame(a, columns = col)
train2 = a
counter = 0
for i in range(len(train2)):
    if len((train2["Название"][i])) > 30:
        counter += 1
        
print("Количество книг с названием <30 символов :",counter)
print()
txt = input("Введите автора: ")
print()
search_book(txt)

a = [random.randint(0,len(train)) for i in range(20)]
a.sort()
list_of_books = []
counter = 0
f.write("Номер в списке) ID книги, Автор. название книги - дата выхода" + "\n")

for i in a:
    counter += 1
    q = str(str(i) +") "+train2["ID"][i] + ", " + train2["Автор"][i] + ". " + train2["Название"][i] + " - " + train2["Дата поступления"][i]).replace('"', '')
    list_of_books.append(q)

for i in list_of_books:
    f.write(i+'\n')

f.close()

f = open('result.txt','w')
a = []
with open('books-en.csv','r') as csvfile:
    table = csv.reader(csvfile, delimiter = ';')
    for row in table:
        a.append(row)
        
col = a[0]
a = a[1:len(a)]
a = pd.DataFrame(a, columns = col)

print()

print("Список издательств")
for i in set(a['Publisher']):
    print(i)
    
print()
    
a = a.astype({'Downloads': np.int})
a = a.sort_values(by='Downloads', ascending=False)
a.head(20)

