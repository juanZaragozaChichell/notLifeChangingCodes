from selenium import webdriver

url = 'https://intranet.upv.es/pls/soalu/est_intranet.NI_Dual?P_CUA=wm9'
dni = 'my8DigitDNI'
pin = 'my4DigitPIN'




browser = webdriver.Edge()
browser.get(url)
userElem = browser.find_element_by_name('dni')
userElem.send_keys(dni)
userElem = browser.find_element_by_name('clau')
userElem.send_keys(pin)
loginElem = browser.find_element_by_class_name('upv_btsubmit')
loginElem.click()


# In[ ]:




