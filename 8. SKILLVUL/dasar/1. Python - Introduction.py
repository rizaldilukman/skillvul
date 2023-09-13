#!/usr/bin/env python
# coding: utf-8

# # INTRODUCTION

# ## 1. BAHASA PEMROGRAMAN PYTHON

# 1. Merupakan bahasa pemrograman tingkat tinggi dan bahasa yang populer didunia. 

# 2. Banyak digunakan untuk berbagai aplikasi yaitu : Artificial Inteligence, IoT, Data Science, Web Development Program sampai ke otomasi

# 3. Python digunakan dan diintrepretasikan sama dengan bahasa manusia. Untuk digunakan secara luas dan berbagai bidang, beberapa tools dan library seperti, Pandas, NumPy, SciPy, Matplotlib, dan TensorFlow serta Keras.

# ##  Contoh Penggunaan library : 

# a. Tensor Flow Digunakan untuk aliran data dan pemrograman  differensial berfokus pada deep neural network untuk machine learning.

# b. Pandas digunakan untuk manipulasi dan analisis data, terutama untuk tabel numerik dan operasi deret waktu.

# ## 2. INSTALASI PYTHON

# Kunjungi website python di web resminya download versi terbaru yaitu python 3 

# Lakukan instalasi seperti biasa, cheklist pilihan Add to Python to Path 

# Setelah selesai, buka Run dan cari cmd untuk membuka command prompt. Masukkan perintah python --version. Lalu ketik python jika tampilan seperti dibawah ini, artinya python sudah bisa digunakan.Dapat digunakan pada jupyter notebook dan atau VS Code untuk menulis baris program

# ![python_1.jpg](attachment:python_1.jpg)

# ## 3. FUNGSI DALAM PYTHON 
# 1. FUNGSI PRINT : Digunakan untuk menampilkan hasil dalam (). Jika dalam berbentuk kalimat atau karakter kurung tersebut harus dilengkapi dengan tanda kutip ("")

# Contohnya seperti dibawah ini : 

# a. Fungsi untuk String (Kalimat)

# In[2]:


print ('hello world')


# b. Fungsi untuk memasukkan numerik tanpa tanda kutip ("")

# In[3]:


print (10)


# Dapat juga menggabungkan keduanya 

# In[4]:


print ('Hello', 10)


# Bisa juga ditambah dengan karakter dan nilainya 

# In[5]:


print('Hello' * 3) # akan menduplicate string Hello sebanyak 3 kali
print(10 * 20) # akan mengalikan bilangan tersebut

print('Hello' + 'World') # akan menggabungkan kedua string tersebut
print(10 + 20) # akan menambahkan kedua bilangan tersebut


# ## 4. PYTHON SYNTAX - COMMENT

# Komentar dalam pemrograman adalah bagian yang cukup penting untuk memberi maksud dan tujuan dari program tersebut. Komentar adalah bagian dari program yang tidak akan dieksekusi oleh sistem. terdapat dua tipe komentar yaitu : 
# 1. Single line comment gunakan # 
# 2. Multiple line comment  gunakan ("" "")

# Contoh : 

# In[6]:


""" Program ini bertujuan untuk menampilkan angka 5 dengan menggunakan fungsi print """


# In[7]:


print(5) #Menampilkan angka 5


# ## 5. ERROR PADA PYTHON 

# Terdapat 2 error pada python yaitu : 
# 
# ### 1. Syntax Error : 
# 
# a. Bahasa Pemrograman digunakan dibawah aturan konvensi yang 
#    ketat. Menulis kode menyimpang dari tata aturan. 
# 
# b. Untuk mencegahnya, kita harus mempelajari dan mempraktikan 
#    tata bahasa python sesuai aturan. 
# 
# c. Untuk mencetak string 'hallo'. digunakan kedua tanda kutip.
# 
# ### 2. Runtime Error :
# 
# a. Berbeda dengan kesalahan sintaks, kode yang benar secara 
#    tata bahasa masih dapat menyebabkan kesalaha selama 
#    eksekusi. 
# 
# b. Untuk mencegahnya, harus dipertimbangkan kemungkinan 
#    memasukkan data yang salah. 
# 
# c. Dalam kode dibawah ini, memasukkan kedua string dua dan  
#    bukan bilangan bulat 2 sehingga kesalahan terjadi.   

# In[8]:


num = int(input('Input an integer'))


# In[9]:


100/20


# In[10]:


100 **2


# In[11]:


100 * 2


# In[12]:


100 ** 2


# In[ ]:





# In[13]:


print( 30 * 2 + 10 - (21  // 5) )


# In[14]:


21//5


# In[15]:


a = 10
a += 200
a -= 100
a = a * 2

print(a)


# In[16]:


a = 200
b = 300
d = 0

e = b // a
c = e ** b * d
print(c)


# In[17]:


age = 18 # diberikan kondisi bahwa age = 18

if age < 20: # result dari age < 20 adalah True
    print('youth discount')


# In[18]:


age = 20 


# In[19]:


if age < 25:
    print('older discount')


# In[20]:


a = 6
b = 2


# In[21]:


if a/b ==3:
    print("6 dibagi 3 adalah 2")


# In[22]:


age = 18
if age < 20:
    print('youth discount')
print('Welcome')


# In[23]:


print ("hello")


# In[24]:


age = 21
if age < 20:
    print('youth discount')
print('Welcome')


# In[25]:


age = 12
if age < 15:
    print('youth discount')
    print('Welcome')
    print('Hai')


# In[26]:


angka = 10

if angka > 5:
    print("Angka lebih besar dari 5")
else:
    print("Angka tidak lebih besar dari 5")


# In[27]:


for i in range(5):
 print("Iterasi", i)


# In[28]:


num = 7
if num % 2 == 0:
    print('Nomor genap')
if num % 3 == 0:
    pass


# In[29]:


def func():
    pass

func()


# In[30]:


score = 95
statement1 = ('good')
statement2 = ('bad')
statement  = ('fair')

if score >= 90 :
    statement1
else :
    if score >= 80:
        statement2
    else:
        statement
print (statement)


# In[31]:


angka = 8

if angka > 10:
    print("Angka lebih besar dari 10")
elif angka < 10:
    print("Angka lebih kecil dari 10")
else:
    print("Angka sama dengan 10")


# In[ ]:




