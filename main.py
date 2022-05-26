from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver_path = "C:\\Program Files\\Google\chromedriver.exe"

browser = webdriver.Chrome(driver_path)

music_name = input("Enter music name :")
artist_name = input("Enter artist name :")
print("""
site to search
Spotify
Yotube
""")
site_name = input("Type site name")


browser.get("https://www.google.com/")

enter_date = browser.find_element_by_css_selector(".gLFyf.gsfi")


enter_date.send_keys(music_name + "" + artist_name + " " +"site:{}.com".format(artist_name))
time.sleep(2)

enter_date.send_keys(Keys.ENTER)
time.sleep(2)

müzik_oynat_youtube = browser.find_element_by_xpath("//*[@id='rso']/div[2]/video-voyager/div/div/div/div[1]/a")
müzik_oynat_youtube.click()
time.sleep(200)
