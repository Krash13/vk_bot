from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://ig.pro100basket.ru/games/?region=40120&compId=42127")
main_page = driver.page_source
print(main_page)