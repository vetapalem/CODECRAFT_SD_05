from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

import time as tt, csv

path = Service(executable_path=r'driver file should be .exe format')

web_driver = wb.Chrome(service=path)


web_driver.maximize_window()




web_driver.get(url='domain-id ')

obj_serch = web_driver.find_element(By.XPATH,"//input[@name='q']")

obj_serch.send_keys('cloth')
obj_serch.submit()

tt.sleep(5)

a =10


tt.sleep(6)



def main():

    data= []
    try:

        for pages in web_driver.find_elements(By.CLASS_NAME,'cn\+\+Ap'):
            pages.click()
            print(web_driver.current_url)

            tt.sleep(25)


            

            cv = web_driver.find_elements(By.XPATH,'//*[@class="slAVV4"]')



            if len(cv)>0:
                axindex=0
                print(data)

                for a in cv :
                    
                    shuffle = a.find_element(By.CLASS_NAME,'Nx9bqj').text.split('₹')[1]
                    print(shuffle)

                   


                    data.append(
                       [ a.find_element(By.CLASS_NAME,'wjcEIp').get_attribute('title'),
                        shuffle,
                        a.find_element(By.CLASS_NAME,'XQDdHH').text
                        ]
                       

                    )
                    
                        

            else:
                print(len(cv))

            tt.sleep(10)
    except Exception as ep:
        print('exception',ep)
        
        with open('data.csv','w',newline="") as db:
            print('file open')

            writer = csv.writer(db)
            writer.writerows(data)
            print('updata .. data ..')

    finally:
        print('finally block')
        
        with open('data1.csv','w',newline="") as db:
            print('file open')

            writer = csv.writer(db)
            writer.writerows(data)
            print('updata .. finally block ..')




main()


tt.sleep(25)




web_driver.quit()

