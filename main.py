from string import capwords
from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import math

driver = webdriver.Chrome(ChromeDriverManager().install())

#driver.maximize_window()
driver.get("https://edalnice.cz/en/bulk-purchase/index.html#/multi_eshop/batch")

df = pd.read_csv('sample.csv')


for i in range((df.shape[0])-1):
    country= driver.find_element_by_id('react-select-2-input')
    country.send_keys(df['Country'].iloc[i])
    time.sleep(5)
    country.send_keys(Keys.RETURN)

    date = driver.find_element_by_id('valid-since-input')
    date.send_keys(df['Validity Begins'].iloc[i])
    date.send_keys(Keys.RETURN)

    license = driver.find_element_by_class_name('flex-grow-1')
    license.send_keys(df['License Plate'].iloc[i])
    license.send_keys(Keys.RETURN)

    try:
        if math.isnan(df['Powered by'].iloc[i]) == True:
            continue
    except:
        checkbox = driver.find_element_by_xpath(".//*[@data-testid='eco-fuel-type-check']").click()
        time.sleep(2)
        if df['Powered by'].iloc[i] == 'Natural Gas':
            natural_gas = driver.find_element_by_xpath(".//*[@option='NATURAL_GAS']").click()
        elif df['Powered by'].iloc[i] == 'Biomethane':
            biomethane =  driver.find_element_by_xpath(".//*[@option='BIO_METHANE']").click()

    addbatch = driver.find_element_by_xpath("//button[@class ='kit__button   btn btn-danger']")
    addbatch.send_keys(Keys.RETURN)
time.sleep(10)

continue_button1 = driver.find_element_by_xpath("//*[@class = 'kit__button  w-100 btn btn-primary']").click()
time.sleep(3)
continue_button2 = driver.find_element_by_xpath("//*[@class = 'kit__button  w-100 btn btn-primary']").click()
time.sleep(3)

#payment 
email = driver.find_element_by_id('email-input')
email.send_keys('sample@gmailcom')

email_conformation = driver.find_element_by_id('email-confirmation-input')
email_conformation.send_keys('sample@gmailcom')

via_card =  driver.find_element_by_id('card_payment_radio_array_option')

terms_payment_checkbox = driver.find_element_by_id('_termsAgreement-true').click()
time.sleep(5)

card_no = driver.find_element_by_id('cardnumber')
card_no.send_keys('5422000180911025')

card_validity = driver.find_element_by_id('expiry')
card_validity.send_keys('05/25')

cvv = driver.find_element_by_id('cvc')
cvv.send_keys('913')

pay = driver.find_element_by_id('pay-submit').click()

driver.quit()








