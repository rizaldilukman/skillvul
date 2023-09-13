#!/usr/bin/env python
# coding: utf-8

# # TIPE DATA DAN OPERATOR

# ## 1. TIPE DATA BASIC

# ### KLASIFIKASI TIPE DATA
# Beberapa struktur dan tipe data dalam bahasa python yang sering dipakai 
# 1. Number
# 2. Boolean
# 3. String
# 4. List
# 5. Tuple 
# 6. Dictionary 

# ![tipe_data.jpg](attachment:tipe_data.jpg)

# ### MEMBEDAKAN DAN MENGETAHUI TIPE DATA 
# 1. Istilah yang mengacu pada nilai numerik, fungsi, dan kelas yang merupakan komponen python dan objek
# 2. Peran Operator berbeda tergantung pada apakah tipe data objek adalah integer atau string
# 3. Fungsi (type()) untuk mengetahui tipe data yang sedang digunakan

# contoh:

# In[1]:


type(200) #Memberi tahu tipe data dari 100


# In[6]:


type (200.0) # tipe data ini berbeda dengan yang diatas


# In[3]:


type ('200')


# In[5]:


type (10 + 3j) #tipe data bilangan kompleks berupa bilangan real + imajiner seperti 10 + 3j


# ### CARA MENGUBAH TIPE DATA 
# String '10' dapat diubah menjadi tipe data integer menggunakan fungsi int('10'). Oleh karena itu, int('10')/2 dijalankan tanpa error. Untuk mengubah nilai numerik 10 pada Python ke string '10', gunakan fungsi str(10).

# In[13]:


int('10')/2 # Ubah string '10' menjadi bilangan bulat dan bagi dengan 2.


# In[14]:


'i like number' + str(10) #Ubah angka 10 menjadi string dan gunakan + operator


# In[15]:


a = None 
type(a)


# ## 2. TIPE DATA STRING

# Tipe data ini dugnakan untuk menampilkan informasi berangkat lunak. 
# String dalam python adalah bentuk dimana setiap huruf terhubung.
# Operasi penjumlahan dan perkalian dimungkinakna untuk string dalam python
# Huruf dan spasi dalam sebuah string juga disebut sebagai character.

# ## A. STRING OPERATOR

# String Operator operasi + dan * yang diperbolehkan dalam string, digunakan untuk menghubungkan dua string atau menduplikasi string tersebut. contoh seperti dibawah ini. 

# In[16]:


'I'+'Love'+ 'Python' # String dapat ditambahkan dalam string 


# In[17]:


'Python' * 10 # Menghasilkan string python sebanyak 10 kali


# In[18]:


'*' * 50 # Menghasilkan string * sebanyak 50 kali


# In[19]:


str(100) * 10 #String 100 diulang 10 kali


# In[22]:


'100'*10


# ## B. STRING INDEXING 

# Pengindeksian string dapat digunakan untuk emndapatkan beberapa karakter dari string yang panjang. digunakan tanda kurung besar [] dan nomor /urutan index. Terdapat dua jenis Indexing yaitu : Positive Index dan Negative Index

# POSITIVE INDEX : Digunakan jika dalam suatu kalimat ingin mendapatkan karakter pertama dalam string tersebut, dimulai dari 0. Contohnya seperti dibawah ini:

# In[24]:


"hello"[0]


# In[25]:


"hello"[1]


# NEGATIVE INDEX  : Digunakan untuk mengambil karakter dari akhir kata dan dimulai dari 1 dan menambahkan tanda (-). Contohnya seperti dibawah ini : 

# In[26]:


"hello"[-1]


# ## C. STRING BUILT - IN FUNCTION

# Dalam tipe data string di python, ada beberapa built - in function yang digunakan dalam python, yaitu : 
# 1. split   : Berguna sebagai separator yang di inginkan dan mengembalikan hasilnya sebagai sebuah list
# 2. islower : Mengecek apakah semua element adalah huruf kecil,
# 3. count    : Menghitung berapa kali value muncul dalam sebuah string
# contoh : 

# In[32]:


##contoh split
teks = "halo, nama saya, budi"
x = teks.split(",")
print(x)


# In[34]:


#contoh islower
a = "Halo"
b = "halo"
print (a.islower())
print (b.islower())


# In[36]:


#contoh count
teks = "Halo semuanya, disini saya bersama dengan budi semuanya"
x = teks.count("semuanya")
print(x)


# ## 3. OPERATOR BASIC
# Digunakan untuk operasi numerik (aritmatika). Nilai data atau variabel yang akan dipakai disebut operand. Subjek operasi disebut Operator. Operator basic dalam bahasa pemrograman python adalah dibawah ini. 

# ![operator.jpg](attachment:operator.jpg)

# ### Penggunaan Operator

# In[37]:


100 + 2 #Penjumlahan angka


# In[38]:


100*2 #Perkalian Angka


# In[39]:


100 - 20 #Pengurangan Angka


# In[44]:


x=100/20 #pembagian angka (hasilnya akan float (desimal))
print (x)
type (x)


# In[47]:


x = 100//20  #Pembagian angka tanpa sisa(hasilnya integer (bilangan bulat)
print (x)
type (x)


# In[48]:


x = 100%20 #Pembagian dengan menemukan hasil dari sisa bagi 
print (x)
type (x)


# ###  PRIORITAS OPERATOR
# 1. Penjumlahan dan perkalian muncul dalam satu kalimat, maka yang dilakukan operasi adalah perkalian terlebih dahulu
# 2. Ketika tanda kurung mulai terlebih dahulu, maka  dilakukan operasi dengan tanda kurung terlebih dahulu.
# 3. Hasil penghitungan dalam operasi bervariasi sesuai dengan pemrosesan operator

# In[49]:


10+20*30 #python akan menghitung perkalian terlebih dahulu


# In[50]:


(10+20)*30 #python akan menghitung yang didalam kurung terlebih dahulu 


# Berikut beberapa urutan - urutan prioritas yang sering digunakan dalam python

# ![operator_prioritas.jpg](attachment:operator_prioritas.jpg)

# ## 4. BUILT IN FUNCTION

# Fungsi ini berguna untuk meringkas program kita di python 
# contoh: int(digunakan untuk bilangan bulat)
#         float(digunakan untuk nilai pangkat suatu bilangan)
#         str(string digunakan untuk mengubah sebuah obejk menjadi string)

# In[56]:


#contoh tipe data integer
x = int("12") #bilangan dalam bentuk string akan dibuah dalam bentuk integer
y = int(12.5) #bilangan dalam bentuk float di ubah menjadi bentuk string 
print (x)
print(y)     


# In[58]:


#contoh tipe data float
x = pow(3, 3) #3 pangkat 3
y = pow (3,-3) #3 oangkat -3
print (x)
print (y)


# In[60]:


#contoh tipe data string 
x = str(12) #mengubah bentuk integer menjadi bentuk string
y = str (12.5) #mengubah bentuk float menjadi string
print (type(x))
print (type(y))


# In[ ]:




