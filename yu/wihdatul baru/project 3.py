# import Modul
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# fungsi untuk mengirim email
def kirim_email(pengirim, penerima, subject, html_content):
    # konfigurasi server SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(pengirim, 'kqnm gylw nmhx clxy')  # Pastikan ini adalah sandi atau token aman
    
    # membuat object email
    msg = MIMEMultipart()
    msg['From'] = pengirim
    msg['To'] = penerima
    msg['Subject'] = subject

    # menyisipkan konten HTML ke dalam email
    msg.attach(MIMEText(html_content, 'html'))

    # mengirim email
    server.send_message(msg)
    server.quit()

# membuat template HTML untuk email
html_template = """
<html>
<head>
  <title>Sistem Email Otomatis</title>
  <style>
  body {
    font-family: Arial, sans-serif;
    color: #333;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
  }
  .container {
    width: 100%;
    max-width: 600px;
    margin: 0 auto;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border: 1px solid #ddd;
  }
  h1 {
    font-size: 24px;
    color: #333;
    margin-bottom: 10px;
    text-align: center;
  }
  .button-container {
    text-align: center;
    margin-top: 20px;
    color: white;
  }
  .button {
    background-color: #6a0dad;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
    font-size: 16px;
    display: inline-block;
    color: white;
  }
  .button:hover {
    background-color: #5a0bb5;
  }
  .footer {
    font-size: 14px;
    color: #888;
    text-align: center;
    margin-top: 20px;
  }
  </style>
</head>
<body>
  <div class="container">
    <h1>Mencoba Sistem Email Otomatis</h1>
    <p>Ini adalah pengirim email otomatis menggunakan python</p>
    <div class="button-container">
      <a href="#" class="button">pelajari lebih lanjut</a>
    </div>
    <div class="footer">
      &copy; 2024 Hak Cipta dilindungi.
    </div>
  </div>
</body>
</html>
"""

# menggunakan fungsi untuk mengirim email
pengirim = 'maulazuhroidawihdatul@gmail.com'
penerima = 'sadiyahrpl@gmail.com'
subject = 'Wihdatul Maula Zuhroida/36'
kirim_email(pengirim, penerima, subject, html_template)
print('Email berhasil terkirim!')
