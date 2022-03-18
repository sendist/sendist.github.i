# Import Package
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json

# Request ke website
page = requests.get("https://www.republika.co.id/")

# Extract konten menjadi objek BeautifulSoup
obj =  BeautifulSoup(page.text, 'html.parser')

# List kosong untuk menampung data
data = []

# Membuat file .json untuk menampung data
f = open('scraping.json', 'w')

# untuk menampung waktu publish
waktu = obj.find(class_='date')

# Loop untuk Mengambil data kategori dan judul
for kategoriDanJudul in obj.find_all('div', class_='teaser_conten1_center'):

    # mendapatkan waktu saat ini (sebagai waktu akses)
    waktuScrap = datetime.now()
    stringWaktu = waktuScrap.strftime("%d %b %Y %H:%M:%S")

    # append data
    data.append({"judul":kategoriDanJudul.find('h2').text, "kategori":kategoriDanJudul.find('h1').text, "publish":waktu.text, "scraping":stringWaktu})

    # mencari waktu publish berikutnya
    waktu = waktu.find_next(class_='date')

# dump list dictionary menjadi file json
jdumps=json.dumps(data, indent = 2)
f.writelines(jdumps)
f.close()
