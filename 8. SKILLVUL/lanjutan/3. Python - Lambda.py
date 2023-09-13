#!/usr/bin/env python
# coding: utf-8

# ##  Lambda - Expression and Syntax

# Lamda adalah fungsi tanpa nama dan disebut juga lambda expression. Lambda bisa disebut juga anynymus function. 

# - Fungsi Reguler : terdiri dari kata kunci def, nama function, paramter, titik 2 body function
# - Fungsi Lambda  : Parameter dan body Function

# ![lambda.jpg](attachment:lambda.jpg)

# Lambda function hanya memiliki satu expression tapi boleh memiliki beberapa parameter. 
# sintaksnya seperti dibawah ini 

# lambda [parameter1, parameter2, ...] : [expression]

# **Dengan def Keyword**

# In[5]:


def add(x,y):
    return x + y 
print ("total dari 100 dan 200 adalah :", add(100,200))


# **Dengan Lambda**

# In[9]:


add = lambda x,y :x + y 
print("total dari 100 dan 200 adalah:", add(100,200))


# Kita dapat mendefiniskan lambda function dengan lambda keyword. Expression menerima x, y sebagai parameter dan mengembalikan x + y. Contoh lambda function di atas bertujuan menambahkan dua argumen seperti def add(x, y):. Ini memverifikasi bahwa ** lambda function berhasil melakukan tugas function yang dilakukan oleh function biasa**.

# ## Lambda - Filter

# Python menawarkan banyak built-in function. Salah satu contohnya adalah filter(). Function filter() **menerima iterable elements dan hanya mengembalikan elemen yang True dalam satu bundel.**
# Sintaks dari function filter() adalah sebagai berikut:

# **filter((fungsi_yang_akan_diaplikasikan, {iterable object})**

# In[28]:


list_umur = [34,39,20,18,13,54]
print("Umur yang dewasa:")
for a in filter(lambda x:x >=19, list_umur):#filter umur menggunakan fungsi filter
    print(a,end = '   ')


# Lambda Function mengembalikan True untuk x sama dengan atau lebih dari 19 dan menggunakan filter(), kita bisa menyaring dan hanya mencetak nilai usia yang sama dengan atau lebih dari 19

# ![lambda_1.jpg](attachment:lambda_1.jpg)

# In[1]:


list_umur = [1,10,30,20,15]
for a in filter(lambda x:x%2 ==0, list_umur):
    print(a,end=' ')


# ## Lambda - Map 

# Mengeksekusi sebuah function untuk setiap iterable items. Setiap item dijadikan argumen pada function yang diinginkan. 
# 

# Sintaks dari map adalah sebagai berikut 

# map(function_to be applied , iterable object, ...)

# In[3]:


a = [1,2,3,4,5,6,7]
a_kuadrat = list(map(lambda b:b **2,a))
print(a_kuadrat)


# ## Lambda - Reduce

# reduce() termasuk merupakan bagian dari module functools. reduce() mengembalikan sebuah nilai dengan menajlankan operasi dengan operasi dengan fungsi yang diberikan pada item dari sebuah iterables object(list, tuple, range). Hampir sama dengan map tapi reduce mengemabilkan nilai tunggal atau single value. 

# In[4]:


from functools import reduce
#Returns the sum of two elements 
def sumTwo(a,b):
    return a+b
result = reduce(sumTwo,[1,2,3,4])
print(result)


# In[5]:


from functools import reduce # mengimport fungsi reduce
a = [1,2,3,4]
n = reduce(lambda x,y : x+y,a)
print(n)


# 1, 2, 3, 4 merupakan items dari list a.
# Pertama, 3 dikembalikan dari lambda x, y: x+y ketika dua nilai pertama 1, 2 diberikan sebagai input.
# Kemudian, nilai yang telah dikembalikan sebelumnya yaitu 3, dengan item ketiga 3, diberikan sebagai input kembali. Kemudian, hasilnya akan mengembalikan 6 (3 + 3). Kemudian nilai 6 dan item terakhir 4 diberikan sebagai input kembali, sehingga mengembalikan nilai akhir 10.

# In[6]:


from functools import reduce
a = [1,2,3]
n = reduce(lambda x,y : x +(x*y),a)
print (n)

