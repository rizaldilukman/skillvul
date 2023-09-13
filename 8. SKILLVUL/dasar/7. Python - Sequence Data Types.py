#!/usr/bin/env python
# coding: utf-8

# # MUTABLE VS IMUTABLE DATA TYPES

# Dalam pemrograman python ada perbedaan mendasar tentang data apakah data tersebut dapat iubah atau tidak dapat diubah : 

# ![mutable.jpg](attachment:mutable.jpg)

# ## IMMUTABLE DATA TYPES

# Adalah jika data telah dibuat  maka value tidak dapat diubah. Maka tipe data tersebut termasuk Immutable data types. Berikut beberapa tipe jenis data yang masuk ke dalam immutable : int, Float, str, tuple

# String merupakan tipe data immutable dan value dari tipe string tidak dapat diubah selain membuat objek baru

# In[8]:


message = ("Welcome to Skilvul")
message[0] = 'p'
print(message)


# dari data diatas bahwa variable message tidak dapat diubah, 
# berbeda dengan contoh kedua dibawah ini 

# In[10]:


#string 
e = "halo, semua!"
print (id(e))
e = 'Halo, Apa kabar?'
print(id(e))
print(e)


# Terlihat pada kode di atas, variable e diberikan sebuah data dengan tipe string 'Halo, semua!'. Kita mencoba untuk mengubah value string dari variabel e dengan 'Halo, Apa kabar?'. Jika kita print, value dari variabel e memang berubah menjadi 'Halo, Apa kabar?' tetapi berbeda dengan tipe data mutable, pada tipe data immutable, id dari variabel tersebut berbeda sebelum dan sesudah dimodifikasi, sehingga ini menandakan bahwa tipe data string adalah immutable.

# ## MUTABLE DATA TYPES

# Adalah jika data telah dibuat dan data masih bisa diubah, berikut beberapa berbagai tipe jenis data alam python yang termasuk mutable : List, Set, Dict

# List merupakan tipe data mutable sehingga dapat merubah variabel dari sebuah list dengan menggunakan fungsi append()

# In[5]:


a= ['apple','banana', 'oranges']
print(id(a))

a.append('grapes')
print('hasil setelah ditambah grapes')
print(id(a))
print(a)


# Dari kode di atas, variabel a merupakan sebuah list yang kemudian kita tambahkan data baru berupa string grapes ke dalam list tersebut. id dari variabel tersebut tidak berubah yang menandakan ini masih sebuah objek yang sama.

# ##  LIST - DECLARATION 

# List digunakan untuk menyimpan data dari tipe data yang berbeda beda secara berurutan. Setiap elemen memiliki address masing - masing disebut sebagai indeks. 
# Nilai indeks di mulai dari 0, dan berlanjut hingga elemmen terakhir yang disebut positive index. Ada juga negative index yang dimulai dari -1, dan memungkinkan anda mengakses elemendari yang terakhir hingga yang pertama. 

# ##  POSITIVE INDEX

# In[15]:


score_list = [87, 84, 95, 67, 88, 94, 63]
score_list


# In[16]:


score_list = [87, 84, 95, 67, 88, 94, 63]
print (score_list[0], score_list[3])


# ## LIST DECLARATION
# 

# Dalam mendeklarasikan list, kita hanya perlu menggunakan keyword list atau menggunakan []. List tidak membatasi tipe data yang bisa terkandung di dalam list, sehingga kita bisa memasukkan data integer, string dan lain-lain ke dalam sebuah list. Untuk memisahkan antara elemen dengan elemen lainnya kita dapat menggunakan ,. Berikut contoh deklarasi sebuah list:

# In[18]:


fruits = ['banana','apple', 'orange', 'kiwi'] #List with strings
print(fruits)
mixed_list = [100,200,'apple', 400] #list dapat memuat tipe data yang berbeda 
print(mixed_list)


# In[19]:


list4 = list(range(1,10)) #dapat juga menggunakan fungsi range untuk membuat angka
list4


# ## LIST INDEXING 
# 

# Dalam sebuah list, index pertama adalah  o, dan item terakhir adalah -1

# Gunakan fungsi len() untuk menghitung jumlah item dalam list (panjang sebuah list)b

# In[20]:


n_list = [11,22,33,44,55,66]
print(n_list)
print(len(n_list))


# Untuk mengakses sebuah list 

# In[23]:


n_list = [11,22,33,44,55,66]
print(n_list[0]) #indeks item pertama dari list adalah 0
print(n_list[1]) #indeks item kedua dari list adalah 1


# Agar selalu berhati hati dalam menggunakan indeks jangan sampai berlebihan melebihi batas maksimum indeks.
# - Maksimum indeks adalah len(n_list)-1
# - Saat menyimpang dari renatng indeks yang dapat diakses, kesalahan yang terjadi adalah indeks out of range. 

# ## NEGATIVE INDEXING 

# Berorientasi pada elemen terakhir dalam list
# - Referensi elemen dimungkinkan dengan menggunakan indeks negatif daftar python
# - Untuk indeks negatif, dengan mengurangi -1 dari elemen terakhir sehingga menjadi -1, -2, -3.

# In[25]:


n_list = [11,22,33,44,55,66]
print(n_list[-1]) #indeks item pertama akhir dari list adalah 0
print(n_list[-2]) #indeks item kedua akhir dari list adalah 1


# ## LIST ADDITION AND DELETION 

# Dalam bahasa pemrograman, sebuah data seringkali berubah - rubah tergantung pemrosesan yang dilakukan, dalam tipe ini, bisa melakukan penambahan, pengurangan dan ekspansi list 

# ## Addition 

# ### Operator 
# - Dapat menggunakan operator untuk dua list yang berbeda tipe
# - Dalam kasus berikut ini, ada penambahan person1 dan person2 akan dimasukkan dalam satu list yaitu person_list.

# In[27]:


person1 = ['David Doe', 20,1,180.0,100.00]
person2 = ['John Smith', 25,1,170.0,70.0]
person_list = person1 + person2
print (person_list)


# ### Append ()
# - Menambahkan single item baru kedalam sebuah akhir list yang sudah ada (menambahkan hanya 1 item)
# 

# In[29]:


a_list = ['a','b','c','d','e']
a_list.append('f') #menambahkan list f
print(a_list)


# ### Extend() 

# - Fungsi extend() digunakan untuk menambahkan list atau item di belakang sebuah list.
# - Seperti contoh di bawah ini, terdapat list1 dan list2. Karena kita mengaplikasikan list1.extend(list2) maka elemen dari list2 yaitu [1, 2, 3] akan ditambahkan ke belakang list1 sehingga elemen pada list1 akan menjadi ['a', 'b', ' c', 1, 2, 3].
# - Namun kita juga dapat memasukkan elemen individual seperti d ke dalam list tersebut

# In[30]:


list1 = ['a','b','c']
list2 = [1,2,3]
list1.extend(list2)
print(list1)

list1.extend('d')
print(list1)


# ## Deletation 

# ## del
# - Dengan menggunakan del kita dapat menghapus item yang ada dalam indeks yang diinginkan

# In[32]:


n_list = [11,22,33,44,55,66]
print(n_list) #print seluruh items

del n_list [3]
print (n_list)


# ## pop ()
# pop() method berfungsi kurang lebih mirip dengan del namun pop() juga mengembalikan value index yang dihapus. Apabila kita tidak mengisi index dalam metode pop() maka elemen terakhir yang akan dihilangkan dari list.

# In[36]:


n_list = [10,20,30]
print(n_list) # print seluruh items

n = n_list.pop()
print('n = ',n)
print('n_list =',n_list)


# ## remove ()
# remove() menghapus nilai tertentu berdasarkan nilai itu sendiri tanpa mengetahui indeksnya.

# In[37]:


n_list = [11,22,33,44,55,66]
print(n_list) # print seluruh items

n = n_list.remove(44)
print(n_list)


# ## LIST SLICING
# - Slicing berarti mengiri bagian tertentu dalam sebuah list 
# - gunakan sintaks list_name[start:end] untuk menyatakan section yang kita mau pisahkan

# ![slicing.jpg](attachment:slicing.jpg)

# In[41]:


a_list = [10,20,30,40,50,60,70,80]
a_list[1:5] #mengambil dari index ke 1 sampai 5 (index dimulai dari 0 jadi tidak dihitung)


# In[42]:


a_list[0:5] #mengambil dari index ke 0 sampai 5 


# In[43]:


a_list[1:] #mengambil dari index ke 1 sampai selesai


# In[46]:


a_list[:5]#mengambil dari awal hingga sampai 5 


# In[48]:


a_list[:]#mengambil semuanya


# ### Kombinasi slicing yang sesuai dengan kebutuhan  

# ![slicing_2.jpg](attachment:slicing_2.jpg)

# In[49]:


a = [1,2,3,4,5]
print (a[:2])


# ## LIST IN OPERATOR

# Operator in mengembalikan True atau False. Setelah memeriksa untuk melihat apakah suatu elemen berada pada sebuah list tertentu, jika benar _True_ jika salah _False_. Operator not in (kebalikannya). sehingga operator ini cocok untuk mem <u>**VALIDASI**</u> apakah data yang kita inginkan ada dalam list tersebut. 

# In[54]:


#contoh 
a_list = [10,20,30,40]
10 in a_list #sebelum melanjutkan dengan metode a_list.remove(10), kita dapat memeriksa item 10 ada dengan operasi "in" dan apakah 
            #itu mengembalikan true, sehingga metode remove()tidak akan menghasilkan error


# In[55]:


50 in a_list


# In[56]:


10 not in a_list


# In[57]:


50 not in a_list


# In[64]:


for n in a_list:
    print(n, end='')


# ## TUPLE 

# - Adalah sebuah Immutable List  tuple tidak dapat diubah dengan cara apapun
# - Tuple mirip dengan list hanya tuple menggunakan kurung () 
# - Setelah dibuat, tuple kita tidak bisa menambahkan elemen atau menghapus 

# - Karena tidak dapat diubah, senhingga memiliki keunggulan sebagai berikut 
#  1. Tuple lebih cepat diproses dibandingkan dengan list
#  2. Tuple dapat melindungi dari perubahan data yang tidak kita  inginkan. 

# In[68]:


colors = ("red", "green", "blue") #string
colors


# In[69]:


numbers = (1,2,3,4,5) #integers
numbers


# In[71]:


#mencoba menambahkan 
t1 = (1,2,3,4,5)
t1[0] = 100


# ## SEQUENCE DATA TYPES- INTRO
# 

# ## DIGUNAKAN UNTUK MENGAMBIL DATA SECARA BERURUTAN SEPERTI (SQL)

# Sequence adalah kumpulan terurut dari tipe data yang serupa atau bisa juga berbeda. Sequence memungkinkan untuk meyimpan beberapa nilai secara terorganisir dan efisien. 
# 
# ## Tipe data Sequence 
# 
# - List
# - Tuple
# - Range dan 
# - String
# 
# Objek dari tipe data sequence disebut objek sequence dan setiap nilai dalam objek sequence disebut elemen

# ##  SEQUENCE DATA TYPES - ITERATOR 
#  

# In[74]:


#**list**
list1 = [11,22,33,44] *2
print (list1)


# In[76]:


#tupple
tup = (1,2,3)
print (tup*2)


# In[78]:


#String 
str = 'hello'
print (str*2)


# In[80]:


#Range


# Sama seperti operator +, kita juga tidak bisa menggunakan operator * untuk tipe data range dan kita bisa menggunakan operator * untuk tipe data range dengan mengubah tipe data tersebut ke dalam list atau tuple terlebih dahulu.

# In[81]:


range (10)*3


# In[84]:


ran = list(range(5))*3 #data harus diubah dalam bentuk list terlebih dahulu
print (ran)


# In[86]:


ran = tuple(range(5))*3 #data harus diubah dalam bentuk list terlebih dahulu
print (ran)


# In[88]:


a = [1,2,3,4]
b = a*2 
print (b)


# ##  SEQUENCE DATA TYPES - Count Method

# Method count() mengembalikan jumlah elemen dalam objek sequence. Metod ini bisa digunakan untuk mencari elemen yang terdapat di dalam objek sequence dan mengetahui berapa banyak elemen dalam objek sequence tersebut. 

# In[4]:


list1 =[11,11,11,22,33,44]
print(list1.count(11))#mencari jumlah nilai 11 dalam list


# Dapat juga digunakan untuk tipe data tuple, range, dan string : 

# In[8]:


#Tuple
tup1 = (11,11,11,22,33,44)
print(tup1.count(11))#mencari total angka 11 dalam tuple 


# In[9]:


#String 
str1 = 'hello world'
print (str1.count('l')) #mencari jumlah huruf l dalam string


# In[10]:


#contoh penggunaan dan aplikasi metode count() kode : 
ran = range(0,5,1)
print(len(ran))
print (ran.count(2))


# ran memiliki lima elemen 0, 1, 2, 3, 4. Banyaknya elemen yang dicetak dengan menggunakan fungsi len adalah 5.
# Pada sisi lain, ketika menggunakan metode count() untuk melihat berapa banyak angka 2 dalam variabel yang dijalankan, itu akan mencetak 1 karena hanya ada satu angka 2 dari range 0 hingga 5.

# ##  SEQUENCE DATA TYPES - Linking

# - Menggabungkan tipe data yang sama biasa menggunakan operator+ 
# - Namun tipe data range tidak bisa digabungkan dengan operator +, ubah dulu dalam list untuk bisa menggunakan oeprator + 

# In[11]:


#list : 
list1 = [11,22,33,44]
list2 = [55,66]
print(list1)
print(list1+list2)


# In[20]:


#tuple : 
tup1 = [1,2,3,]
tup2 = [4,5,6]
print(tup1+tup2)


# In[17]:


#string: 
str1 = 'Hello'
str2 = 'World'
print (str1 + str2)


# In[5]:


#untuk tipe data range berbeda lagi,

print(list(range(10)) + list(range(10,20)))
print(tuple(range(10)) + tuple(range(10,20)))


# In[4]:


print(list(range(10)) + list(range(10,20)))
print(tuple(range(10)) + tuple(range(10,20)))


# In[6]:


range (10)


# ## SEQUENCE DATA TYPES - OPERATORS

# Dalam tipe data sequence kita dapat menggunakan operator in dan not in untuk mencari apakah suatu elemen tertentu terdapat di dalam struktur data seperti string, tuple atau list.
# 
# - in operator akan mengembalikan nilai True jika elemen tertentu ada dan False jika tidak.
# 
# - not in operator akan mengembalikan nilai False jika elemen tertentu ada dan True jika tidak.
# 
# Berikut beberapa contoh pengaplikasian operator in dan not in dalam tipe data sequence

# In[ ]:


list = [10]


# In[9]:


list1 = [10,20,30,40]
print(10 in list1)
print(10 not in list1)


# In[10]:


tup = (1,2,3,4)
print(3 in tup)


# In[11]:


print('a' in 'abcd')


# In[12]:


print(11 in range(10))


# In[13]:


list1 = [5,6,7,8]
print(10 in list1)

