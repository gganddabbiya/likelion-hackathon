from crawling.craw_func import festival_setdefault, exhibition_setdefault, festival_save, exhibition_save, duplicateCheck, parse_date

from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep


def festival(driver):
    driver.get("https://ticket.melon.com/concert/index.htm?genreType=GENRE_CON")

    # 근데 여기부터는 이미 열린 거라 BeautifulSoup 이용 가능
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    date = bs.find_all("span", {"class", "day"})
    location = bs.find_all("span", {"class", "location"})

    # 태그 제거
    for i in range(len(date)):
        date[i] = date[i].text
        location[i] = location[i].text

    # 상세페이지 링크
    href = bs.select('#perf_poster > li > a')
    href_list = []
    for i in href:
        href_list.append('https://ticket.melon.com/' + i.attrs['href'])

    dictList = []
    for i in range(len(date)):
        dic = festival_setdefault()
        driver.get(href_list[i])

        sleep(0.5)

        dic["image"] = driver.find_element(By.CSS_SELECTOR, 'div.wrap_consert_cont img').get_attribute("src")
        dic["title"] = driver.find_element(By.CSS_SELECTOR, 'p.tit').text

        parse_date(date[i], dic, '-')

        dic["place"] = location[i]
        dic["link"] = href_list[i]

        dic["timeinfo"] = driver.find_element(By.CSS_SELECTOR, 'dl > dd:nth-child(4)').text
        dic["age"] = driver.find_element(By.CSS_SELECTOR, 'dl.info_right > dd:nth-child(4)').text

        images = []

        image_eles = driver.find_elements(By.CSS_SELECTOR, "div.box_img_content img")

        for img in image_eles:
            images.append(img.get_attribute("src"))

        dic['detail_img'] = images

        dictList.append(dic)
        print(dic["title"])
        sleep(0.5)
    duplicateCheck(dictList, "fe")
    festival_save(dictList)


def exhibition(driver):
    driver.get("https://ticket.melon.com/concert/index.htm?genreType=GENRE_EXH")

    # 근데 여기부터는 이미 열린 거라 BeautifulSoup 이용 가능
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    date = bs.find_all("span", {"class", "day"})
    location = bs.find_all("span", {"class", "location"})

    # 태그 제거
    for i in range(len(date)):
        date[i] = date[i].text
        location[i] = location[i].text

    # 상세페이지 링크
    href = bs.select('#perf_poster > li > a')
    href_list = []
    for i in href:
        href_list.append('https://ticket.melon.com/' + i.attrs['href'])

    dictList = []
    for i in range(len(date)):
        dic = exhibition_setdefault()
        driver.get(href_list[i])

        dic["image"] = driver.find_element(By.CSS_SELECTOR, 'div.wrap_consert_cont img').get_attribute("src")
        dic["title"] = driver.find_element(By.CSS_SELECTOR, 'p.tit').text

        parse_date(date[i], dic, '-')

        dic["place"] = location[i]
        dic["link"] = href_list[i]

        dic["timeinfo"] = driver.find_element(By.CSS_SELECTOR, 'dl > dd:nth-child(4)').text
        dic["age"] = driver.find_element(By.CSS_SELECTOR, 'dl.info_right > dd:nth-child(4)').text

        images = []

        image_eles = driver.find_elements(By.CSS_SELECTOR, "div.box_img_content img")

        for img in image_eles:
            images.append(img.get_attribute("src"))

        dic['detail_img'] = images

        dictList.append(dic)
        print(dic["title"])
        sleep(1)

    duplicateCheck(dictList, "ex")
    exhibition_save(dictList)