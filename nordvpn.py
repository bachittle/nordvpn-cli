import os 
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options           

options = Options()
options.add_argument("--headless")

browser = webdriver.Chrome(options=options)
browser.get("https://nordvpn.com/servers/tools/")

time.sleep(2) # just in case nothing loads
servername = browser.find_elements_by_class_name("Title")
servername = [x.text for x in servername]

# debug the output in case they change the site

print(servername)
print("sudo openvpn /etc/openvpn/ovpn_udp/"+servername[1]+".udp.ovpn")
os.system("sudo openvpn /etc/openvpn/ovpn_udp/"+servername[1]+".udp.ovpn")

browser.quit()