#!/usr/bin/env python
# coding: utf-8

# # VARIABEL

# ## 1. VARIABEL DAN INPUT

# Variabel adalah konsep kunci dalam pemrograman. Digunakan untuk menyimpan nilai tertentu dalam komputer. Python tidak memerlukan deklarasi tipe data pada variabel. contoh dibawah ini

# In[2]:


berat = 77.5 #variabel dengan nama berat berisi nilai 77.5
manusia = ('David',77.5) #variabel dengan nama manusia disimpan dalam bentuk tuples(data bisa dimasukkan dalam semua tipe tapi tidak bisa diganti)
print (berat)
print (manusia)


# tanda =  disebut assignment operator yang berarti menyimpan nilai sebelah kanan dengan nama variabel di sebelah kiri

# ## 2. DEKLARASI VARIABEL

# ####  IDENTIFIER
# Merupakan nama yang diberikan untuk sebuah entitas seperti class, function, variabel dan yang lain - lain. 

# Aturan - aturan dalam pembuatan variabel
# 1. Identifier dapa berupa kombinasi huruf dan atau angka dan garis bawah, tetapi tidak terdiri dari simbol khusus apapun
# 2. Identifier tidak dapat dimulai dengan angka
# 3. Identifier tidak boleh berisi spasi atau tab
# 4. Identifier adalah case sensitive
# 5. Identifier tidak dapat menggunakan salah satu dari *Python Reseerved Words* dibawah ini

# ![kata_kunci_bawaan_python.jpg](attachment:kata_kunci_bawaan_python.jpg)

# ## 3. VARIABEL ASSIGNMENT 

# ![variabel_assignment.jpg](attachment:variabel_assignment.jpg)

# ## Python Simultaneous Assignment 

# Dimungkkinkan untuk menetapkan beberapa variabel ke nilai dalam satu baris secara bersamaan. Ini disebut simultaneous assignment. 

# In[3]:


x,y = 100, 200
result = x + y
print (result)


# ## Python Multiple Assignment 
# Dimungkinkna untuk menetapkan nilai sekaligus dalam satu variabel 

# In[5]:


num1 = num2 = num3 = 200 
print (num1,num2,num3)


# ## 4. COMPUND ASSIGNMENT OPERATORS

# 1. Terdiri atas binary operator dan simpel assignment operator.
# 2. Melakukan operasi binary pada kedua operan dan menyimpan hasil operasi tersebut di operan kiri.
# 3. Dapat Mengunakan aritmatika jika tidak terbiasa
# 4. Akan menjadi masalah jika tidak terbiasa dengan compund assignment operators karena tidak bisa membaca kode orang lain

# ![compound_assignment.jpg](attachment:compound_assignment.jpg)

# In[12]:


#contoh dari penggunaan
num = 200
m = 2
num += 100
print (num)

num -=100
print (num)

num *=20
print (num)

num /=2
print (num)

num %=2
print (num)


# ## 5. OPERATOR ARITMATIKA 

# Operator Aritmatika yang digunakan pada python adalah dibawah ini 

# ![operator_aritmatika.jpg](attachment:operator_aritmatika.jpg)

# In[15]:


berat =float(input("Masukkan berat anda ke dalam kg: "))
tinggi =float(input("Masukkan berat anda ke dalam m: "))

bmi = (berat/(tinggi**2))
print("BMI ANDA=",bmi)


# ## 6. INPUT FUNCTION
# sebuah fungsi dari python digunakan untuk mendapatkan input dari data user.

# In[16]:


name = input("Enter Name: ")
print("Hello", name)
print("Welcome to the world python programming.")


# ### Input to Integers 
# 
# Fungsi input() dapat digunakan untuk memasukkan bilangan bulat. Namun, fungsi input() selalu mengembalikan input dalam bentuk string. Contoh output yang dihasilkan adalah string "300".
# 
# 
# Untuk mengubah string "300" menjadi bilangan bulat 300, nilai kembalian dari fungsi input() harus dikonversikan menggunakan fungsi bawaan Python lainnya yaitu int(). Fungsi int() bertujuan untuk mengubah string menjadi integer.
# 

# In[18]:


x = int(input("Masukkan integer pertama:" ))
y = int(input("Masukkan integer kedua:" ))
s = x + y
print("Total dari",x,"dan",y,"adalah",s)


# ### Input errors

# !! Jika Anda memasukkan karakter atau string seperti "hundred" alih-alih string "300" sebagai berikut, fungsi int() tidak dapat mengubah "hundred" menjadi bilangan bulat dan akan menghasilkan Value Error.

# In[19]:


x = int(input("Masukkan integer pertama:" ))
y = int(input("Masukkan integer kedua:" ))
s = x + y
print("Total dari",x,"dan",y,"adalah",s)


# In[ ]:




