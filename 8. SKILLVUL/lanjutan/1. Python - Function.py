#!/usr/bin/env python
# coding: utf-8

# ## BASIC STRUCTURE

# Function adalah sekumpulan blok kode yang melakukan operasi tertentu dalam suatu program. Software yang digunakan kemungkinan besar dibuat dengan menggabungkan berbagai function dan module. 

# ![function_1.jpg](attachment:function_1.jpg)

# **Manfaat dari Function**

# Beberapa keuntugan ketika kita menggunakan function 

# 1. Pemrograman menjadi lebih terstruktur karena suatu program dapat dibagi menjadi beberapa bagian. 
# 2. Kita dapat menggunakan kemabali function yang dibuat pada bagian program lain 
# 3. Code readability kode dapat dengan mudah dibaca dan dipahami oleh kita dan rekan 
# 4. Bahkan ketika memodifikasi sebuah program, perawatannya mudah, karena hanya beberapa function yang perlu dimodifikasi

# Berikut adalah contoh membuat function dan memanggilnya untuk dieksekusi oleh program.

# In[4]:


def print_star(): #Deklarasi fungsi untuk menampilkan tanda bintang
    print('*************')
print_star() #Memanggil fungsi untuk menampilkan tanda bintang


# Baris ke-1 : Dalam def print_star() = sebuah function yang didefinisikan menggunakan kata kunci def. 
# tanda (:) . Setelah tanda titik dua : tersebut adalah blok kode

# Baris ke-2 : Pernyataan yang membentuk _function_ dimasukkan. Pernyataan yang membentuk _function_ harus menjorok (terindentansi). Potongan ini disebut blok dan _function_ akan mengeksekusi blok ini. 

# Baris ke-4 adalah pernyataan yang memanggil _function_ dengan memanggil langsung nama function tersebut, **print_star()** program akan mengeksekusinya

# In[9]:


def print_star():
  print("***********************")
print_star() #memanggil functionprint_star (1)
print_star() #memanggil functionprint_star (2)
print_star() #memanggil functionprint_star (3)
print_star() #memanggil functionprint_star (4)


# ## Function - Arguments and Parameters 

# Dalam Python, terdapat dua keywords yaitu argumen dan parameter. Kedua ini tidak bisa dipisahkan. Jika sebuah **_function_** memiliki parameter, saat memanggil **_function_** wajib mengirimkan nilai atau data berupa argumen. 

# - Argumen : Argumen mengacu pada nilai atau data yang ingin di proses ketika suatu function dipanggil 
# - Parameter : adalah variabel yang didefinisikan pada sebuah function. Parameter bersifat data yang dinamis butuh diproses oleh sebuah function. 

# ![function_2.jpg](attachment:function_2.jpg)

# kode berikut mengkalkulasi total integer dari 1 hingga 10 dan mengembalikan hasilnya 

# ![function_3.jpg](attachment:function_3.jpg)

# ## Function - Arbitrary Arguments

# Saat kita menggunakan _function_ dalam sebuah program, kadang ada kasus di mana jumlah argumen belum bisa atau tidak ditentukan. Kasus ini disebut Arbitrary Argumen. Untuk emnentukannya digunakan * didepan parameter. Variabel dalam fungsi yang menerima arbitrary argumen adalah arbitrary parameter. 
# 
# Arbitrary Parameter dapat digunakan dalam pernyataaan for -in, seperti dalam tuple dan list. 

# In[2]:


def greet(*names): #mendefinisikan greet yang isinya names (names merupakan arbitrary argumen dari function greet)
    for name in names: #isi names adalah name
        print('Hello', name, '!') #cetak hello, name yang sudah disusun, tambah tanda !
greet('A','B','C') #3 argumen
greet('James','Thomas') #2 argumen


# ## Function - Default Parameters (kalo di excel if error)

# Jika sebuah function memiliki sebuah parameter yang harus dipenuhi, tapi kita tidak memberikan argumen dalam function tersebut. maka muncul error. Untuk mengatasinya kita butuh _default parameters_ 

# In[5]:


def print_star(n): #dibutuhkan 1 argument
    for_in range(n)
        print ('********')
print_star() # muncul error karena tidak menyertakan argumen


# In[10]:


def print_star(n=1): #parameter n mempunyai default value = 1
    for _ in range(n):
        print ('********')
print_star() # Tetap tereksekusi walau tidak menyertakan argumen


# ## Function - Keyword Parameter 

# Dalam Python, metode default untuk menyampaikan argument disebut ***positional argument method***. Sehingga urutan argumen diteruskan dalam function  sama dengan yang diterima dalam functuon tersebut. Berikut gambaran dari positional argument methode.

# 

# Hal ini cukup menyulitkan apalagi banyak parameter dalam sebuah function dan tidak hapal seluruh urutan tersebut. Sehingga menggunakan ***Keyword parameter** adalah jawabannya. Saat memanggil function, daripada hanya meneruskan nilai argumen, kita dapat meneruskan argumen dengan menentukan nama argumen yang disebut sebagai keyword parameters.

# In[14]:


def get_root(a,b,c):
        r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        return r1,r2
result1, result2 = get_root(a=1, c=-8, b=2)
print('Hasil akar- akarnya adalah',result1, 'atau', result2)


# In[16]:


def test(a=2, b=3):
    print (a,b)
test(4)


# ## Function_Return Statement 

# Secara umum, kita dapat mengasumsikan bahwa bagian dalam suatu fungsi adalah sebuah black box, yang berarti bagian dalam suatu fungsi memiliki kode tertentu dan bagian tersebut dapat melakukan tugas yang diberikan atau input value serta mengembalikan hasil. Dan untuk mengembalikan hasil tersebut, kita dapat menggunakan keyword return atau return statement.

# In[19]:


def get_sum(a,b):# fungsi yang akan mengembalikan total dari 2 angka
    result =a+b
    return result # mengembalikan hasil penjumlahan menggunakan return
n1 = get_sum(10,20)
print("hasil penjumlahan dari 10 dan 20 adalah",n1)


# Selain mengembalikan sebuah result, return statement juga bisa mengembalikan multiple result dalam bentuk sebuah tuple seperti contoh sebelumnya.

# In[22]:


def get_root(a,b,c):
    r1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    r2 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    return r1,r2
result1, result2 = get_root(a=1, c=-8, b=2)
print('Hasil akar - akarnya adalah',result1,'atau',result2)


# Dimana dapat dilihat di contoh kode diatas, bahwa fungsi get_root() mengembalikan dua value r1 dan r2. Dan kita bisa mengakses 2 value tersebut dengan result1 dan result2 seperti kode dibawah ini:
# result1,result2 

# = get_root(a=1,c=-8,b=2)

# In[23]:


def test123(a,b):
    if a>b:
        return a + b,"OK!"
    else:
        return a - b,"Not Ok"
print (test123(1,2))        


# 
