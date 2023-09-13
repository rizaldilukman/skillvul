#!/usr/bin/env python
# coding: utf-8

# ## SET - Definition and Declaration 

# Tipe data set adalah tipe data dasar yang disediakan oleh Python tetapi tidak disediakan di tipe dasar bahasa pemrograman lain. Beberapa poin penting dalam tipe data set : 
# - Dalam set, tidak diperbolehkan ada data yang sama atau duplikat sehingga data di dalam set sifatnya adalah unik (tidak boleh ada data yang sama)
# - Tipe data set adalah unordered sehingga item dapat muncul dalam urutan yang berbeda setiap kali menggunakannya dan kita tidak bisa mengakses data menggunankan index atau key seperti tipe data list atau dictionary
# - Tipe data tidak bisa diubah setelah kita membuatnya

# ### Set Declaration 
# Beberapa cara untuk membuat tipe data set, 

# ![set_declaration.jpg](attachment:set_declaration.jpg)

# In[2]:


#contoh 
days_list = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']#list
days_set = set(days_list) #membuat set dari list
print (days_set)


# In[3]:


fruits_tuple = ('apple','orange','water melon')
fruits_set = set(fruits_tuple) # membuat set dari tuple
print(fruits_set)


# ## Set - Check Value in Sets (mengecek apakah ada data ada di dalam set)

# Untuk mengakses value yang ada di dalam set, kita bisa menggunakan for loop untuk melakukan **iterasi** untuk mendapatkan item yang ada di dalam set

# In[5]:


numbers = {2,1,3}
for x in numbers:
    print (x)


# kita juga bisa melakukan validasi untuk mengecek apakah sebuah item ada di dalam sebuah set dengan menggunakan operator **in** yang kita juga bisa pakai dalam tipe data list.

# In[7]:


numbers = {2,1,3}
if 1 in numbers:
    print('1 terdapat dalam set')


# **Menambah dan mengurangi atau menghapus value** 
# Menggunakan fungsi add() serta remove() 

# In[8]:


numbers = {1,2,3}
numbers.add(4)
print(numbers)


# In[10]:


numbers = {1,2,3,4}
numbers.remove(4)
print(numbers)


# ## Set - Union and Intersections 

# Dalam tipe data set, terdapat beberapa operator yang kita bisa gunakan seperti :
# 
#     - & untuk intersection
#     - | untuk union
#     - - untuk difference of set dan,
#     - ^ untuk symmetric difference

# ### Union (Gabungan) 

# In[11]:


s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}


# ![union.jpg](attachment:union.jpg)

# Union berarti kita mengambil semua data yang ada dari s1 dan s2. Pada Python kita implementasikan seperti kode di bawah ini :

# In[12]:


s1|s2


# ### Intersection (Irisan)

# Intersection berarti kita mengambil irisan data antara s1 dan s2. Pada Python kita implementasikan seperti kode di bawah ini :

# ![intersection.jpg](attachment:intersection.jpg)

# In[13]:


s1 & s2


# In[14]:


s1.intersection(s2)


# ### Set Difference and Symetric Difference  

# ### Difference

# In[ ]:




Dalam tipe data set, terdapat beberapa operator yang kita bisa gunakan seperti :

- & untuk intersection
- | untuk union
- - untuk difference of set dan,
- ^ untuk symmetric difference


# In[16]:


s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}


# ![difference.jpg](attachment:difference.jpg)

# Difference digunakan untuk mengambil data unik dari salah satu set (s1 atau s2) 
# - sehingga penulisan untuk difference cukup krusial karena s1-s2 berbeda artinya dengan s2-s1. 
# - Untuk pola s1-s2 mengambil data yang hanya ada di s1 dan tidak ada di s2, 
# - sementara pola s2-s1 melakukan kebalikannya. Kita bisa membuatnya ke dalam program sebagai berikut:

# In[17]:


s1 - s2 


# In[18]:


s1.difference(s2)


# ### Symmetric difference (ambil keduanya bukan irisan)

# ![symmetric_difference.jpg](attachment:symmetric_difference.jpg)

# - Symmetric difference digunakan untuk mengambil data unik dari kedua set (s1 dan s2) dimana hal ini merupakan kebalikan dari intersection.
# - Symmetric difference mengeliminasi data yang ada di kedua set. Kita bisa membuatnya ke dalam program sebagai berikut:

# In[20]:


s1^s2


# ### Set - Subset and Superset 

# Dalam tipe data set, terdapat istilah superset dan juga subset yang berarti:
# 
# - Sebuah set dapat dikatakan superset apabila mengandung semua elemen dari set yang lain.
# - Dan sebuah set dapat dikatakan subset apabila seluruh elemen terkandung dari set yang lain.

# In[21]:


A = {1,2}
B = {1,2,3}


# A adalah subset dari B karena semua elemen A terkandung dalam B. B merupakan superset dari A karena B mengandung seluruh elemen dari A.

# Untuk mengecek subset dan superset kita bisa menggunakan fungsi issubset(set) dan issuperset(set). Penggunaan fungsi tersebut bisa kita lihat pada contoh berikut:

# In[22]:


s1 = {1,2,3,4,5}
s2 = {1,2,3}
s3 = {1,2,6}


# In[24]:


s2.issubset(s1) #apakah s2 adalah subset s1


# In[27]:


s3.issubset(s1) #apakah s3 adalah subset dari s1


# In[26]:


s1.issubset(s2) #apakah s1 adalah subset dari s2


# In[28]:


s1.issubset(s3) #apakah s1 adalah subset dari s3


# In[ ]:




