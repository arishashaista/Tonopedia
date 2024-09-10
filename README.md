## Deployment
Tautan PWS: http://arisha-shaista-tonopedia.pbp.cs.ui.ac.id

## 
**1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**  

&nbsp;&nbsp;&nbsp;**Jawab:**  
&nbsp;&nbsp;&nbsp;a. Membuat direktori lokal bernama `Tonopedia`.  
&nbsp;&nbsp;&nbsp;b. Membuat virtual environment dengan cara membuka terminal direktori dan menjalankan perintah berikut (untuk Mac OS):  
```
          python3 -m venv env
```  
&nbsp;&nbsp;&nbsp;c. Mengaktifkan virtual environment dengan perintah berikut (untuk Mac OS):  


```
source env/bin/activate
```
     d. Dalam direktori `Tonopedia`, Buat file bernama 'requirements.txt' dan tambahkan __dependencies__ berikut:  
```
django  
gunicorn  
whitenoise  
psycopg2-binary  
requests  
urllib3  
```


     e. Lakukan instalasi dengan perintah berikut dan pastikan virtual environment tetap berjalan.  
```
pip install -r requirements.txt
```


     f. Membuat proyek Django bernama `tonopedia` dengan perintah berikut.  
```
django-admin startproject tonopedia .
```


     g. Buka file `settings.py` yang ada pada direktori dan tambahkan kedua string berikut pada `ALLOWED_HOSTS`:
```
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
```




**2. Jelaskan fungsi git dalam pengembangan perangkat lunak!** </br>  

   **Jawab:** </br>  
