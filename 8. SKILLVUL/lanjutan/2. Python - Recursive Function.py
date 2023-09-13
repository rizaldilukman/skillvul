#!/usr/bin/env python
# coding: utf-8

# ## Recursive Function 

# Recursive function adalah function yang memanggil dirinya sendiri di dalam suatu function. Rekursi adalah teknik pemecahan masalah yang sangat berguna dan cukup sering dipakai dalam pembuatan program. Recursive function dapat secara intuitif dan sederhana memecahkan masalah yang sulit diselesaikan dengan teknik prosedural. Contoh yang sering dipakai dalam recursive function adalah faktorial, dimana ekspresi faktorial dan definisi : n! = n * (n – 1)!, jika n <= 1 : return 1

# ![recursive_function.jpg](attachment:recursive_function.jpg)

# Alur fungsi rekursif faktorial adalah sebagai berikut. faktorial(3) mengembalikan 3 * faktorial(2) dan faktorial(2), mengembalikan2 * faktorial(1). Kemudian hal ini terjadi secara berulang dan hasil pengembaliannya adalah 120 seperti contoh di bawah ini.

# ![recursive_function_2.jpg](attachment:recursive_function_2.jpg)

# Contoh penggunaan recursive function yang paling umum ditemukan adalah dari konsep factorial. Dimana konsep factorial bisa didefinisikan sebagai 1! = 1, n! = n*(n-1)! Dan jika ini diimplementasikan sebagai recursive function dalam Python, maka dapat dinyatakan sebagai berikut:

# In[9]:




def factorial(n): # membuat function untuk factorial
  if n <= 1: # untuk melakukan termination/pemutusan recursive function
    return 1
  else:
    return n * factorial(n-1) # implementasi dari recursive function 

n = 5
print(f"factorial dari {n} adalah {factorial(n)}")


# Poin kunci dalam recursive function adalah ketika program berakhir. Menurut definisi, 1! = 1, sehingga ketika nilai n adalah satu atau kurang, kita tidak perlu mengulangi untuk mengeksekusi function dan saat itu recursive function berakhir.

# In[11]:


def is_palindrome(word):
    if len(word) <=1:
        return True
    if word[0] !=word[-1]:
        return False
    return is_palindrome(word[1:-1])
str1 = "Hello"
if is_palindrome(str1):
    print("Palindrome")
else:
    print("Not a palindrome")

