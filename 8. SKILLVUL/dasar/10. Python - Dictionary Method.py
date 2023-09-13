#!/usr/bin/env python
# coding: utf-8

# ## Dictionary - Get Method (mendapatkan nilai spesifik) 

# Fungsi get() digunakan untuk mendapatkan value dari key yang spesifik 

# In[1]:


dic = {'a':10,'b':20,'c':30,'d':40}
a = dic.get('a') #fungsi untuk mendapatkan value dari a
print(a)


# In[6]:


#jika tidak ada value dari dic tersebut?, maka hasil akan 0
dic = {'a':10,'b':20,'c':30,'d':40}
b = dic.get('z',0) # tidak terdapat key z dalam dictionary dic sehingga dikembalikan value 0
print(b)


# In[12]:


#Kita juga dapat memberikan default value dalam sebuah fungsi get()
#dic.get(key,default_value)


# Sehingga jika kita menggunakan fungsi get() untuk sebuah key yang tidak ada di dalam sebuah dictionary maka fungsi get() akan mengembalikan default value tersebut.

# In[13]:


dic = {'a':10,'b':20,'c':30,'d':40}
b = dic.get('z',0) # tidak terdapat key z dalam dictionary dic sehingga dikembalikan value 0
print(b)


# ##  Dictionary - Pop, Popitem, Clear Method (menghapus nilai dari dictionary)

# ada beberapa cara untuk menghilangkan item dari sebuah dictionary

# ### Popular 

# Fungsi pop() **digunakan untuk menghapus item** Fungsi pop() menghapus key value pair yang spesifik dan **mengembalikan value yang dihapus**

# In[16]:


dic = {'a':10,'b':20,'c':30,'d':40}
print(dic.pop('a')) #menghapus key value pair dengan key a


# In[15]:


print(dic)


# Contoh kode di atas dic.pop(key) mengembalikan nilai yang dihapus setelah menghapus key-value pair yang spesifik dari dictionary. Dalam contoh kode di atas, dalam sebuah dictionary dic, kita menghapus key-value pair dengan key a dan setelah fungsi pop() dijalankan, fungsi tersebut mengembalikan nilai 10, yang merupakan value dari key a. Setelah dihapus menggunakan fungsi pop() , key-value pair dengan key a dan value 10, sudah tidak ada lagi di dalam dictionary dic.

# ## popitem()

# Fungsi popitem() juga merupakan metode untuk menghapus sebuah elemen dari dictionary, namun fungsi popitem() menghapus key-value pair apa pun dari sebuah dictionary dan mengembalikan key-value pair yang dihapus dalam bentuk tipe data tuple.

# In[23]:


dic = {'a':10,'b':20,'c':30, 'd':40}
print(dic.popitem())


# In[4]:


dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
print(dic.pop('c'))


# ## Dictionary - Items, Keys, Values

# ### Menampilkan dengan keys
# Menampilkan seluruh key yang ada di dalam sebuah dictionary dengan fungsi keys()

# In[5]:


dic = {'a':10,'b':20, 'c':30, 'd':40}
print (dic.keys())


# ### Menampilkan dengan values ()

# In[8]:


#menampilkan seluruh value yang ada dalam dictionary dengan values
dic = {'a':10, 'b':20, 'c':30, 'd':40}
print (dic.values())


# ### Menampilkan dengan Fungsi Items()

# Kita juga dapat mengakses seluruh item dalam sebuah dictionary dengan fungsi items(). Jika fungsi items() digunakan menggunakan for loop maka akan mengembalikan sebuah tipe data tuple yang berisi (key,value) dan bisa kita manfaatkan seperti kode di bawah ini:

# In[10]:


dic = {'a':10,'b':20,'c':30,'d':40}
print(dic.items())


# In[12]:


for str1,num, in dic.items(): #mengakses dictionary dengan for
    print(str1,':',num)


# In[14]:


dic = {'w': 10,'x': 20,'y': 30}

for str,elemens in dic.items():
    if elemens > 10:
        print("Hello!")


# ## Menambahkan dan update data
# ### DICTIONARY - UPDATE

# Fungsi yang digunakan adalah updaet(). fungsi update(key=value) memodifikasi nilai key dalam sebuah dictionary. 

# In[16]:


dic = {'a':10,'b':20,'c':30,'d':40}
print(dic)
dic.update(a=90)
print(dic)


# Jika kita menggunakan fungsi update untuk sebuah key yang tersedia, fungsi update digunakan untuk menambahkan key-value pair dalam dictionary.

# In[21]:


dic = {'a':10,'b':20,'c':30,'d':40}
print(dic)
dic.update(e=50) # karena key e belum ada maka key e dan value akan ditambahkan kedalam dictionary
print(dic)


# Dapat juga kita gunakan dengan bersamaan untuk update data dan menambahkan key 

# In[22]:


dic = {'a':10,'b':20,'c':30,'d':40}
print(dic)
dic.update(a=900,f=60)
print(dic)


# ## Dictionary - Assignment and Copying Method

# ## Copy

# Menggunakan fungsi copy() untuk membuat replika dari dictionary. Hanya ingin sementara mengubah sementara valur dalam dictionary tersebut. 

# In[27]:


x={'a':0,'b':0,'c':0,'d':0}
y=x.copy


# In[28]:


print(x is y) # cek apakah kedua dictionary merupakan objek yang sama
print (x==y) # cek apakah key-value pairnya sama


# In[29]:


print(y)


# In[30]:


type(y)


# Apabila ingin membuat replika dari sebuah double dictionary, kita tidak dapat menggunakan metode copy(). Berikut jika melakukan replika menggunakan metode copy() pada tipe data double dictionary : 

# In[31]:


x = {'a': {'python':'2.7'},'b':{'python':'3.6'}}
y = x.copy()

y['a']['python'] = '2.7.15' # merubah value dari key a - python
print(x)
print(y)


# In[34]:


import copy


# In[36]:


#syntax
#y = copy.deepcopy(dictionary_yang_ingin_dicopy)

x = {'a': {'python':'2.7'},'b':{'python':'3.6'}}
import copy # memanggil copy module
y = copy.deepcopy(x) # deep copy menggunakan deepcopy function dari copy module

y['a']['python'] = '2.7.15' # merubah value dari key a - python
print(x)
print(y)


# In[38]:



a = {'abc': 100, 'cde': 200}
b = a.copy()

print(a is b) 


# ### Dictionary - Default Dict (untuk mencegah error pada key yang tidak ada di dict)

# Fungsi defaultdict() berguna untuk memberikan initial value apabila sebuah key tidak ada di dalam sebuah dictionary.

# Dari contoh di atas kita bisa melihat bahwa jika kita mencoba mengakses key z dari sebuah dictionary x yang tidak memiliki key tersebut, maka akan muncul KeyError.
# 
# Sehingga untuk mencegah hal ini terjadi kita butuh fungsi defaultdict(). Fungsi defaultdict() ini akan membantu kita agar mencegah KeyError dan akan mengembalikan default value. defaultdict() merupakan bagian dari collections module sehingga kita harus melakukan import dengan menggunakan:from collections import defaultdict
# 
# Untuk menggunakan defaultdict() mari kita perhatikan contoh di bawah ini:

# In[40]:


from collections import defaultdict # import default dict method dari collections module

keys = ('a','b','c','d')
y = dict.fromkeys(keys,100)
y = defaultdict(int) # set default value sebagai integer

print(y['z']) # mengakses key z dari dictionary y


# Pada contoh di atas kita mencoba mengakses key z yang tidak ada di dalam dictionary y, namun karena kita sudah memanggil fungsi defaultdict() dan kita sudah set default value sebagi int dan default value dari int adalah 0, maka program akan mengembalikan nilai 0 dan KeyError tidak terjadi.

# ## Dictionary - Double Dictionary 
# 

# Dalam sebuah dictionary, kita bisa memasukkan dictionary ke dalam sebuah dictionary. Hal ini serupa dengan tipe data list. 

# In[45]:


terrestial_planet = {
    'Mercury':{
        'mean_radius':2439.7,
        'mass': 3.3022E+23,
        'orbital_period':87.969,
    },
    'Venus':{
        'mean_radius':2439.7,
        'mass': 3.3022E+23,
        'orbital_period':87.969,
    },
    'Earth':{
        'mean_radius':2439.7,
        'mass': 3.3022E+23,
        'orbital_period':87.969,
    },
    'Mars':{
        'mean_radius':2439.7,
        'mass': 3.3022E+23,
        'orbital_period':87.969,
    }
}

print(terrestial_planet['Venus']['mean_radius'])


# Dalam contoh kode di atas, masing-masing key di dalam dictionary terrestial_ planet memiliki value sebuah dictionary yang berisi 'mean_radius', 'mass', dan 'orbital_period'. Double dictionary sangat berguna untuk menyimpan hierarchical data. Lalu untuk mengakses dictionary yang berada di dalam dictionary kita bisa menggunakan sintaks berikut:

# dictionary[key][key] = value

# Pada contoh kode di atas jika kita ingin mengakses 'mean_radius' dari 'Venus' kita bisa menuliskan seperti berikut:

# In[49]:


print(terrestial_planet['Venus']['mean_radius'])


# In[50]:


a = {"orang": 
        {
        "nama": "Budi",
        "umur": "20",
        "alamat": "Jalan"
        }
}

print(a["orang"]["nama"])


# ## Dictionary - From Keys Method  (mengisi dictionary dengan methode formkeys) 

# Ada berbagai cara untuk membuat dictionary dan salah satunya adalah menggunakan **fromkeys() **

# In[52]:


#syntax
#dict.fromkeys(key_list)


# dimana kita bisa mengkonversikan sebuah list atau tuple menjadi sebuah key list dengan value awal adalah None. Untuk lebih jelasnya mari kita perhatikan kode di bawah ini:

# In[53]:


keys = ['a','b','c','d']
x = dict.fromkeys(keys)
print(x)


# Kode di atas menunjukkan cara membuat sebuah dictionary x dengan key berdasarkan data dari sebuah list keys. Key yang ada di dalam dictionary x berasal dari keys dengan value awal yaitu None.
# 
# Selain membuat dictionary dari tipe data list, kita juga dapat membuat dictionary dari tipe data tuple dengan cara dan hasil yang sama seperti kode di bawah ini:

# In[55]:


keys = ('a','b','c','d')
y = dict.fromkeys(keys,100)
print(y)

