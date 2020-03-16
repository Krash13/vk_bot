from selenium import webdriver
from bs4 import BeautifulSoup

def print_score(url):
    driver = webdriver.PhantomJS()
    driver.get(url)
    main_page = driver.page_source
    soup = BeautifulSoup(main_page, 'lxml')
    scoreA = soup.find("div", { "class" : "ig__stat-scoreA" }).text
    scoreB = soup.find("div", {"class": "ig__stat-scoreB"}).text
    names = soup.findAll("div", { "class" : "ig__stat-team-name" })
    nameA=names[0].text
    nameB = names[1].text
    return " {} {}:{} {}".format(nameA,scoreA,scoreB,nameB)
