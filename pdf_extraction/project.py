from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pdf_extract

# option=Options()
# option.add_argument("--headless")
arr=pdf_extract.extract("mypdf.pdf")
count=0
for links in arr:
    for link in links:
        # driver=Chrome(executable_path="/home/tharikh/web_crawl_projects/pdf_extraction/chromedriver")#chrome_options=option)
        # driver.get(link)
        # driver.find_element_by_xpath('//*[@id="main-content"]/article[1]/div/div/div[2]/div/div/a').click()
        print(link)
        count+=1
print count
