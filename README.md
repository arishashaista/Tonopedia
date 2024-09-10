## Deployment
Tautan PWS: http://arisha-shaista-tonopedia.pbp.cs.ui.ac.id

## Pertanyaan dan Jawaban
**1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).** </br>  
   
   **Jawab:** </br>
     a. Membuat direktori lokal bernama `Tonopedia`. </br>
     b. Membuat virtual environment dengan cara membuka terminal direktori dan menjalankan perintah berikut (untuk Mac OS): </br>
        ```
        python3 -m venv env
        ```
     c. Mengaktifkan virtual environment dengan perintah berikut (untuk Mac OS): </br>
        ```
        source env/bin/activate
        ```
     d. Dalam direktori `Tonopedia`, Buat file bernama 'requirements.txt' dan tambahkan __dependencies__ berikut: </br>
        ```
        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3
        ```
     e. 
