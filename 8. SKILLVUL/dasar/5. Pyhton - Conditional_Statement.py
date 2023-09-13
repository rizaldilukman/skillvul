#!/usr/bin/env python
# coding: utf-8

# # SELECTION STRUCTURE 

# Dalam Bahasa python, dikenal beberapa control structures, terdapat tiga control structure dalam bahasa pemrograman yaitu :
# 1. Sequence = Struktur dimana perintah dieksekusi secara berurutan.
# 2. Selection = Struktur dimana salah satu dari beberapa instruksi dipilih dan dieksekusi.
# 3. Iteration = Struktur dimana perintah yang sama dieksekusi berulang kali. 

# ![selection_structure.jpg](attachment:selection_structure.jpg)

# Pada beberapa tahap program, ada lebih dari satu jalur yang harus dilalui, diantaranya kita harus memilih satu.
# Jika tidak ada struktur seleksi, program akan selalu mengulangi tindakan yang sama dan jika program selalu melakukan hal yang sama, itu akan selalu mencapai kesimpulan yang tidak akan pernah berubah.

# ## IF STATEMENT SYNTAX

# Penggunaan if syntax digunakan jika menggunakan beberapa fungsi 

# ![IF_.jpg](attachment:IF_.jpg)

# In[71]:


age = 18 # diberikan kondisi bahwa age = 18 
if age <20: #hasil dari age kurang dari 20 adalah true
    print('youth discount')


# Ketika nilai lebih dari 20, maka tidak akan ada jawaban karena syarat dari fungsi tersebut adalah 20 contohnya adalah seperti dibawah ini.

# In[72]:


age = 23
if age < 20:
    print('youth discount')


# In[ ]:





# # Indentation 

# Python adalah bahasa pemrograman dimana indentation adalah hal yang penting. Tergantung pada indentation, kode yang sama menghasilkan hasil yang berbeda. Hal ini sangat berbeda dengan bahasa pemrograman seperti C++ atau Java yang tidak mementingkan indentation karena mereka memiliki separator antara bagian program yang satu dengan yang lain menggunakan separator ; dimana Python tidak memiliki hal tersebut.

# In[73]:


# indentation kondisi if adalah true 
age = 18 
if age < 20:
    print('youth discount')
print('Welcome')


# In[74]:


#indentation dimaan kondisi if adalah False 
age = 24
if age < 20:
    print('youth discount')
print('Welcome')


# In[75]:


#indentation dimaan kondisi if adalah False dan diberikan indentation
age = 24
if age < 20:
    print('age', age)
    print('youth welcome')
    print('youth discount')


# Pada contoh kode diatas, kode nomor 2 dan 4, kondisi if statement pada kedua contoh diatas adalah False, namun pada kode nomor 4, tidak ada output yang di tampilkan pada program karena print('youth welcome'), print('age',age), dan print('youth discount') diberikan indentation, dimana pada kode nomor 2, 'Welcome' muncul di hasil program karena tidak diberikan indentation.

# ## Pass Keyword

# adalah sebuah built in dari python yang ditemui dalam program. Pass statetement adalah null statement. Perbedaan pass statement dan komentar adalah intrepreter tidak akan mengeksekusi kode yang merupakan sebuah komentar sementara intrepeter akan mengeksekusi pass namun tidak akan muncul pada output karena pass merupakan null statement. 
# 
# Pass digunakan ketika ingin menulis blok seperti conditional, function atau looping pada lain waktu karena eksekusi yang tepat dari blok kode tersebut belum di temukan

# In[76]:


num = 2
if num % 2 == 0:
    print ('nomor genap')
if num % 3 == 0:
    pass


# In[77]:


num = 11
if num % 2 == 0:
    print ('nomor genap')
if num % 3 == 0:
    pass


# Pass Statement Python juga dapat digunakan untuk mendefinisikan nama dari sebuah fungsi dan mengimplementasikan fungsionalitasnya nanti. Kita akan belajar tentang fungsi pada lesson berikutnya.Fungsi func di bawah ini hanya mendefinisikan namanya dan bermaksud untuk mengimplementasikan fungsinya nanti.

# In[78]:


def func():
    pass

func()


# ## ELIF STATEMENT

# Pertimbangkan sebuah program yang menerima bilangan bulat dari pengguna dan mencetak "Ini positif", "Ini 0", dan "Ini negatif".
# Jika True dikembalikan dari pernyataan if pertama, baris kode dieksekusi dan keluar dari pernyataan kondisional.
# Jika False, keputusan mungkin harus dibuat sesuai dengan ekspresi kondisional kedua.
# Program dengan struktur seperti itu dapat dibangun menggunakan if-elif-else.
# elif adalah singkatan dari else if.

# ![elif_1.jpg](attachment:elif_1.jpg)

# Penggunaan elif digunakan untuk mempersingkat baris dan membuatnya lebih mudah dibaca dibanding harus menulis else dan if secara terpisah. Kedua kondisi menghasilkan hasil yang sama namun elif lebih sederhana dan mengurangi jumlah kode. 

# ![if_else.jpg](attachment:if_else.jpg)

# In[79]:


score = 85 #score masuk 85
if score >= 90: 
    print("baik") #(jika score masuk 90 maka hasilnya baik)
else:
    if score >= 80:
        print("kurang") #(jika score masuk 80 maka hasilnya kurang)


# In[80]:


score =  90
if score >= 90 : #(jika score masuk 90 maka hasilnya baik)
    print ('baik')
elif score >= 80 :
    print ('kurang')#(jika score masuk 80 maka hasilnya kurang)


# # sistemnya sama dengan if majemuk di excel, 

# In[81]:


#contoh lainnya


a = "ABC"
b = "abc"
c = "ABC"
d = "CBA"

if a == b: # disamain antara a dan b
    print("123") #jika sama maka cetak 123
elif a == c: #disamain antara a dan c
    print("456") # jika sama, maka cetak 456

if a == b:
    print("1234")
else:
    print("789")


# ## IF ELSE STATEMENT 
# Jika kondisinya benar maka jalankan jika kondisinya tidak benar, maka jalankan yang lain. 

# In[82]:


hour = 10
if hour < 12:
    print('it is morning')
else: 
    print('it is afternoon')


# ![if%20else.jpg](attachment:if%20else.jpg)

# Berikut perbandingan flowchart antara if else dan if if statement

# ![if_else_2.jpg](attachment:if_else_2.jpg)

# ##  NESTED CONDITIONAL STATEMENT

# Pernyataan if-else ganda dapat terjadi dalam situasi di mana kondisi spesifik memerlukan verifikasi tambahan setelah True atau False dikembalikan untuk kondisi pertama. Sehingga dalam kode diatas, langkah validasi pertama adalah mengecek apakah angka tersebut adalah angka negatif <0 atau positif >0 dan kemudian validasi kedua adalah jika angka tersebut adalah positif, apakah nomor itu ganjil atau genap, sehingga diperlukan if dan else yang kedua.

# In[83]:


num = -100
if num < 0:
    print(num, 'adalah bilangan negatif. ') #if else luar (outer if else)
else:
    print(num, 'adalah bukan bilangan negatif ')
    if num % 2 == 0:                            #if else dalam (inner if else)
        print(num, 'adalah bilangan genap')
    else:
        print(num, 'adalah bilangan ganjil')


# Dalam kode di atas, if-else digunakan dua kali. Pernyataan if-else di luar disebut pernyataan outer if-else, dan pernyataan if-else di dalam disebut pernyataan inner if-else.

# In[ ]:




