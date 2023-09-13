#!/usr/bin/env python
# coding: utf-8

# # DICTIONARY 

# ## Dictionary Basics 

# Dictionary adalah data yang memiliki pasangan nilai kunci atau sering yang disebut key value pair. Merupakan struktur data yang banyak digunakan karena mengacu pada nilai dengan menggunakan kunci.

# - Dictionary memiliki kemiripan dengan tipe data list, karakteristiknya adalah memiliki pasangan nilai kunci.
# - Kunci harus unik dan tidak dapat diduplikasi. 

# syntax : [kunci] : [nilai] 
# CONTOH

# In[2]:


person = {'Name' : 'David Doe', 'Age' : 26, 'Weight' : 82 } # Dictionary dengan nama, umur dan berat


# In[3]:


print (person)


# In[8]:





# In[10]:


Dalam contoh dibawah ini kita 


# Dalam contoh di bawah ini kita akan melihat konsep dari key-value pair pada sebuah dictionary. Seperti yang ditunjukkan pada kode di bawah, melalui konsep dari key-value pair sehingga dimungkinkan untuk mencari David Doe melalui kunci dictionary person yaitu key Name,Age dan Weight.

# In[11]:


person = {'Name':'David Doe', 'Age':26, 'Weight' : 82}


# In[12]:


person['Name']


# In[13]:


person['Age']


# In[14]:


person['Weight']


# ## DICTIONARY - ADDING, MODIFYING, DELETE VALUES

# ### Adding Items 

# nama_dictionary [nama_kunci] = nilai 

# In[17]:


person = {'Name': 'David Doe', 'Age': 26, 'Weight' : 82}
person['Job'] = 'Data Scientist' # Key baru: masukkan nilai dari key tersebut
print(person)


# ## Modifying Items 

# Dalam mengubah nilai dari sebuah key dalam dictionary yaitu kurang lebih sama dengan menambahkan item ke dalam dictionary, perbedaanya terletak pada nama key. 
# - Mengubah    : nama harus sudah ada
# - Menambahkan : harus dengan key yang baru 

# In[18]:


person = {'Name': 'David Doe', 'Age': 26, 'Weight' : 82}
person['Age'] = 27 # Ubah value dari key yang sudah ada 'Age' 
print(person)


# ## Deleting Items 

# Untuk menghapus, sebuah item bisa dengan del keywords. 

# In[19]:


person = {'Name': 'David Doe', 'Age': 26, 'Weight' : 82}
del person['Age'] # Delete value dari key yang sudah ada 'Age' 
print(person)


# ## Dictionary - Function and Operators

# len() function dan in operator

# Fungsinya untuk mengetahui jumlah item dalam sebuah dictionary, kita bisa menggunakan fungsi len()

# In[22]:


a = {'abc':100,'def':200}
print(len(a))


# in digunakan untuk **memvalidasi** apakah key ada di dalam sebuah dictionary. 

# Operator in akan bernilai true jika key ada dalam dictionary, jika tidak maka false. dan not in melakukan kebalikan dari operator in 

# In[24]:


person = {'Name':'David Joe', 'Age' :26, 'Weight':82}


# In[25]:


len(person)


# In[26]:


'Name' in person


# In[27]:


'job' in person


# In[28]:


'David Doe' in person


# In[29]:


'David Doe' not in person


# ## Json Datatypes - Basics

# Json (Java Script Object Notation) dikembangkan untuk mengirimkan objek data yang terdiri dari key-value-pair. Data ini dalam format standar terbuka menggunakan teks dan dapat kita baca. Ini merupakan format data utama untuk komunikasi antara browser dan server. Digunakna untuk mengekspresikan data saat bertukar informasi di internet. 

# Tidak ada batasan dalam tipe data dan sangat tepat untuk mengekspresikan variabel dari program komputer. Json berawal dari javascript. Sehingga mengikuti sintaks JavaScript, tetapi memiliki format data bahasa independent. kode untuk analisis sintaks dan pembuatan data JSON dapat dengan mudah digunakan dalam berbagai bahasa pemrograman termasuk C, C++, C#, Java, JavaScript, Perl, Python, dan lainnya.

# ![JSON_BASIC.jpg](attachment:JSON_BASIC.jpg)

# ## JSON Read and Exporting

# ### Read Json Data

# Digunakan dalam data, Json untuk membaca file atau string json sebagai dictionary dan mengubahnya menjadi string. 

# Untuk membaca string tipe json, kita dapat gunakan fungsi loads(). Data tipe json yang terdiri dari string dapat diubah menjadi tipe dictionary melalui fungsi loads() dalam modul json. Kita bisa menggunakan fungsi loads() untuk merubah data json menjadi dictionary:

# In[75]:


import json


# In[76]:


data = '{"Name":"David Doe", "Age":25, "Hobby":["basketball"],\"Family":{"father":"John Doe", "mother":"Marry Doe"},"Married" : true}'


# In[77]:


json_data = json.loads(data)


# In[78]:


print (type(json_data))
print(json_data['Name'])
print(json_data['Family'])
print(json_data['Married'])


# ## DUMPS

# fungsi **Dumps** () digunakan untuk merubah dictionary menjadi json-string. Fungsi dumps() untuk menghasilkan sebuah file tipe Json dari data dictionary. 

# In[81]:


import json
Dictionary = {'Halo':123, 'Semua':456}
json_string = json.dumps(Dictionary)

print('Result:',json_string)
print('Tipe:',type(json_string))


# ## Export Json data (json.dump)

# Membuat format json ke dalam file pada python, dapat menggunakan json.dump(). **Harap diperhatikan bahwa ada 2 method yang berbeda yaitu json.dump() dan json.dumps()**

# In[82]:


import json 


# In[83]:


data = '{"tittle":"The Old man and The Sea","ISBN":"12345","Author":"Ernest Hemigway"}'


# In[84]:


json_data = json.loads(data)


# In[85]:


with open('book.json','w') as f:
    json.dump(json_data, f, indent='\t')


# In[ ]:





# In[ ]:




