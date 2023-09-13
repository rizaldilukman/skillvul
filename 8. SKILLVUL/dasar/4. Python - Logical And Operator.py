#!/usr/bin/env python
# coding: utf-8

# ## LOGICAL AND COMPARISON OPERATOR

# ## 1. LOGICAL 

# 1. Berfungsi untuk memeriksa hubungan ukuran dua operan yang sebanding, seperti angka dan string, bisa lebih besar, kurang dari. 
# 2. Hasil ini dikembalikan menjadi nilai True atau false (boolean)

# In[1]:


print('Result of 10 > 5: ', 10 > 5)
print('Result of 5 < 1: ', 5 < 1)
print('Result of 5 == 5', 5 == 5)
print('Result of 5 != 5', 5 != 5)
print("Result of 'a' > 'b': ", 'a' > 'b')


# ![logical_and_comparison.jpg](attachment:logical_and_comparison.jpg)

# ### Penerapan Comparison Operators
# Digabungkan dengan arithmathic operation 
# 

# In[2]:


n = int(input("Masukkan sebuah integer: "))
print('Apakah integer tersebut genap?', n % 2 == 0)


# ## String Comparison 

# In[3]:


print('aaa' == 'aaa')
print('aaa'== 'bbb')
print('aaa' != 'aaa')
print('aaa' != 'bbb')


# ## 2. COMPARISON OPERATOR Is & In

# ## Comparison Operator Is 
# Operator is menentukan apakah kedua objek sama. Perbedaan dengan == adalah jika  == memeriksa nilai dari kedua objek.

# In[ ]:


a = 1
b = 1.0 
print (a==b)
print (a is b)


# ## Comparison Operator In 

# Operator in memeriksa untuk melihat apakah kedua string cocok sebagian. Operator in sering digunakan untuk menentukan apakah ada karakter yang cocok di dalam string, apabila terdapat kecocokan maka akan mengembalikan nilai True dan jika tidak akan mengembalikan nilai False.

# In[5]:


print('aaa' in 'aaa-bbb-ccc')
print('bbb' in 'aaa-bbb-ccc')
print('ddd' in 'aaa-bbb-ccc')


# ## 3. LOGICAL OPERATORS

# ![LOGICAL_OPERATORS_OPERATOR.jpg](attachment:LOGICAL_OPERATORS_OPERATOR.jpg)

# Terdapat 3 logical operator yang sering digunakan pada Python yaitu and, or, dan not. Contoh penggunaan logical operator dalam kode:
#     
# 1. Operator and mengharuskan semua operan bernilai True agar bisa mengembalikan nilai True dan selain dari kondisi tersebut, operator and akan mengembalikan nilai False.
#     
# 2. Berbeda dengan operator or, jika salah satu operan setidaknya bernilai True maka operator or akan mengembalikan nilai True sementara jika semua operan bernilai False maka operator or akan mengembalikan nilai False
#     
# 3. Operator not akan menghasilkan negasi dari nilai operan, jika operan bernilai True maka jika menggunakan operator not, nilainya akan berubah menjadi False.

# In[7]:


x = True
y = False
print(x and y)
print(x or y)
print(not x)
print(not y)

