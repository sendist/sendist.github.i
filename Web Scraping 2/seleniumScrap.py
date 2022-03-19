from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import json

# Buka web driver dan membuat objek driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&ref_=adv_prv")

topMovie= []

k = 1

# Loop sampai 1000 data
while k <= 1000:

    # Mendapatkan fiel director
    directors = driver.find_elements(By.XPATH, "//p[@class='']")
    counter = 0

    # Auto Scroll page
    total_height = int(driver.execute_script("return document.body.scrollHeight"))

    for i in range(1, total_height, 45):
        driver.execute_script("window.scrollTo(0, {});".format(i))

    # Loop untuk mendapatkan field dengan class "lister-item"
    for movie in driver.find_elements_by_class_name("lister-item"):

        # mendapatkan waktu saat ini (sebagai waktu akses)
        waktuScrap = datetime.now()
        stringWaktu = waktuScrap.strftime("%d %b %Y %H:%M:%S")

        # menampilkan nomor urutan sebagai indikasi scraping berhasil
        print(movie.text.split("\n")[0].split(".")[0] + "\n")

        # Loop mendapatkan source image 
        for img in movie.find_elements_by_class_name("loadlate"):

            # Append data ke variabel topMovie
            topMovie.append({"No": movie.text.split("\n")[0].split(".")[0],
                                "Judul": movie.find_element_by_class_name("lister-item-content").find_element_by_class_name("lister-item-header").find_element_by_tag_name("a").text,
                                "Rilis": movie.find_element_by_class_name("lister-item-year").text.translate(str.maketrans({'(': '', ')':''})),
                                "Genre": movie.find_element_by_class_name("genre").text,
                                "Durasi": movie.find_element_by_class_name("runtime").text,
                                "Rating": movie.find_element_by_tag_name('strong').text,
                                "Votes": movie.find_element_by_name('nv').text,
                                "Direktur": directors[counter].text.split(":")[1].split("|")[0],
                                "Image": img.get_attribute("src"),
                                "Scraping": stringWaktu})

            # increment
            counter = counter + 1
            k = k+1
    
    # Klik next page
    try: 
        driver.find_element(By.CLASS_NAME, "next-page").click()
    except NoSuchElementException:
        break

# Membuka file (membuat jika file tidak ada)
hasilScraping = open("Web Scraping 2/topMovie.json", "w")
# Dump data pada variabel topMovie ke dalam file .json
json.dump(topMovie, hasilScraping, indent = 2)

# Tutup file dan objek driver
hasilScraping.close()
driver.quit()