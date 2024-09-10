## 📎 DEPLOYMENT
Tautan PWS: http://arisha-shaista-tonopedia.pbp.cs.ui.ac.id

## 💻 IMPLEMENTASI STEP-BY-STEP
&nbsp;&nbsp;&nbsp;1. Membuat direktori lokal bernama `Tonopedia`.  
&nbsp;&nbsp;&nbsp;2. Membuat virtual environment dengan cara membuka terminal direktori dan menjalankan perintah berikut (untuk Mac OS):  
```bash
python3 -m venv env
```
&nbsp;&nbsp;&nbsp;3. Mengaktifkan virtual environment dengan perintah berikut (untuk Mac OS):  
```bash
source env/bin/activate
```
&nbsp;&nbsp;&nbsp;4. Membuat file bernama 'requirements.txt' dalam direktori dan menambahkan *dependencies* berikut.  
```
django  
gunicorn  
whitenoise  
psycopg2-binary  
requests  
urllib3  
```
&nbsp;&nbsp;&nbsp;5. Melakukan instalasi dengan perintah berikut.  
```bash
pip install -r requirements.txt
```
&nbsp;&nbsp;&nbsp;6. Membuat proyek Django bernama `tonopedia` dengan perintah berikut.  
```bash
django-admin startproject tonopedia .
```
&nbsp;&nbsp;&nbsp;7. Menambahkan kedua string berikut di `ALLOWED_HOSTS` pada berkas `settings.py` yang ada pada direktori.
```python
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
```
&nbsp;&nbsp;&nbsp;8. Membuat repositori GitHub baru bernama `Tonopedia` dengan visibilitas publik.  
&nbsp;&nbsp;&nbsp;9. Membuat berkas `.gitignore` dan isinya.  
&nbsp;&nbsp;&nbsp;10. Menginisiasi direktori lokal `Tonopedia` sebagai repositori git.  
&nbsp;&nbsp;&nbsp;11. Membuat proyek baru di `Pacil Web Service` dengan `Project Name` bernama `tonopedia`.  
&nbsp;&nbsp;&nbsp;12. Menambahkan `URL Deployment PWS` pada `ALLOWED_HOSTS` di `settings.py`.  
&nbsp;&nbsp;&nbsp;13. Membuat aplikasi baru dengan nama main dengan perintah berikut.  
```bash
python manage.py startapp main
```
&nbsp;&nbsp;&nbsp;14. Membuka berkas `settings.py` pada direktori `tonopedia` dan menambahkan string berikut pada `INSTALLED_APPS`.
```python
INSTALLED_APPS = [
    ...,
    'main'
]
```
&nbsp;&nbsp;&nbsp;15. Membuat direktori baru bernama `templates` di dalam direktori aplikasi `main`.  
&nbsp;&nbsp;&nbsp;16. Membuat berkas baru bernama `main.html` pada direktori `templates` dan mengisi berkas `main.html` sebagai berikut.
```django
<h1>Tonopedia</h1>

<h5>NPM:</h5>
<p>{{ npm }}</p>

<h5>Name:</h5>
<p>{{ name }}</p>

<h5>Class:</h5>
<p>{{ class }}</p>
```

## ⚙️ FUNGSI GIT DALAM PENGEMBANGAN PERANGKAT LUNAK
&nbsp;&nbsp;&nbsp;Pada pengembangan perangkat lunak, Git berfungsi untuk melacak perubahan-perubahan pada kode selama proses pengembangan. Selain itu, Git mengizinkan berbagai pengembang untuk bekerja di proyek yang sama secara serentak, dan memastikan perubahan yang dilakukan pengembang tidak memiliki konflik satu sama lain.
