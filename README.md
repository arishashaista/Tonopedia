# TONOPEDIA  
Tonopedia? Klik Klik Beres!

### 📎 Deployment
Tautan PWS: http://arisha-shaista-tonopedia.pbp.cs.ui.ac.id  
  
  
### 💻 Langkah Implementasi
1. Membuat direktori lokal bernama `Tonopedia`.  
2. Membuat virtual environment dengan cara membuka terminal direktori dan menjalankan perintah berikut (untuk Mac OS):  
```bash
python3 -m venv env
```
3. Mengaktifkan virtual environment dengan perintah berikut (untuk Mac OS):  
```bash
source env/bin/activate
```
4. Membuat file bernama 'requirements.txt' dalam direktori dan menambahkan *dependencies* berikut.  
```
django  
gunicorn  
whitenoise  
psycopg2-binary  
requests  
urllib3  
```
5. Melakukan instalasi dengan perintah berikut.  
```bash
pip install -r requirements.txt
```
6. Membuat proyek Django bernama `tonopedia` dengan perintah berikut.  
```bash
django-admin startproject tonopedia .
```
7. Menambahkan kedua string berikut di `ALLOWED_HOSTS` pada berkas `settings.py` yang ada pada direktori.
```python
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
```
8. Membuat repositori GitHub baru bernama `Tonopedia` dengan visibilitas publik.  
9. Membuat berkas `.gitignore` dan isinya.  
10. Menginisiasi direktori lokal `Tonopedia` sebagai repositori git.  
11. Membuat proyek baru di `Pacil Web Service` dengan `Project Name` bernama `tonopedia`.  
12. Menambahkan `URL Deployment PWS` pada `ALLOWED_HOSTS` di `settings.py`.  
13. Membuat aplikasi baru bernama `main` dengan perintah berikut.  
```bash
python manage.py startapp main
```
14. Membuka berkas `settings.py` pada direktori `tonopedia` dan menambahkan string berikut pada `INSTALLED_APPS`.
```python
INSTALLED_APPS = [
    ...,
    'main'
]
```
15. Membuat direktori baru bernama `templates` di dalam direktori aplikasi `main`.  
16. Membuat berkas baru bernama `main.html` pada direktori `templates` dan mengisi berkas `main.html` sebagai berikut.
```django
<h1>Tonopedia</h1>

<h5>NPM:</h5>
<p>{{ npm }}</p>

<h5>Name:</h5>
<p>{{ name }}</p>

<h5>Class:</h5>
<p>{{ class }}</p>

<h5>Nama Produk:</h5>
<p>{{ product_name }}</p>

<h5>Harga:</h5>
<p>{{ price }}</p>

<h5>Deskripsi Produk:</h5>
<p>{{ description }}</p>
```
17. Mengisi berkas `models.py` pada direktori aplikasi `main` sebagai berikut.
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
```
18. Membuat migrasi model dan menerapkan migrasi ke dalam basis data lokal dengan perintah berikut.
```
python manage.py makemigrations
python manage.py migrate
```
19. Membuat fungsi pada `views.py` pada direktori `main` sebagai berikut.
```python
from django.shortcuts import render
from .models import Product

def show_main(request):
    model = Product.objects.all()
    context = {
        'npm' : '2306123456',
        'name': 'Arisha Shaista Aurelya',
        'class': 'PBP C',
        'product_name': 'Soffell',
        'price': 27000,
        'description': 'Soffell adalah penangkal nyamuk yang memiliki wangi lembut dan tidak membuat kulit kering',
    }

    return render(request, "main.html", context)
```
20. Membuat berkas `urls.py` pada direktori `main` dengan isi sebagai berikut untuk mengonfirmasi *routing* URL aplikasi `main` .
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
21. Menambahkan fungsi impor dan rute URL pada `urls.py` yang berada di direktori `tonopedia` untuk mengonfigurasi *routing* URL proyek.
```python
...
from django.urls import path, include
...
```python
urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
]
```
22. Melakukan deployment ke `Pacil Web Service` terhadap aplikasi yang sudah dibuat.
23. Melakukan `git add, commit, dan push` untuk seluruh penambahan ataupun perubahan yang ada.

  
### 🔄 Alur Django  
![Django Flow Chart](https://github.com/arishashaista/Tonopedia/blob/master/alur_bagan/bagan_request.png)  
**Penjelasan:**  
Pengguna mengirimkan permintaan melalui internet untuk mengakses halaman web. Server menerima permintaan tersebut dan memprosesnya. Kemudian, Web server bertindak sebagai perantara yang menghubungkan pengguna dengan Django. Permintaan dari website diarahkan ke urls.py yang bertugas memetakan URL ke fungsi atau kelas di views.py. Setelah URL dihubungkan, views.py menangani alur kerja aplikasi yang diperlukan. views.py berkomunikasi dengan models.py untuk mengambil atau menyimpan data ke dalam database. models.py sendiri berisi struktur dan logika yang berhubungan dengan penyimpanan data. Setelah data diproses oleh views.py, data tersebut dikirim ke berkas template HTML untuk ditampilkan kepada pengguna dalam format halaman web.  

  
### ⚙️ Fungsi Git dalam Pengembangan Perangkat Lunak
Pada pengembangan perangkat lunak, Git berfungsi untuk melacak perubahan-perubahan pada kode selama proses pengembangan. Selain itu, Git mengizinkan berbagai pengembang untuk bekerja di proyek yang sama secara serentak, dan memastikan perubahan yang dilakukan pengembang tidak memiliki konflik satu sama lain.  


### ❓ Mengapa Framework Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak?  
Django sering dijadikan pilihan untuk pembelajaran pengembangan perangkat lunak karena kemudahan penggunaannya, terutama bagi mereka yang sudah familiar dengan Python, mengingat pada mata kuliah DDP-1 mahasiswa telah diajarkan mengenai Python. Framework ini memiliki sistem template yang intuitif serta *library* aplikasi yang dapat digunakan kembali, sehingga memudahkan para pengembang untuk menambahkan fungsionalitas pada proyek mereka.  Framework ini juga dilengkapi dengan sistem penamaan untuk setiap fungsi dan komponen, serta panel admin yang lebih mudah digunakan dibandingkan framework lain. Dengan berbagai modul bawaan seperti ORM, panel admin, migrasi, dan autentikasi. Dengan demikian, Django mempercepat proses pengembangan tanpa harus memulai dari nol, menjadikannya pilihan tepat untuk permulaan pembelajaran pengembangan perangkat lunak.  


### 🔎 Mengapa Model pada Django disebut ORM?
Model Django disebut ORM (Object-Relational Mapping) karena berfungsi sebagai penghubung antara objek Python dan tabel dalam basis data relasional. Dengan ORM, pengembang dapat mengelola basis data menggunakan kode Python tanpa harus menulis kueri SQL secara langsung. ORM ini secara otomatis menerjemahkan operasi Python ke perintah SQL, sehingga memudahkan pengelolaan data, menjaga kode tetap konsisten, dan mendukung berbagai jenis relasi antar tabel, serta berbagai jenis basis data.

