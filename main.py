import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

#YUANCON CONTROLLERS
nostock = "Stock: 0"
#YUANCON SDVX
def yuan_sdvx():
    driver.get('https://yuancon.store/controller/sdvx')
    yc = driver.find_elements_by_tag_name('h4')[0].text
    if yc == nostock:
        print("Yuancon SDVX controller OUT OF STOCK")
    else:
        print("Yuancon SDVX controller", yc)

yuan_sdvx()

#YUANCON SDVX BLACK
def yuan_sdvx_black():
    driver.get('https://yuancon.store/controller/sdvxblack')
    yc = driver.find_elements_by_tag_name('h4')[0].text
    if yc == nostock:
        print("Yuancon black SDVX controller OUT OF STOCK")
    else:
        print("Yuancon black SDVX controller", yc)

yuan_sdvx_black()

#YUNACON TAIKO DRUM
def yuan_taiko():
    driver.get('https://yuancon.store/controller/taiko')
    yc = driver.find_elements_by_tag_name('h4')[0].text
    if yc == nostock:
        print("Yuancon Taiko drum OUT OF STOCK")
    else:
        print("Yuancon Taiko drum", yc)

yuan_taiko()

#YUANCON GROOVE COASTER CONTROLLER
def yuan_groove():
    driver.get('https://yuancon.store/controller/groovecoaster')
    yc = driver.find_elements_by_tag_name('h4')[0].text
    if yc == nostock:
        print("Yuancon Groove Coaster controller OUT OF STOCK")
    else:
        print("Yuancon Groove Coaster controller", yc)

yuan_groove()

#GAMO2 CONTROLLERS
special_char = "-"
#GAMO2 POP'N MUSIC CONTROLLER
def gamo_pop():
    driver.get('https://www.gamo2.com/en/index.php?dispatch=products.view&product_id=249')
    try:
        gc = driver.find_element_by_xpath('//*[@id="out_of_stock_info_249"]').text
    except:
        gc = driver.find_element_by_xpath('//*[@id="in_stock_info_249"]').text
    #Removing "-"
    for x in special_char:
        gc = gc.replace(x, " ")
        gc = gc.upper()
    print("Gamo2 Pop'n Music controller", gc)

gamo_pop()

def gamo_sdvx():
    driver.get('https://www.gamo2.com/en/index.php?dispatch=products.view&product_id=320')
    try:
        gc = driver.find_element_by_xpath('//*[@id="out_of_stock_info_320"]').text
    except:
        gc = driver.find_element_by_xpath('//*[@id="in_stock_info_320"]').text

    for x in special_char:
        gc = gc.replace(x, " ")
        gc = gc.upper()
    print("Gamo2 SVSE5 Sound Voltex controller", gc)

gamo_sdvx()

def gamo_jubeat():
    driver.get('https://www.gamo2.com/en/index.php?dispatch=products.view&product_id=321')
    try:
        gc = driver.find_element_by_xpath('//*[@id="out_of_stock_info_321"]').text
    except:
        gc = driver.find_element_by_xpath('//*[@id="in_stock_info_321"]').text

    for x in special_char:
        gc = gc.replace(x, " ")
        gc = gc.upper()
    print("Gamo2 Jubeat controller", gc)

gamo_jubeat()

def gamo_phoenix():
    driver.get('https://www.gamo2.com/en/index.php?dispatch=products.view&product_id=348')
    try:
        gc = driver.find_element_by_xpath('//*[@id="out_of_stock_info_348"]').text
    except:
        gc = driver.find_element_by_xpath('//*[@id="in_stock_info_348"]').text

    for x in special_char:
        gc = gc.replace(x, " ")
        gc = gc.upper()
    print("Gamo2 Pheonixwan Beatmania controller", gc)

gamo_phoenix()

def gamo_ezmax():
    driver.get('https://www.gamo2.com/en/index.php?dispatch=products.view&product_id=349')
    try:
        gc = driver.find_element_by_xpath('//*[@id="out_of_stock_info_349"]').text
    except:
        gc = driver.find_element_by_xpath('//*[@id="in_stock_info_349"]').text

    for x in special_char:
        gc = gc.replace(x, " ")
        gc = gc.upper()
    print("Gamo2 EZMAX Hybrid controller", gc)

gamo_ezmax()

def gamo_diva():
    driver.get('https://www.gamo2.com/en/index.php?dispatch=products.view&product_id=355')
    try:
        gc = driver.find_element_by_xpath('//*[@id="out_of_stock_info_355"]').text
    except:
        gc = driver.find_element_by_xpath('//*[@id="in_stock_info_355"]').text

    for x in special_char:
        gc = gc.replace(x, " ")
        gc = gc.upper()
    print("Gamo2 Project Diva controller", gc)

gamo_diva()

def gamo_gitadora():
    driver.get('https://www.gamo2.com/en/index.php?dispatch=products.view&product_id=358')
    try:
        gc = driver.find_element_by_xpath('//*[@id="out_of_stock_info_358"]').text
    except:
        gc = driver.find_element_by_xpath('//*[@id="in_stock_info_358"]').text

    for x in special_char:
        gc = gc.replace(x, " ")
        gc = gc.upper()
    print("Gamo2 Gitadora controller", gc)

gamo_gitadora()

#ISTMALL CONTROLLERS (MY FAVORITE HEEM HEEM)

