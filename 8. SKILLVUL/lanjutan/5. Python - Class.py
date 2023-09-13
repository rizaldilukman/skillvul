#!/usr/bin/env python
# coding: utf-8

# ## Definition Concept of Object 

# Python merupakan salah satu contoh dari Object Oriented Programming Language atau yang biasa lebih dikenal dengan singkatan OOP. Hampir semua hal di dalam Python adalah sebuah object, dengan properties and method object tersebut.

# ![oop1.jpg](attachment:oop1.jpg)

# Beberapa materi yang saling berinteraksi di dalam sebuah game disebut sebagai object, hal ini juga sama seperti element dari sebuah GUI pada komputer disebut sebagai object. Serta Class merupakan sebuah blueprint untuk membuat object atau biasa disebut sebagai object constructor.

# Sintaks untuk memanggil object dan method dari sebuah class dalam Python adalah sebagai berikut:
# 
# OOP in Python

# In[2]:


'tiger'.upper()


# ![oop_2.jpg](attachment:oop_2.jpg)

# ![oop_3.jpg](attachment:oop_3.jpg)

# Berikut contoh ilustrasi bahwa dari beberapa built-in module Python seperti datetime module, sys module, math module dan lain-lain. Terdiri dari beberapa class yang juga berisi beberapa atribut serta method yang bisa kita panggil menggunakan sintaks di atas. Namun di dalam sebuah program, selain kita membutuhkan object, kita juga memerlukan interaksi antara object tersebut.

# ## Class - INstance vs Class

# Dalam konsep OOP, terdapat istilah instances dan objects dan kedua istilah ini cukup penting dalam OOP dan kita juga harus mengetahui perbedaan mendasar dari kedua istilah ini.
# - Class : Sebuah konsep abstrak yang menunjukkan satu set atribut dan tindakan yang digunakan dalam sebuah program.
# - Instances : Sebuah objek individu yang dibuat dari class. Instances memiliki nilai atribut tertentu yang spesifik.
# 
# Untuk lebih jelas tentang perbedaan antara class dan instances, mari kita lihat ilustrasi berikut ini:||

# ![instance1.jpg](attachment:instance1.jpg)

# Dalam contoh di atas, konsep abstract dari sebuah kucing (sebuah kucing pasti memiliki warna, ukuran dan nama) adalah contoh dari class, dan sebuah kucing yang spesifik dan memiliki warna, ukuran dan nama tertentu merupakan sebuah instances.

# ## Declaring and Self Parameters

# Untuk mendeklarasikan dan mmebuat sebuah class dan object, berikut contoh sederhana dalam kode Python : 

# In[3]:


class cat:#membuat class cat
    pass #menggunakan pass statement
nobi = cat() #membuat sebuah instance dari Cat
print (nobi)


# Dalam kode diatas, kita sudah bisa mendeklarasikan class, hanya saja belum berguna didalam program dan kali ini kita akan menambahkan method ke dalam class tersebut. 

# **Method adalah function yang didefinisikan di dalam class yang digunaka oleh class atau instance dari class**

# In[8]:


class Cat:# membuat class Cat
    def meow(self): #fungsi meow didalam class Cat
        print('meowww')
nobi = Cat() #membuat sebuah instance dari CAt
nobi.meow() #setelah membuat object dari Cat, kita bisa memanggil method meow


# Di dalam method kita juga perlu menambahkan self-keyword, dimana self keyword adalah : 

# **variabel yang mereferensikan dirinya sendiri dan dgunakan untuk mengakses variabbel yang dimiliki class tertentu.**
# 

# _self keyword_ wajib diberikan pada parameter pertama dari sebuah method

# ## Class - Constructor _init_method

# Dalam konsep OOP kita juga mengenal namanya constructor. Umumnya digunakan untuk membuat instance objek. Tugasnya adalah menginisialisasi (menitiokan nilai) ke anggota data dari _class_ tersbeut ketika objek dari class tersebut dibuat. 

# Didalam Python kita dapat menggunakan _init_ method dalam mengaplikasikan konsep constructor. Contoh penggunaannya didalam kode adalah sebagai berikut : 
# 

# In[15]:


class Cat:
    def _init_(self,name,color): #menginisialisasi instance dengan constructor
        self.name = name
        self.color = color


# In[24]:


nobi = Cat('nobi','black') # membuat instance dari kelas Cat dengan nama nabi dan warna hitam
nero = Cat('nero','white')

print(nobi.name)
print(nobi.color)
print(nero.name)
print(nero.color)


# Dari kode di atas, __init__ method akan dieksekusi (__init__ method selalu dieksekusi saat awal kita membuat object).
# 
# name --> self.name
# 
# color --> self.color

# ![init.jpg](attachment:init.jpg)

# ## Class - Instance vs Class Variables

# ### Instance Variables
# 

# Jika nilai dari variabel bervariasi dari objek ke objek, maka variable tersebut disebut instance variabels. _Instance variables_ tidak dibagikan sebagai objek. Setiap objek memiliki salinan sendiri dari instance attribute. Artinya, untuk setiap objek suatu kelas, memiliki nilai instance variables yang berbeda. 

# In[32]:


class Circle:
    def _init_(self, name, radius,PI):
        self._name = name #instance variable
        self._radius = radius #instance variable
        self._Pi = Pi


# In[33]:


#menghitung area sebuah lingkaran denagn pi * r kuadrat
def area (self):
    return self._Pi*self._radius**2  # rumus lingkaran


# In[35]:


c1 = Circle("C1",4,3.14)


# In[36]:


class Circle:
  def __init__(self,name,radius,PI):
    self.__name = name # instance variable
    self.__radius = radius # instance variable
    self.__PI = PI
  
  # menghitung area sebuah lingkaran dengan pi * r kuadrat
  def area(self):
    return self.__PI * self.__radius ** 2

c1 = Circle("C1",4,3.14)
print("Area dari c1:",c1.area())
c2 = Circle("C2",6,3.141)
print("Area dari c2:",c2.area())
c3 = Circle("C3",6,3.1415)
print("Area dari c3:",c3.area())


# __name, __radius, __PI dalam kode di atas dapat memiliki nilai yang berbeda untuk setiap instance. Variabel seperti itu disebut instance variables.

# Alasan menggunakan awalan '__' adalah untuk menyembunyikan instance ini dari akses eksternal.

# ![class_.jpg](attachment:class_.jpg)

# ### Class Variables

# Dari contoh di atas mengenai instance variables, terkadang kita memerlukan suatu variabel yang bisa di bagikan ke seluruh instance dari class tersebut, contohnya adalah nilai dari PI. Nilai dari PI adalah constant sehingga seharusnya masing-masing instance memiliki nilai PI yang sama dan tidak perlu di deklarasikan di masing-masing instance serta mengurangi kemungkinan error. Maka disini kita menggunakan yang disebut sebagai class variable.
# 
# Class Variable in Python

# ![class_variable.jpg](attachment:class_variable.jpg)

# Dan contoh instance variables sebelumnya jika kita menggunakan PI sebagai class variable, ilustrasinya adalah seperti dibawah ini

# ![circle_class.jpg](attachment:circle_class.jpg)

# In[1]:


class Circle:
  PI = 3.1415
  def __init__(self,name,radius):
    self.__name = name # instance variable
    self.__radius = radius # instance variable
  
  # menghitung area sebuah lingkaran dengan pi * r kuadrat
  # method dari class Circle dan instance akan mengambil value PI dari class variable melalui Circle.PI
  def area(self):
    return Circle.PI * self.__radius ** 2

c1 = Circle("C1",4)
print("Area dari c1:",c1.area())
c2 = Circle("C2",6,)
print("Area dari c2:",c2.area())
c3 = Circle("C3",5)
print("Area dari c3:",c3.area())


# ## CLASS - INHERITANCE

# Konsep Inheritence ditunjukkan melalui ilustrasi di bawah ini. Person, yang merupakan parent class, memiliki fitur yang agak umum. Person tersebut akan memiliki fitur umum seperti usia, jenis kelamin, nama, dan lain-lain. Namun, child class seperti Manager(Manajer), Employee(Karyawan) dan Student(Siswa), akan memiliki seluruh attribute dan method yang diwarisi oleh class Person serta dapat mengubah yang ada dan menambahkan attribute dan method baru.
# 
# Inheritance in Python

# ![INHERITANCE.jpg](attachment:INHERITANCE.jpg)

# In[4]:


class Person: # Parent class
    nama = 'test'
class Employee(Person): #child class
    gaji = 1000
person1  = Person ()
employee1 = Employee ()
print ('nama dari person',person1.nama)
print ('nama dari employee',employee1.nama)
print ('gaji dari employee',employee1.gaji)
print ('gaji dari person',person1.gaji)


# ## Class - Polymorphism

# _Polymorphism_ berarti memiliki bentuk yang berbeda - beda. Dalam dunia pemrograman, Polymorphism mengacu pada kemampuan fungsi dengan nama yang sama untuk membawa fungsionalitas yang berbeda secara bersamaan. Ini menciptakan struktur yang dapat menggunakan banyak bentuk objek. 
# 

# Pada Childclass, slain mewarisi semua sifat dari parent-ny, child class juga berisi kemampuan yang berbeda- beda dengan parent nya, namun bisa jadi berbeda output dengan sibling atau parent nya, hal ini disebut polymorphism. 

# Polymorphism pada python adalah membuat method pada child class yang mempunyai nama yang sama dengan method milik parent class. Bedanya dengan inheritance child class meawarisi methods langsung dari parent class. Hal ini juga memungkinkan untuk memodifikasi method pada child class yang mewarisi langsung dari parent class.

# ![polymorphism.jpg](attachment:polymorphism.jpg)

#     Kucing adalah Hewan
#     Anjing adalah Hewan
#     Anggora adalah Kucing
#     Anggora adalah Hewan

# Contoh gambar di atas menjelaskan bahwa, child class adalah bagian dari parent class. Namun parent class bukanlah bagian dari child class. Walaupun Kucing dan Anjing merupakan bagian dari Hewan, tetapi mereka memiliki karakteristik yang berbeda.
# 
# Pada topik sebelumnya, kamu sudah belajar caranya untuk mewarisi suatu class. Maka child class akan memiliki properti dan method dari parent class-nya. Polymorphism di sini mengarah pada method yang dimiliki oleh child class.

# ## Implementasi Polymorphism

# In[1]:


class Bird:
    def intro (self):
        print("There are different types of birds")
    
    def flight (self):
        print("Most of the birds can fly but some cannot")

class parrot (Bird):
    def flight(self):
        print("Parrots can Fly")

class penguin (Bird):
    def flight (self):
        print("Penguins do not fly")
        
        
obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()


obj_bird.intro()
obj_bird.flight()


obj_parr.intro()
obj_parr.flight()


obj_peng.intro()
obj_peng.flight()
    
    
    


# ###  Dapat juga dengan loop yang berulang melalui object tuple

# In[4]:


class hewan ():
    def suara (self):
        print ("suara hewan")

class kucing ():
    def suara (self):
        print ("meow")
        
    def harapan_hidup (self):
        print ("harapan hidup kucing adalah 10 tahun")
        
    def warna (self):
        print ("warna bulu kucing adalah warna kuning")

class anjing ():
    def suara (self):
        print ("woof")
    def harapan_hidup (self):
        print ("harapan hidup anjing adalah 15 tahun")
    def warna (self):
        print ("warna bulu anjing adalah hitam")

obj1 = kucing()
obj2 = anjing()

for type in (obj1,obj2): #creating a loop to iterate through the obj1, obj2
    type.harapan_hidup()
    type.warna()


# Terlihaht dalam loop diatas kita dapat membuat sebuah tuple yang berisi objek dari sebuah class dan memanggil method.

# ### Keuntungan Polymorhism

# - Code dan class yang ditulis sekali dapat digunakan kemabli dan diimplementasikan berulang kali
# - Ini membantu dalam mengurangi coupling antara fungsi yang berbeda dan perilaku objek

# In[6]:


class Kucing(): 
    def suara(self):
       print("Meow")
   
    def warna_tubuh(self): 
      print("Warna tubuh kucing pada umumnya adalah kuning") 
   
class Anjing(): 
    def suara(self):
      print("Woof")

    def harapan_hidup(self): 
      print("Harapan hidup anjing adalah 15 tahun.") 
   
   
obj1 = Kucing() 
obj2 = Anjing() 
for type in (obj1, obj2):
    type.suara()


# ## Class - Encapsulation  

# Saat bekerja dengan class dan menangai data yang sensitif, menyediakan akses global ke semua attribute yang digunakna dalam program bukanlah pilihan yang baik. Encapsulation menawarkan cara terbaik untuk mengakses attribute tanpa memberikan program akses penuh ke salah satu attribute.

# Memperbarui, mengubah, atau menghapus data dari attribute dapat dilakukan melalui penggunaan metode yang ditentukan secara khusus untuk tujuan tersebut. Manfaat menggunakan pendekatan pemrograman ini adalah peningkatan kontrol atas data input dan keamanan yang lebih baik.

# ### Metode untuk mengontrol akses

# #### Single Underscore

# Konvensi pemrograman Python umum untuk mengidentifikasi private attribute adalah dengan mengawalinya dengan garis bawah atau undescore _. Namun ini tidak benar-benar membuat perbedaan di sisi compiler. Variabel atau attribute masih dapat diakses seperti biasa. Tetapi menjadi standar yang telah disetujui oleh programmer yang memberi tahu programmer lain bahwa attribute atau method harus digunakan hanya dalam lingkup class.

# In[19]:


class Orang:
    def __init__(self, name, age=0):
        self.name = name
        self._age = age
 
    def tampilkan(self):
        print(self.name)
        print(self._age)
 
orang_obj = Orang('Budi', 30)

#mengakses melalui metode
orang_obj.tampilkan()

#mengakses langsung variable
print(orang_obj.name)
print(orang_obj._age)


# Terlihat dari kode di atas bahwa kita tetap bisa mengakses langsung variable _age dari luar class menggunakan instance dari class tersebut.

# #### Double Underscore

# Jika kita ingin menjadikan anggota class yaitu method dan attribute menjadi private, maka kita harus mengawalinya dengan garis bawah ganda atau double underscore__.

# In[21]:


class Orang:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age
 
    def tampilkan(self):
        print(self.name)
        print(self.__age)
 
orang_obj = Orang('Budi', 30)

#mengakses melalui metode
orang_obj.tampilkan()

#mengakses langsung variable
print(orang_obj.name)
print(orang_obj.__age)


# Jika kita menggunakan double underscore pada variable __age, maka terlihat kita hanya bisa mengakses variabel tersebut melalui metode getter yaitu tampilkan() dan akan muncul error apabila kita ingin mencoba mengakses variabel tersebut diluar dari class.
# 
# Untuk mengubah data, kita juga perlu membuat setter karena tidak bisa mengubah data secara langsung.

# In[23]:


class Orang:
  def __init__(self, name, age=0):
    self.name = name
    self.__age = age

  def setAge(self, age):
    self.__age = age
 
  def tampilkan(self):
    print(self.name)
    print(self.__age)
    print("----------")
 
orang_obj = Orang('Budi', 30)

#mengakses melalui metode
orang_obj.tampilkan()

#mengubah data tanpa setter tidak memungkinkan
orang_obj.__age = 50
orang_obj.tampilkan()

#mengubah data harus memalui setter
orang_obj.setAge(27)
orang_obj.tampilkan()


# In[24]:


class Orang:
  def __init__(self, name, age=0):
    self.name = name
    self._age = age

org_obj = Orang('Budi')
print(org_obj._age)


# ## Class - Abstraction

# Abstraction adalah salah satu konsep kunci dari bahasa pemrograman berorientasi objek (OOP). Tujuan utamanya adalah untuk menangani kompleksitas dengan menyembunyikan detail yang tidak perlu dari pengguna. Abstraction memungkinkan pengguna untuk menerapkan logika yang lebih kompleks di atas abstraksi yang disediakan tanpa memahami atau bahkan memikirkan semua kompleksitas yang tersembunyi.
# 
# Misalkan Kamu memesan tiket film dari aplikasi online menggunakan internet banking atau proses lainnya. Kamu tidak tahu prosedur bagaimana pin dihasilkan atau bagaimana verifikasi dilakukan. Ini disebut abstraksi dari aspek pemrograman, pada dasarnya berarti Kamu hanya menampilkan detail implementasi dari proses tertentu dan menyembunyikan detail dari pengguna. Ini digunakan untuk menyederhanakan masalah yang kompleks dengan memodelkan kelas yang sesuai dengan masalah.
# 
# Dalam Python, abstraction dapat dicapai dengan menggunakan abstract classes and interfaces.

# ## Abstract Class in Python

# Class yang terdiri dari satu atau lebih abstract method disebut Abstract Class. Abstract Class dimaksudkan untuk menjadi blueprint dari kelas lain. Python menyediakan modul abc untuk menggunakan abstraksi dalam program Python. Berikut adalah sintaks Abstraction menggunakan modul abc

# In[31]:


from abc import ABC, abstractmethod
class abstract_class(ABC): 
    """ normal_methd """
    def normal_methd(self):
        pass #normal_methd definition
    """ abstract_methd"""
    def abstract_methd(self):
        pass #abstract_methd definition


# In[32]:


from abc import ABC, abstractmethod 

class MobilMewah(ABC):  
    @abstractmethod 
    def harga(self):   
        pass  

class Tesla(MobilMewah):   
    def harga(self):   
        print("Harga mobil ini 2 Milliar Rupiah")   
class Lexus(MobilMewah):   
    def harga(self):   
        print("Harga mobil ini 3 Milliar Rupiah")  
class Ferrari(MobilMewah):   
    def harga(self):   
        print("Harga mobil ini 10 Milliar Rupiah")  

tesla_obj = Tesla()
tesla_obj.harga()

ferrari_obj = Ferrari()
ferrari_obj.harga()


# In[33]:


from abc import ABC, abstractmethod
class abs_class(abstractmethod):
    @ABC
    def abstract_methd(self):
        pass


# In[34]:


from abc import ABC, abstractmethod
class abs_class(ABC):
    @abstractmethod
    def abstract_methd(self):
        pass


# In[35]:


from abc import ABC, abstractmethod
class abs_class(abstractmethod):
    def abstract_methd(ABC):
        pass


# In[36]:


from abc import ABC, abstractmethod
class abs_class(ABC):
    def abstract_methd(abstractmethod):
        pass

