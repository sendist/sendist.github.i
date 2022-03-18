from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://myanimelist.net/topanime.php")

for anime in driver.find_elements_by_class_name("ranking-list"):
    print(anime.text)
    for img in anime.find_elements_by_tag_name("img"):
        print(img.get_attribute("src"))
driver.quit()
