#!/usr/bin/env python
# coding: utf-8

# # Creating 2D Lists

# Dua dimensi list adalah struktur data dimana satu dimensi list dikelompokkan dan penggunaan dua dimensi lists ini cukup sering digunakan dalam pemrograman.
# 
# Untuk membuat list dua dimensi, sebuah list harus dibuat di dalam list. Untuk lebih jelasnya mari kita perhatikan gambar di bawah ini yaitu dua dimensi list dengan 3 baris dan 3 kolom.

# ![2d_list.jpg](attachment:2d_list.jpg)

# In[15]:


#cara membuat 2d list 
#dimulai dengan 0 untuk elemen pertama
list_array = [[1,2,3], [4,5,6], [7,8,9]]


# In[16]:


print(list_array)


# In[17]:


list_array[0]


# In[18]:


list_array = [[1,2,3],[4,5,6],[7,8,9]]
list_array[0]


# Untuk mengakses elemen secara individual dari 2D list, kita dapat menggunakan dua kali [ ] (tanda kurung siku) dan tentukan indeks baris dan indeks kolom di dalam [ ].

# In[20]:


list_array = [[1,2,3],[4,5,6],[7,8,9]]
list_array[0][2] #list yang 0 merupakan vertikal dan yang 2 merupakan list horizontal


# ![list_.jpg](attachment:list_.jpg)

# Mengganti elemen dalam sebuah 2D lists :

# In[21]:


list_array[1][1] = 300


# In[22]:


print(list_array[1])


# ## Double Loop 2D Lists 
# Seperti tipe data list, kita juga bisa mengakses elemen 2D list dengan menggunakan for loop. Jika kita menggunakan for loop untuk 2D list , maka akan mengakses elemen secara berurutan dari yang pertama hingga yang terakhir. Karena ini adalah sebuah 2D list, maka tipe data dari masing-masing elemen tersebut adalah sebuah list.

# In[24]:


list_array = [[1,2,3],[4,5,6],[7,8,9]]
for item in list_array:
    print('item=',item)


# ## 2D Lists dengan Double For Loop  

# Jika kita ingin mengakses elemen individual dari 2D list, kita tidak bisa menggunakan satu buah for loop saja seperti contoh di atas, sehingga kita perlu menggunakan double for loop.

# In[26]:


list_array=[[1,2,3],[4,5,6],[7,8,9]]
for i in list_array:
    for j in i:
        print(j,end= '')
    print()


# Contoh di atas adalah contoh program yang menampilkan individual elemen dari list_array menggunakan double for loop. Program tersebut terdiri dari dua tahap:
# 
# - for loop luar for i in list_array: mengakses kolom demi kolom dari seluruh lists ke variable i.
# - for loop dalam for j in i: mengakses seluruh elemen dari i dan mencetaknya ke console.

# In[28]:


list_array = [[1,2,3],[4,5,6],[7,8,9]]
for item in list_array:
  if item == [1,2,3]:
    print("Hello!")
    continue
  print('item =',item)

