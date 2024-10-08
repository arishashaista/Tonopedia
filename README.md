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

## Tugas 4 PBP

### 1. Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`?

**Jawaban**:

- Ketika menggunakan `HttpResponseRedirect()`, diperlukan untuk menyebutkan URL tujuan secara eksplisit. Sementara, ketika menggunakan `redirect()`, fungsi ini dapat menerima URL, nama view, atau objek model sebagai argumen, dan akan membangun URL yang sesuai sehingga lebih fleksibel dan mudah dibaca.

### 2. Jelaskan cara kerja penghubungan model Product dengan User!

**Jawaban**:

- Model `Product` dengan `User` di Django bekerja melalui `ForeignKey`. Cara menghubungkan model `Product` dengan `User` adalah dengan mengaitkan setiap entri produk yang dibuat oleh pengguna dengan user yang sedang login. `ForeignKey` digunakan untuk membangun relasi satu-ke-banyak antara `Product` dan `User`. Artinya, seorang user dapat memiliki banyak entri produk. Selain itu, parameter `on_delete=models.CASCADE` berfungsi untuk menghapus semua entri produk yang terkait jika user tersebut dihapus dari sistem.

- Contoh:

```python
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

**Jawaban**:

- Authentication (Otentikasi) adalah proses memverifikasi identitas pengguna menggunakan kredensial seperti username dan password, untuk memastikan bahwa pengguna adalah orang yang berwenang.
- Authorization (Otorisasi) adalah proses menentukan hak akses pengguna setelah terautentikasi, yaitu menentukan apa yang diizinkan untuk dilakukan oleh pengguna di dalam sistem, seperti mengakses atau mengubah data.
- Implementasi di Django: Django menangani otentikasi dengan sistem bawaan `(django.contrib.auth)` menggunakan fungsi seperti `authenticate()` dan `login()`. Sementara, otorisasi diatur menggunakan izin (permissions) dan grup. Django memeriksa izin pengguna, misalnya dengan `user.has_perm()`, untuk menentukan tindakan yang diizinkan bagi pengguna yang telah terautentikasi.

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

**Jawaban**:

- Django mengingat pengguna yang telah login dengan menggunakan cookies dan session. Setelah login, Django menyimpan session ID di cookie pada browser pengguna, yang dikirim kembali ke server di setiap permintaan untuk mengidentifikasi pengguna tanpa perlu login lagi.
- Kegunaan lain dari cookies adalahmMenyimpan preferensi pengguna, personalisasi konten, melacak aktivitas pengguna untuk analitik, dan menyimpan data sementara seperti keranjang belanja.
- Tidak semua cookies aman. Cookies rentan terhadap serangan jika tidak diatur dengan baik. Secure cookies hanya dikirim melalui HTTPS, dan HttpOnly cookies mencegah akses dari JavaScript, sehingga lebih aman Cookies bisa disalahgunakan melalui serangan seperti session hijacking atau CSRF, tetapi Django memiliki mekanisme seperti CSRF tokens untuk melindungi dari risiko ini.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).

**Jawaban**:</br>

1. Menambahkan import `UserCreationForm` dan `messages` pada `main/views.py`.
2. Membuat dan menambahkan fungsi untuk register.
3. Membuat berkas baru bernama `register.html` pada direktori `main/templates` untuk membuat halaman Register.
4. Import fungsi `register` pada `main/urls.py` dan tambahkan _path url_ ke dalam `urlpatterns`.
5. Membuat fungsi untuk logout yaitu `logout_user` dan import `logout` pada `main/views.py`
6. Menambahkan potongan kode ini pada `main/templates/main.html`.

```html
...
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
...
```

7. Import fungsi `logout_user` dan menambahkan _path url_ dalam `urlpatterns` untuk mengakses fungsi di `main/urls.py`.
8. Merestriksi akses halaman main dengan cara menambahkan import `login_required` pada `main/views.py` dan menambahkan potongan kode berikut di atas fungsi `show_main`.

```python
@login_required(login_url='/login')
```

9. Menambahkan import berikut pada `main/views.py`.

```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

10. Mengganti kode yang ada pada blok `if form.is_valid()` menjadi potongan kode berikut pada fungsi `login_user`.

```python
...
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```

11. Menambahkan potongan kode berikut pada fungsi `show_main` bagian `context`.

```python
context = {
    ...
    'last_login': request.COOKIES['last_login'],
}
```

12. Mengubah fungsi `logout_user` menjadi sebagai berikut.

```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

13. Menambahkan potongan kode berikut pada `main/templates/main.html`.

```html
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

14. Import `from django.contrib.auth.models import User` pada `main/models.py` kemudian menambahkan `user = models.ForeignKey(User, on_delete=models.CASCADE)` pada model `Product`.
15. Mengubah kode di fungsi `create_product_entry` pada `main/views.py`sebagai berikut.

```python
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```

16. Mengubah value dari `model` dan `context` pada fungsi `show_main` menjadi seperti berikut.

```python
def show_main(request):
    model = MoodEntry.objects.filter(user=request.user)

    context = {
         'name': request.user.username,
         ...
    }
...
```

17. Menyimpan seluruh perubahan dengan melakukan `makemigrations` dan `migrate`.
18. Menambahkan `import os` pada `tonopedia/settings.py` dan mengganti variabel `DEBUG` menjadi seperti berikut.

```
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```
## Tugas 5 PBP
### 1.  Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
**Jawaban**:</br>
Urutan prioritas pengambilan CSS selector terlebih dahulu adalah:
1.  Inline Styles</br>
Gaya yang ditulis langsung pada atribut style di dalam elemen HTML memiliki prioritas tertinggi.
```html
<div style="color: blue;">Teks ini berwarna biru</div>
```
2. Selector ID</br>
Selector yang menggunakan ID `#id` memiliki prioritas lebih tinggi dibandingkan kelas, atribut, atau selector elemen.

```css
#header {
  background-color: yellow;
}
```
3. Selector dengan Kelas, Atribut, dan Pseudo-Kelas</br>
Selector yang menggunakan kelas (.class), atribut ([type="text"]), atau pseudo-kelas (:hover) memiliki prioritas sedang.

```css
.button {
  padding: 10px;
}

input[type="text"] {
  border: 1px solid #ccc;
}

a:hover {
  text-decoration: underline;
}
```
4. Selector Elemen dan Pseudo-Elemen</br>
Selector yang menggunakan nama elemen (div, p, h1, dll.) atau pseudo-elemen (::before, ::after) memiliki prioritas terendah.

```css
p {
  font-size: 16px;
}

h1::after {
  content: "!";
}
```
</br>

5. Selector Universal dan Kombinator</br>
Selector universal (`*`) dan kombinator seperti descendant (` `), child (`>`), adjacent sibling (`+`), dan general sibling (`~`) memiliki prioritas yang sangat rendah dan biasanya tidak mempengaruhi spesifisitas secara signifikan.
```css
* {
  margin: 0;
  padding: 0;
}

div p {
  line-height: 1.5;
}
```
6. Aturan `!important` </br>
Jika sebuah aturan CSS menggunakan `!important`, aturan tersebut akan memiliki prioritas tertinggi dan akan mengesampingkan aturan lain, kecuali ada aturan `!important` lain dengan spesifisitas yang lebih tinggi.

```css
p {
  color: red !important;
}

#intro p {
  color: blue;
}

```

### 2.   Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
**Jawaban**:</br>
Responsive Design adalah pendekatan desain web yang memastikan tampilan dan fungsionalitas situs web menyesuaikan secara optimal dengan berbagai ukuran layar dan perangkat. Hal ini sangat penting untuk mengakomodasi berbagai perangkat, meningkatkan pengalaman pengguna, optimasi SEO, dan efisiensi pengembangan juga pemeliharaan.</br>

- Contoh Aplikasi yang Menerapkan Responsive Design:
Twitter, Instagram, Traveloka.

- Contoh Aplikasi yang Belum Menerapkan Responsive Design: SiakNG

### 3.  Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
**Jawaban**:</br>
-  **Margin** adalah ruang di luar batas (border) elemen. Ia menciptakan jarak antara elemen tersebut dengan elemen lainnya di sekitarnya.</br>
- **Border** adalah garis yang mengelilingi padding dan konten elemen. Border dapat memiliki berbagai gaya, warna, dan ketebalan.
- **Padding** adalah ruang di dalam border elemen, antara border dan konten elemen itu sendiri. Padding memberikan ruang internal agar konten tidak terlalu berdekatan dengan border.
-  **Contoh Implementasi:**
```css
.element {
  margin: 10px;
  border: 2px;
  padding-top: 5px;
}
```

### 4.  Jelaskan konsep flex box dan grid layout beserta kegunaannya!
**Jawaban**:</br>
- **Flepbox**
    - Flepbox adalah modul layout CSS yang dirancang untuk menyusun, mengatur, dan mendistribusikan ruang di antara item dalam sebuah container, bahkan ketika ukuran mereka tidak diketahui atau dinamis. Flexbox bekerja pada satu dimensi, baik sebagai baris (horizontal) maupun kolom (vertikal).
    - Kegunaan Flexbox:
        - Penyusunan Satu Dimensi
        - Responsivitas
        - Penyesuaian Otomatis
        - Alignment dan Justification
- **Grid Layout**
    - Grid Layout adalah sistem layout CSS dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom secara bersamaan. Grid sangat cocok untuk membuat tata letak kompleks yang membutuhkan kontrol yang lebih presisi terhadap posisi dan ukuran elemen.
    - Kegunaan Grid Layout:
        - Tata Letak Dua Dimensi
        - Desain Kompleks
        - Penempatan Elemen yang Presisi
        - Responsivitas yang Tinggi

### 5.   Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
**Jawaban**:</br>
1. Menghubungkan tailwind ke aplikasi pada `templates/base.html`.
2. Menambahkan fitur `edit_product` dan `delete_product` sehingga User dapat menghapus atau menyunting produk yang telah dibuat.
3. Membuat navigation bar pada `templates/navbar.html` untuk aplikasi.
4. Mengonfigurasi static files di `settings.py` dengan cara:
    - Menambahkan middleware WhiteNoise
    ```python
    MIDDLEWARE = [
    ...
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    ...
    ]
    ```
    - Memastikan variabel `STATIC_ROOT`, `STATICFILES_DIRS`, dan `STATIC_URL` dikonfigurasikan seperti ini.
    ```python
    STATIC_URL = '/static/'
    if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static' 
    ]
    else:
    STATIC_ROOT = BASE_DIR / 'static'
    ```
5. Membuat file `global.css` pada `static/css` dan menghubungkannya ke `base.html`.
6. Menambahkan custom styling ke `global.css`.
7. Melakukan styling pada halaman Login, Register, Home, Create Product, Edit Product, dan lainnya yang membutuhkan styling.

## Tugas 6 PBP
### 1.  Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
Berikut beberapa manfaat dari penggunaan JavaScript:
- **Interactivity**: Memungkinkan pembuatan elemen interaktif seperti menu dropdown, slider, dan animasi untuk meningkatkan pengalaman pengguna.
-   **Client Side Processing**: Mengurangi beban server dengan melakukan validasi form dan manipulasi data di sisi klien, sehingga meningkatkan efisiensi aplikasi.
- **Rich Ecosystem**: Tersedia banyak framework dan library populer seperti React, Angular, dan Vue.js yang mempermudah pengembangan aplikasi kompleks.
- **Compatibility**: Didukung oleh semua browser modern, memastikan aplikasi web dapat diakses oleh berbagai pengguna tanpa masalah kompatibilitas.
- **Asynchronous Programming**: Mendukung teknik seperti AJAX dan Fetch API untuk melakukan permintaan data tanpa perlu memuat ulang halaman, memungkinkan aplikasi yang lebih dinamis dan responsif.

### 2.  Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?
Fungsi penggunaan `await` ketika menggunakan `fetch()`:
- **Menunggu Resolusi Promise**: `await` menghentikan eksekusi kode hingga Promise dari `fetch()` selesai, memungkinkan akses data yang siap digunakan.
- **Sintaks yang Lebih Bersih**: `await` membuat kode asinkron lebih mudah dibaca dan dipahami, mirip dengan kode sinkron dibandingkan penggunaan `.then()`.
- **Pengelolaan Error yang Lebih Mudah**: `await` memungkinkan penggunaan blok `try...catch` untuk menangani error secara langsung dan jelas.</br>

Konsekuensi tidak menggunakan `await`:
- **Kode Lebih Kompleks dan Sulit Dibaca**: Penggunaan banyak `.then()` membuat kode bertingkat dan sulit diikuti, terutama untuk operasi asinkron berantai.
- **Pengelolaan Error Kurang Efisien**: Menangani error dengan `.catch()` kurang intuitif dibandingkan menggunakan blok `try...catch.`
- **Eksekusi Tidak Sinkron**: Tidak dapat menunggu hasil operasi asinkron sebelum melanjutkan kode berikutnya, yang bisa menyebabkan masalah saat data diperlukan untuk langkah selanjutnya.

### 3.  Mengapa kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX `POST`?
- Decorator `csrf_exempt` digunakan pada view AJAX POST untuk mengabaikan pengecekan `csrf_token`, sehingga memudahkan pengiriman data melalui AJAX namun meningkatkan risiko terhadap serangan CSRF.

### 4.  Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
- Meskipun validasi di frontend penting untuk meningkatkan pengalaman pengguna dan memberikan umpan balik instan, pembersihan dan validasi data di backend adalah esensial untuk memastikan keamanan, integritas, dan konsistensi data. Mengandalkan hanya frontend akan meninggalkan aplikasi rentan terhadap berbagai ancaman dan masalah data, sehingga praktik terbaik adalah menerapkan validasi di kedua sisi untuk perlindungan yang komprehensif.

### 5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. Menambahkan kedua impor berikut pada file `views.py`.
```python
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
```   
2. Membuat fungsi baru pada `views.py` dengan nama `add_product_entry_ajax` yang menerima parameter request seperti berikut.
```python
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))  
    description = strip_tags(request.POST.get("description"))  
    price = request.POST.get("price")
    user = request.user

    new_product = Product(
        name=name, 
        price=price,
        description=description,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
```
3. Menambahkan routing untuk fungsi `add_product_entry_ajax` di `urls.py`.
4. Menghapus dua baris berikut pada `views.py`.
```python
product_entries = Product.objects.filter(user=request.user)
```
```python
'product_entries': product_entries,
```
5. Mengubah baris pertama views untuk `show_json` dan `show_xml` seperti berikut.
```python
data = Product.objects.filter(user=request.user)
```
6. Mengapus bagian block conditional `product_entries` untuk menampilkan `card_product` ketika kosong atau tidak pada `main.html` dan menambahkan kode berikut.
```html
<div id="product_entry_cards"></div>
```
7. Membuat *block* `<script>` di bagian bawah berkas `main.html` (sebelum `{% endblock content %}`) dan membuat fungsi baru pada block `<script>` tersebut dengan nama `getProductEntries` serta `refreshProductEntries`.
8. Menambahkan kode dibawah `div` dengan `id` `product_entry_cards` untuk mengimplementasikan modal (*Tailwind*) pada aplikasi dan menambahkan fungsi-fungsi JavaScript berikut.
10. Mengubah bagian tombol `Add New Product Entry` dan menambahkan tombol baru untuk melakukan penambahan data dengan AJAX.
11. Membuat fungsi baru pada block `<script> `dengan nama `addProductEntry`.
12. Menambahkan `strip_tags` untuk membersihkan data baru dan membersihkan data dengan DOMPurify​.




