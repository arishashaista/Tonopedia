## 📎 DEPLOYMENT
Tautan PWS: http://arisha-shaista-tonopedia.pbp.cs.ui.ac.id

## 
**1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**  

&nbsp;&nbsp;&nbsp;**Jawab:**  
&nbsp;&nbsp;&nbsp;a. Membuat direktori lokal bernama `Tonopedia`.  
&nbsp;&nbsp;&nbsp;b. Membuat virtual environment dengan cara membuka terminal direktori dan menjalankan perintah berikut (untuk Mac OS):  
```bash
python3 -m venv env
```
&nbsp;&nbsp;&nbsp;c. Mengaktifkan virtual environment dengan perintah berikut (untuk Mac OS):  
<pre><code>source env/bin/activate</code></pre>  
&nbsp;&nbsp;&nbsp;d. Dalam direktori `Tonopedia`, Buat file bernama 'requirements.txt' dan tambahkan __dependencies__ berikut:  
```
django  
gunicorn  
whitenoise  
psycopg2-binary  
requests  
urllib3  
```
&nbsp;&nbsp;&nbsp;e. Lakukan instalasi dengan perintah berikut dan pastikan virtual environment tetap berjalan.  
<pre><code>pip install -r requirements.txt</code></pre>  
&nbsp;&nbsp;&nbsp;f. Membuat proyek Django bernama `tonopedia` dengan perintah berikut.  
<pre><code>django-admin startproject tonopedia .</code></pre>


     g. Buka file `settings.py` yang ada pada direktori dan tambahkan kedua string berikut pada `ALLOWED_HOSTS`:
```
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
```




## ⚙️ FUNGSI GIT DALAM PENGEMBANGAN PERANGKAT LUNAK
&nbsp;&nbsp;&nbsp;Pada pengembangan perangkat lunak, Git berfungsi untuk melacak perubahan-perubahan pada kode selama proses pengembangan. Selain itu, Git mengizinkan berbagai pengembang untuk bekerja di proyek yang sama secara serentak, dan memastikan perubahan yang dilakukan pengembang tidak memiliki konflik satu sama lain.
