# from bs4 import BeautifulSoup
# from soup2dict import convert
import pickle
from selenium.webdriver.common.by import By
import requests
import time
import undetected_chromedriver as uc
import json




def complete_only_text(forms):
    print('THIS FUNCTION RUNS')
    url = 'https://1cef-35-230-104-156.ngrok-free.app'+'/api'
    

    load_inputs=[]
    load_instructions=[]
    for form in forms:
        
        try:
            # print('before')
            load_inputs.append(form.find_element(By.TAG_NAME,"input"))
            # print('after')
            load_instructions.append([form.find_element(By.TAG_NAME,"label").text,form.find_element(By.TAG_NAME,"span").text])
            # print('uberafter')
        except Exception as e:
            print('this error')
            print(e)
            # time.sleep(1000000)
            return False
    counter=0
    for i in load_instructions:
       
        myobj = {
        "data": [i]
        }
        x = requests.post(url, json = myobj)
        print('or here')
        print(x.json())
        load_inputs[counter].send_keys(x.json()["prediction"])
        counter+=1
        # except Exception as e:
        #     print('what happened with api')
        #     print(e)
        #     print(x.text)
        #     time.sleep(1000000)
    
    # time.sleep(1000000)
        
        
        




# html = form.get_attribute('innerHTML')

    # soup = BeautifulSoup(html,'lxml')
    # print(soup.prettify())
    # html_to_dict=convert(soup)
    # with open('html_to_dict.pkl', 'wb') as fp:
    #     pickle.dump(html_to_dict, fp)