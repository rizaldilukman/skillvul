#!/usr/bin/env python
# coding: utf-8

# ## NESTED FUNCTION

# Dalam Bahasa pemrograman, kita dapat mendefinisikan suatu function di dalam function, dan kita dapat meneruskan suatu function sebagai nilai balik dari suatu function. 
# Dengan hal ini, kita dapat secara struktural menulis kode yang seharusnya ditulis dengan control statement dalam bahasa lain. kita juga dapat menyederhanakan kode dengan lebih sedikit dengan control statement. 

# In[4]:


def decorate (style = 'italic'):
    def italic(s):
        return '<i>' + s +'<i>'
    def bold (s):
        return '<b>' + s + '<b>'
    if style  == 'italic':
        return italic
    else:
        return bold


# In[5]:


dec = decorate()
print(dec('hello'))
dec2 = decorate('bold')
print(dec2('hello'))


# In[11]:


type (dec2)


# Konsep function di dalam suatu function disebut nested function. Berbeda dengan function yang terletak di luar, ia dapat dengan bebas membaca variabel dari function induknya atau outer function. Agar lebih jelas, perhatikan kode di bawah ini:

# In[12]:


def another_func():
  print('hello')
  
def outer_func():
  return another_func()
  
outer_func()


# ## Non-local Variable - Local Variable vs Global Variable

# Perbedaan mendasar local variable dan global variable dalam bahasa pemrograman Python local variable adalah variabel yang digunakan dalam sebuah fungsi atau blok kode tertentu, sementara global variable adalah variabel yang digunakan di seluruh kode.

# ![non%20local%20variable.jpg](attachment:non%20local%20variable.jpg)

# ## Global Keyword 

# Dari kondisi di atas, bila berada dalam function print_counter kita tidak bisa mengakses dan merubah variabel yang ada di luar dari function tersebut. Namun dengan bantuan global keyword kita bisa melakukan hal tersebut yaitu menjadikan local variable menjadi global variable. Berikut cara penggunaan global keyword di dalam kode:

# In[16]:


def print_counter():
    global counter
    counter = 200 
    print ('counter didalam fungsi=',counter)#nilai counter dalam fungsi

counter = 100
print_counter()
print('counter diluar fungsi =', counter)#niai counter diluar fungsi


# Dengan bantuan deklarasi global seperti di atas, nilai global variable berubah menjadi 200 saat kita menetapkan counter = 200 di dalam function print_counter karena print_counter menginisialisasi variabel global counter.

# ## Closure - Concept 

# Pada Python kita dapat memuat function di dalam function yang biasa disebut nested function. Di sini kita dapat mengatakan bahwa nested function ‘was closured.’ Jika sebuah fungsi dikatakan closured, variabel di dalam body fungsi asli (outer function) tidak hilang dari memori.

# In[19]:


def closure_calc():
    a=2
    def mult(x):
        return a*x
    return mult
c = closure_calc()
print(c(1),c(2), c(3))


# Pada contoh di atas kita membuat function mult di dalam function closure_calc. mult adalah sebuah nested function.
# 
# Di dalam function mult, kita mengakses variabel a yang merupakan non local scope variable. Jadi jika kita lihat didalam function mult, disana terjadi beberapa proses yaitu:
# 
#     Function mult itu sendiri
#     non local scope variable dengan nilai 2 dari a.
# 
# 2 proses di atas disebut Closure.
# 
# Dan dengan membuat fungsi mult closured, kita juga tidak dapat mengakses fungsi tersebut dengan mudah dan hanya bisa melalui outer function closure_calc().

# ![closure_mult.jpg](attachment:closure_mult.jpg)

# Purposes
# 
# Dalam pemrograman tradisional, kita biasanya mendeklarasikan variabel sebagai global variable. Sebenarnya, pemrograman akan menjadi mudah jika kita menggunakan global variable. Namun, terlalu banyak global variable akan menyebabkan efek samping, yaitu menciptakan kesulitan untuk debugging. Sehingga closure dibutuhkan untuk mengatasi masalah tersebut.

# - Untuk membaut fungsi closure, tentukan variable untuk closure dan function bpdy yang diselubungi oleh function lain nantinya akan menjadi outer funtion

# In[29]:


a = 10
def addition(z):
    return a + z


# - Kemudian tentukan outer function yang mengurung nestd function yang telah kita buat sebelumnya, dan tipe pengembalian dari outer function ini menjadi closure

# In[30]:


def fungsi_luar(x):
    a=10
    def addition(z):
        return a + z
    return addition(x)


# Ini dapat mengurangi frekuensi global variable dan menyembunyikan cara kerja bagian dalam function dari luar

# Penggunaan closure digunakan sebagian besar untuk hal-hal berikut:
# 
#    - Membatasi penggunaaan global variables
#    - Menyembunyikan data (data hiding)
# 
# Dalam hal efisiensi operasi memori, closure tidaklah efisien. Namun bisa lebih efektif karena mengurangi penggunaan global variable. Jika kita ingin menyembunyikan data, deklarasikan closure sebagai fungsi pelindung local variable.
