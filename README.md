# TONOPEDIA

Tonopedia? Klik Klik Beres!

### 📎 Deployment

Tautan PWS: http://arisha-shaista-tonopedia.pbp.cs.ui.ac.id

## Tugas 2 PBP

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

4. Membuat file bernama 'requirements.txt' dalam direktori dan menambahkan _dependencies_ berikut.

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

20. Membuat berkas `urls.py` pada direktori `main` dengan isi sebagai berikut untuk mengonfirmasi _routing_ URL aplikasi `main` .

```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

21. Menambahkan fungsi impor dan rute URL pada `urls.py` yang berada di direktori `tonopedia` untuk mengonfigurasi _routing_ URL proyek.

```python
...
from django.urls import path, include
...
```

```python
urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
]
```

23. Melakukan deployment ke `Pacil Web Service` terhadap aplikasi yang sudah dibuat.
24. Melakukan `git add, commit, dan push` untuk seluruh penambahan ataupun perubahan yang ada.

### 🔄 Alur Django

![Django Flow Chart](https://github.com/arishashaista/Tonopedia/blob/master/alur_bagan/bagan_request.png)
**Penjelasan:**
Pengguna mengirimkan permintaan melalui internet untuk mengakses halaman web. Server menerima permintaan tersebut dan memprosesnya. Kemudian, Web server bertindak sebagai perantara yang menghubungkan pengguna dengan Django. Permintaan dari website diarahkan ke urls.py yang bertugas memetakan URL ke fungsi atau kelas di views.py. Setelah URL dihubungkan, views.py menangani alur kerja aplikasi yang diperlukan. views.py berkomunikasi dengan models.py untuk mengambil atau menyimpan data ke dalam database. models.py sendiri berisi struktur dan logika yang berhubungan dengan penyimpanan data. Setelah data diproses oleh views.py, data tersebut dikirim ke berkas template HTML untuk ditampilkan kepada pengguna dalam format halaman web.

### ⚙️ Fungsi Git dalam Pengembangan Perangkat Lunak

Pada pengembangan perangkat lunak, Git berfungsi untuk melacak perubahan-perubahan pada kode selama proses pengembangan. Selain itu, Git mengizinkan berbagai pengembang untuk bekerja di proyek yang sama secara serentak, dan memastikan perubahan yang dilakukan pengembang tidak memiliki konflik satu sama lain.

### ❓ Mengapa Framework Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak?

Django sering dijadikan pilihan untuk pembelajaran pengembangan perangkat lunak karena kemudahan penggunaannya, terutama bagi mereka yang sudah familiar dengan Python, mengingat pada mata kuliah DDP-1 mahasiswa telah diajarkan mengenai Python. Framework ini memiliki sistem template yang intuitif serta _library_ aplikasi yang dapat digunakan kembali, sehingga memudahkan para pengembang untuk menambahkan fungsionalitas pada proyek mereka. Framework ini juga dilengkapi dengan sistem penamaan untuk setiap fungsi dan komponen, serta panel admin yang lebih mudah digunakan dibandingkan framework lain. Dengan berbagai modul bawaan seperti ORM, panel admin, migrasi, dan autentikasi. Dengan demikian, Django mempercepat proses pengembangan tanpa harus memulai dari nol, menjadikannya pilihan tepat untuk permulaan pembelajaran pengembangan perangkat lunak.

### 🔎 Mengapa Model pada Django disebut ORM?

Model Django disebut ORM (Object-Relational Mapping) karena berfungsi sebagai penghubung antara objek Python dan tabel dalam basis data relasional. Dengan ORM, pengembang dapat mengelola basis data menggunakan kode Python tanpa harus menulis kueri SQL secara langsung. ORM ini secara otomatis menerjemahkan operasi Python ke perintah SQL, sehingga memudahkan pengelolaan data, menjaga kode tetap konsisten, dan mendukung berbagai jenis relasi antar tabel, serta berbagai jenis basis data.

## Tugas 3 PBP

### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

**Jawaban**:

Data delivery adalah komponen esensial dalam implementasi platform karena menghubungkan berbagai bagian sistem, memastikan aliran data yang lancar dan aman antara server, pengguna, dan interface. Tanpa sistem data delivery yang efektif, elemen-elemen dalam platform akan terpisah, mengakibatkan gangguan pada fungsionalitas dan kinerja platform. Selain itu, mekanisme data delivery yang baik mendukung kemampuan platform untuk berkembang, beradaptasi dengan kebutuhan yang berubah, dan mengelola peningkatan volume data dengan efisien.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

**Jawaban**:

JSON lebih populer dibandingkan XML sebagai format pertukaran data karena kesederhanaannya, ukuran file yang lebih kecil, dan kecepatan parsing yang lebih tinggi. JSON menggunakan sintaks yang lebih sederhana tanpa memerlukan tag pembuka dan penutup, serta memiliki struktur data yang fleksibel, mirip dengan objek dan array dalam JavaScript. Selain itu, JSON menghasilkan file yang lebih kecil dan dapat diparsing dengan cepat, serta banyak digunakan dalam API modern karena kemudahan integrasinya. Keunggulan-keunggulan ini menjadikannya pilihan utama dalam banyak aplikasi web dan sistem pertukaran data. Oleh karena itu, JSON sering dianggap lebih baik daripada XML untuk banyak aplikasi web dan pertukaran data.

### 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

**Jawaban**:

Method `is_valid()` dalam form Django memainkan peran krusial dalam memvalidasi data yang dimasukkan oleh pengguna. Fungsinya adalah untuk memastikan bahwa data yang dikirim melalui form memenuhi semua kriteria validasi yang telah ditentukan, seperti pengisian field yang wajib dan format data yang benar. Method ini akan mengembalikan True jika data valid dan False jika tidak. Selain itu, jika ada kesalahan, form.errors akan diisi dengan pesan yang menjelaskan kesalahan tersebut. Dengan demikian, method `is_valid()` membantu mencegah data yang tidak sesuai atau berpotensi berbahaya dari masuk ke dalam sistem, menjaga integritas aplikasi, dan memberikan umpan balik yang konstruktif kepada pengguna.

### 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

**Jawaban**:

Cross-Site Request Forgery (CSRF) Token adalah mekanisme keamanan yang penting untuk melindungi aplikasi web dari serangan CSRF. Token ini memastikan bahwa permintaan POST yang diterima oleh server berasal dari situs yang sah, sehingga mencegah modifikasi data yang tidak sah melalui permintaan palsu. Dengan adanya csrf_token, aplikasi dapat memastikan bahwa permintaan yang dikirim benar-benar berasal dari situs yang sah dan melindungi data serta informasi pribadi pengguna dari modifikasi yang tidak sah.

Tanpa csrf_token, penyerang dapat membuat situs web berbahaya atau memodifikasi situs yang sudah ada, lalu pengguna yang telah login ke aplikasi Django mungkin tanpa sadar mengunjungi situs berbahaya tersebut. Situs berbahaya tersebut dapat memuat form tersembunyi yang mengirimkan permintaan ke aplikasi Django, memanfaatkan cookies sesi yang valid dari pengguna. Karena server tidak dapat membedakan antara permintaan yang sah dan yang palsu tanpa token ini, permintaan palsu akan tampak sah.

Django menghasilkan token unik untuk setiap sesi pengguna, yang disertakan dalam setiap form sebagai field tersembunyi. Saat form disubmit, Django memeriksa kecocokan token tersebut. Jika token yang diterima berbeda dari yang diharapkan, permintaan akan ditolak. Dengan cara ini, CSRF token membantu menjaga keamanan aplikasi dengan memastikan bahwa hanya permintaan yang sah dan berasal dari sesi pengguna yang terotentikasi yang dapat memodifikasi data atau melakukan tindakan.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

**Jawaban**:

1.  Membuat direktori `templates` pada direktori utama dan isi direktori tersebut dengan `base.html` sebagai berikut untuk membuat kerangka umum.

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```

2.  Menambahkan kode berikut pada `tonopedia/settings.py/` :

```
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
        'APP_DIRS': True,
        ...
    }
]
...
```

3.  Mengubah `main.html` pada `main/templates/` sebagai berikut.

```
{% extends 'base.html' %} {% block content %}
<h1>Tonopedia</h1>

<h5>NPM: {{ npm }}</h5>

<h5>Name: {{ name }}</h5>

<h5>Class: {{ class }}</h5>

{% endblock content %}
```

4.  Menambahkan atribut `time` dan `id` pada `models.py` dan melakukan migrasi model.

```
from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
```

5.  Membuat `forms.py` pada direktori `main` untuk kebutuhan input dari user.

```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
```

6.  Menambahkan import pada `main/views.py/` sebagai berikut.

```python
from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
```

7.  Membuat fungsi untuk menambahkan produk baru.

```python
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```

8.  Menambahkan kode berikut pada fungsi `show_main`.

```python
    context = {
        ...
        'product_entries': model,
        ...
    }
```

9.  Membuka `urls.py` pada direktori `main` dan import fungsi `create_product_entry`.

```python
from main.views import show_main, create_product_entry
```

10. Menambahkan path URL ke dalam variabel `urlpatterns` pada `main/urls.py/`.

```python
urlpatterns = [
    ...
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    ...
]
```

11. Membuat berkas HTML baru dengan nama `create_proudct_entry.html` pada direktori `main/templates` dan isi dengan kode berikut.

```html
{% extends 'base.html' %} {% block content %}
<h1>Add New Product Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add New Product" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```

12. Membuka `main.html` dan tambahkan kode berikut.

```html
{% if not product_entries %}
<p>Belum ada produk yang diunggah.</p>
{% else %}
<table>
  <tr>
    <th>Name</th>
    <th>Price</th>
    <th>Description</th>
  </tr>

  {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini
  {%endcomment %} {% for product_entry in product_entries %}
  <tr>
    <td>{{product_entry.name}}</td>
    <td>{{product_entry.price}}</td>
    <td>{{product_entry.description}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_product_entry' %}">
  <button>Add New Product</button>
</a>
{% endblock content %}
```

13. Membuka `main/views.py/` dan menambahkan import sebagai berikut.

```python
from django.http import HttpResponse
from django.core import serializers
```

14. Membuat `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id` untuk menampilkan respons dari input user.

```python
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

### Dokumentasi Postman

#### JSON

![JSON](https://github.com/arishashaista/Tonopedia/blob/master/hasil_postman/json.png)

#### XML

![XML](https://github.com/arishashaista/Tonopedia/blob/master/hasil_postman/xml.png)

#### JSON_ID

![JSON_ID](https://github.com/arishashaista/Tonopedia/blob/master/hasil_postman/json_id.png)

#### XML_ID

![XML_ID](https://github.com/arishashaista/Tonopedia/blob/master/hasil_postman/xml_id.png)
