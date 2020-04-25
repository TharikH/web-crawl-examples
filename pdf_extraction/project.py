from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pdf_extract

option=Options()
# option.add_argument("--headless")
arr=pdf_extract.extract("mypdf.pdf")
link=arr[0][3]
for links in arr:
    for link in links:
        driver=Chrome(executable_path="/home/tharikh/web_crawl_projects/pdf_extraction/chromedriver")#chrome_options=option)
        driver.get(link)
        parent=driver.current_window_handle
        driver.find_element_by_class_name("test-bookpdf-link").click()
        driver.implicitly_wait(15)
        allgui=driver.window_handles;
        for guid in allgui:
            if(guid!=parent):
                driver.switch_to_window(guid);
                driver.find_element_by_id("download").click();
                driver.send_keys(u'\ue007')
                driver.implicitly_wait(10)
                driver.close()
                driver.switch_to_window(parent);
        driver.close()


# driver=Chrome(executable_path="/home/tharikh/web_crawl_projects/pdf_extraction/chromedriver")#chrome_options=option)          #for single link
# driver.get(link)
# driver.find_element_by_class_name("test-bookpdf-link").click()
# parent=driver.current_window_handle
# driver.implicitly_wait(30)
# allguid=driver.window_handles;
# for guid in allguid:
#     if(guid!=parent):
#         driver.switch_to_window(guid);
#         driver.find_element_by_id("download").click();
#         driver.send_keys(u'\ue007')
#         driver.implicitly_wait(10)
#         driver.close()
#         driver.switch_to_window(parent);
# driver.close()