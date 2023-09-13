#!/usr/bin/env python
# coding: utf-8

# # BASIC FOR LOOP SYNTAX

# Sebagai contoh loop statement akan kita gunakan for dan loop yang memiliki sintaks sebagai berikut : 

# ![for_loop.jpg](attachment:for_loop.jpg)

# Terdapat dua buah kompionen penting dalam loop yaitu : 
# 1. Variable
# 2. Range Function 

# Variabel yang digunakan untuk loop berupa pernyataan berupa abjad seperti i, j,k,l dan variabel ini disebut kontrol loop

# Range function merupakan bagian penting dalam for loop syntax yang berguna untuk mengontrol fungsi dan kerja dari loop statement. 
# 1. Dalam range dapat menghasilkan bilangan bulat berurutan antara nilai awal yang diberikan dan nilai berhenti, seperti dalam rentang (0,5) atau dapat menambahkan nilali tambahan di akhir, seperti dalam rentang (0,5,2)
# 2. Dalam rentang (0,5,1) 1 terakhir adalah nilai langkah default yang ditambahkan di setiap kenaikan. 

# ![for_llo_1.jpg](attachment:for_llo_1.jpg)

# Dengan memanggil fungsi range (0, stop,1) menghasilakn bilangan bulat dari 0 hingga (stop-1) dengan kelipatan 1.
# Semua angka yang dihasilkan dalam range hanya bisa menggunakan integer sehingga jika kita menggunakan float sebagai contoh, akan muncul error

# In[ ]:


for i in range (0.9):
    print (i,'Welcometo everyone!!')


# In[ ]:


for i in range (4):
    print (i,"welcome")


# In[ ]:


for i in range (0,5,2): #0 bilangan dimulai, 6 adalah jumlah range, dan bilangan ke 3 adalah bilangan yang ditampilkan setelah bilangan awal
    print (i,"welcome") 


# ## SEQUENCE OBJECT ITERATION

# Jika data sudah disediakan dalam list dengan elemen tertentu, perlu sebuaha cara untuk secara berurutan mengunjungi nilai - 
# nilai dalam list tersebut. 

# Nilai - nilai di dalam list [11,22,33,44,55,66]

# ![SEQUENCE_LOOP.jpg](attachment:SEQUENCE_LOOP.jpg)

# In[ ]:


name = [11,22,33,44,55,66] #(variabel yang sudah ditentukan)
for n in name: #menggunakan n sebagai alias in name (sebagai variabel yang akan di panggil
    print("angka",n)


# ## WHILE vs LOOP

# Merupakan looping statement yang sama dengan for loop hanya berbeda cara dalam mengakhirinya 

# For loop berakhir setelah mengunjungi semua elemen pada sequences setelah keyword in, dimana sequences ini berbentuk seperti sebuah fungsi range() ataupun sebuah list sudah ditentukan sebelumnya. 
# 1. Sementara while looping mengulangi instruksi hanya jika sebuah kondisi benar. 
# 2. Sebagai contoh : while x < 5: while function berikut akan mengulangi instruksinya selama variable x memiliki nilai kurang dari 5, dan akan berhenti apabila memiliki nilai 5 atau lebih dari 5.

#     !!! Jika kondisinya terus benar, while loop ini mungkin tidak akan berakhir, jadi berhati-hatilah saat menulis kode.

# In[ ]:


i = 0
while i<6:
    print ('Welcome to everyone!')
    i+=1


# In[40]:


for i in range (6):
    print ("welcome")


# # BREAK vs CONTINUE KEYWORDS

# break dan continue adalah contoh dari Loops and Control Statements. Kedua keywords ini dapat mengontrol dan menentukan proses dari sebuah loop.
# 
# break berfungsi untuk mengakhiri sebuah looping
# continue berfungsi untuk melewati bagian eksekusi yang ada dalam sebuah loop di iterasi tersebut dan lanjut mengeksekusi iterasi selanjutnya
# 
# Untuk lebih jelasnya perhatikan penjelasan kedua keyword tersebut:

# 1. BREAK while dan loop statement melakukan proses dalam block jika kondisinya benar atau bernilai True
# 2. Jika Break diletakkan ditengah proses, maka proses yang sedang berjalan dipaksa segera berakhir dan keluar dari blok loop tersebut

# ![break.jpg](attachment:break.jpg)

# In[52]:


st = 'Programming'
# fungsi akan di eksekusi selama huruf adalah konsonan
for c in st:
    if c in ['a','e','i','o','u']:
        break # stop loop jika menemukan huruf vokal
    print(c)
print('The end')


# Break jika itu adalah huruf vokal, jika tidak tampilkan emnggunakan fungsi print()
# Ketika break dieksekusi, proses looping dihentikan tanpa mengeksekusi sisa iterasi yang ada

# ### CONTINUE 

# FUNGSI : untuk melewati bagian eksekusi yang ada dalam sebuah loop di iterasi tersebut dan lanjut mengeksekusi iterasi selanjutnya. 
# Pengakhiran loop hanya berlaku jika kondisinya salah atau false. 

# ![continue.jpg](attachment:continue.jpg)

# In[53]:


st = 'Programming'
for c in st:
    if c in ['a','i','o','u']:
        continue #skip eksekusi kode dibawah jika huruf vokal 
    print(c)
print('The end')


# Perbedaan mendasar dengan break, continue hanya melewatkan beberapa proses print(ch) dalam program di atas, dimana dalam string 'Programming' huruf vokal (o,a, dan i) tidak dieksekusi oleh print(). Berbeda dengan break, ketika bertemu dengan huruf vokal (o,a, dan i), break langsung menghentikan proses looping.

# ## NESTED LOOP 

# In[57]:


for i in range (2,10): #outer for loop
    for j in range (1,10): #inner for loop
        print ('{}X{} = {:2d}, '. format(i,j,i*j), end = '')
print () #executes inner loop and change line


#     i memiliki nilai dari 2 hingga 9.
#     j bagian dalam memiliki nilai dari 1 hingga 9`.
#     Struktur ini diulang, menghasilkan 72 perhitungan dan output secara total.
#     Dalam kasus double for loop atau triple for loop, menjadi sulit untuk membaca dan memahami kode.
#     Untuk alasan ini, nested loop tidak disarankan menggunakan struktur lebih dari tiga loop.

# In[ ]:




