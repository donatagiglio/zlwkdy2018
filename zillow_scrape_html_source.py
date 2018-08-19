from selenium import webdriver
import time


driver = webdriver.Chrome('/Applications/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.zillow.com/homes/for_sale/Boulder-CO/house_type/30543_rid/3-_beds/0-900000_price/0-3594_mp/globalrelevanceex_sort/40.20169,-105.067062,39.834114,-105.561447_rect/10_zm/');
html = driver.page_source
f = open("zillow_source_01.html", "wt")
f.write(html)
f.close()
driver.close()

for i in range(2,6):
    time.sleep(5)
    driver = webdriver.Chrome('/Applications/chromedriver')  # Optional argument, if not specified will search path.
    driver.get('https://www.zillow.com/homes/for_sale/Boulder-CO/house_type/30543_rid/3-_beds/0-900000_price/0-3594_mp/globalrelevanceex_sort/40.20169,-105.067062,39.834114,-105.561447_rect/10_zm/'+str(i)+'_p/');
    html = driver.page_source
    f = open("zillow_source_"+"{0:0>2}".format(i)+".html", "wt")
    f.write(html)
    f.close()
    driver.close()


