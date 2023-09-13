#!/usr/bin/env python
# coding: utf-8

# ### Concurrency dan Parallelism

# Dalam dunia digital terutama dunia big data, kita akan banyak sekali bermain dengan data-data yang jumlahnya sangat banyak dan data tersebut harus kita proses dengan cepat, namun jika kita menggunakan process secara synchronous atau suatu task harus menunggu sampai task sebelumnya selesai, maka ini akan menjadi masalah yang besar.
# 
# Maka dari itu, kita juga harus membuat program kita bisa berjalan secara asynchronous agar kita bisa meningkatkan performance dari program yang kita buat dan mengurangi total processing time.
# 
# Untuk mengatasi hal tersebut kita dapat menggunakan konsep parallelism dan concurrency.
# 
# Secara umum, concurrency dianggap sebagai konsep yang lebih besar daripada parallelism. Sederhananya, kedua konsep tersebut melakukan banyak hal pada saat yang bersamaan. Dalam praktiknya, ada sudut pandang tertentu pada perbedaan antara kedua ide tersebut, terutama dalam Python.
# 
# Concurrency kemudian sering dipahami sebagai "mengelola" banyak pekerjaan secara bersamaan. Pada kenyataannya, pekerjaan-pekerjaan itu tidak benar-benar dijalankan pada saat yang bersamaan. Mereka bergantian secara Parallelism, berarti mengeksekusi beberapa pekerjaan secara bersamaan atau secara paralel. Parallelism memungkinkan untuk memanfaatkan banyak core pada satu mesin.

# Untuk menerapkan kedua konsep tersebut dalam Python, kita bisa menggunakan library:
# 
# - multiprocess untuk parallelism dan,
# - threading untuk concurrency

# ## Threading 

# Thread  adalah ***entitas dalam proses yang dapat dijadwalkan untuk dieksekusi***. Thread juga adalah unit pemrosesan terkecil yang dapat dilakukan dalam sistem operasi. 

# Dengan kata lain, thread adalah urutan instruksi semacam itu dalam program yang dapat dieksekusi secara independen dari kode lain. Untuk kesederhanaan, anda dapat mengasumsikan bahwa thread adalah bagian dari proses. 

# Multithreading didefinisikan sebagai kemampuan prosesor untuk mengeksekusi beberapa thread secara bersamaan.

# In[5]:


import threading # import library threading
import time # import library time

def print_with_dynamic_sleep(total_iteration):
    
    """ 
    fungsi berikut akan melakukan print command 
    dengan interval yang berbeda - beda
    """
    for x in range (total_iteration):
        print("Hello from dynamic-sleep interval, pengulangan ke-{}".format(x))
        time.sleep(x) #fungsi akan berhenti selama x second, akan berubah2 secara dinamis

def print_with_static_sleep(total_iteration):

    """
    fungsi berikut akan melakukan print command 
    dengan interval yang statis/sama
    """
    
    for x in range (total_iteration):
        print("Hello from static-sleep interval, pengulangan ke-{}".format(x))
        time.sleep(2) #akan berhenti setelah 2 second

if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_with_dynamic_sleep, args=(5,))
    t2 = threading.Thread(target=print_with_static_sleep, args=(5,))

	# memulai thread pertama
	t1.start()
	# memulai thread kedua
	t2.start()

	# tunggu sampai thread 1 selesai dilaksanakan
	t1.join()
	# tunggu sampai thread 2 selesai dilaksanakan
	t2.join()

	# both threads completely executed
	print("Selesai!")
    


# In[ ]:


# sintaks thread 
t1 = threading.Thread(target=nama_fungsi, args=(5,)) 
# kita juga bisa memberikan argument kedalam fungsi tersebut
# nama fungsi tidak perlu menggunakan '()'

# mendeclare fungsi
def nama_fungsi(params): 
    #lakukan sebuah process


# Bisa terlihat dari output program, kedua function tersebut tidak saling menunggu sama lain hingga function yang lainnya selesai melainkan melakukan proses dalam block function masing-masing secara parallel.

# ## Multiprocessing

# Apa itu sebenarnya multiprocessing? **Multiprocessing mengacu pada kemampuan sistem untuk mendukung lebih dari satu prosesor pada saat yang bersamaan.** Aplikasi dalam sistem multiprocessing dipecah menjadi rutinitas yang lebih kecil yang berjalan secara independen. Sistem operasi mengalokasikan thread ini ke prosesor untuk meningkatkan kinerja sistem.
# 
# **Multiprocessing sangat cocok untuk program atau sistem yang membutuhkan komputasi CPU yang tinggi, karena bisa memaksimalkan jumlah CPU yang ada didalam komputer tersebut.** Namun Ada beberapa hal yang perlu diperhatikan dalam process multiprocessing.

# -     Pertama, kita harus dapat menentukan apakah beberapa data mungkin benar-benar perlu diakses oleh semua proses, karena memori antar proses tidak dibagikan.
# - Terakhir, jika komputasi dalam program kita sebenarnya tidak terlalu intensif, multiprocessing mungkin tidak mempercepat secara signifikan karena overhead process untuk menjalankan interpreters.

# In[17]:


import multiprocessing # import library multiprocessing
import time # import library time


# In[18]:


def print_with_dynamic_sleep(total_iteration):
    """
    fungsi berikut akan melakukan print command
    dengan interval yang berbeda-beda
    """
    for x in range(total_iteration):
        print("Hello from dynamic-sleep interval, pengulangan ke-{}".format(x))
        time.sleep(x) # fungsi akan berhenti selama x second, akan berubah2 secara dinamis

def print_with_static_sleep(total_iteration):
    """
    fungsi berikut akan melakukan print command
    dengan interval yang statis/sama
    """
    for x in range(total_iteration):
        print("Hello from static-sleep interval, pengulangan ke-{}".format(x))
        time.sleep(2) # fungsi akan berhenti selama 2 second


# In[19]:



if __name__ == "__main__":
    # creating thread
    p1 = multiprocessing.Process(target=print_with_dynamic_sleep, args=(5,))
    p2 = multiprocessing.Process(target=print_with_static_sleep, args=(5,))

    # memulai process pertama
    p1.start()
    # memulai process kedua
    p2.start()

    # tunggu sampai process 1 selesai dilaksanakan
    p1.join()
    # tunggu sampai process 2 selesai dilaksanakan
    p2.join()

    # both threads completely executed
    print("Selesai!")


# Secara API dan syntax penulisan, multiprocessing memiliki cukup banyak kemiripan dengan threading:

# In[ ]:


p1 = multiprocessing.Process(target=nama_fungsi, args=(5,)) 
# kita juga bisa memberikan argument kedalam fungsi tersebut
# nama fungsi tidak perlu menggunakan '()'

# mendeclare fungsi
def nama_fungsi(params):
  # lakukan sebuah process


# Perbedaan mendasar antara multiprocessing dengan thread dalam Python adalah 
# - multiprocessing secara efektif mengesampingkan Global Interpreter Lock atau (GIL) dengan menggunakan subproses, bukan menggunakan thread. 
# 
# Oleh karena itu, modul multiprocessing memungkinkan program untuk sepenuhnya memanfaatkan multi-core processor pada mesin atau komputer kita.

# In[ ]:




