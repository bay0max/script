import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://service.security.tencent.com/kingkong')
print(driver.title)
#assert "Python" in driver.title
#driver.find_element_by_name("uploadfile").click()

apkpath='D:\研一\爬虫\selenium\\apk'
files=os.listdir(apkpath)
for file in files:
    abname='D:\研一\爬虫\selenium\\apk\\'+file
    print(abname)
    driver.find_element_by_name("uploadfile").click()
    os.system('D:\研一\爬虫\selenium\\auto.exe %s' % abname)
    sleep(2)
    md5=driver.find_element_by_xpath('//*[@id="apk_modal"]/div[2]/div[1]/div[2]').text
    print(md5)
    driver.find_element_by_xpath('//*[@id="apk_modal"]/div[3]/button').click()
    sleep(1)
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)