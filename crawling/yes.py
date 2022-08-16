from crawling.craw_func import festival_setdefault, exhibition_setdefault, festival_save, exhibition_save, duplicateCheck, parse_date
from selenium.webdriver.common.by import By
from time import sleep


def exhibition(driver):
    url = 'http://ticket.yes24.com/New/Genre/GenreList.aspx?genretype=2&genre=15475'
    driver.get(url)

    list = []

    num = len(driver.find_elements(By.CSS_SELECTOR, 'div.ms-list-imgs > a'))
    for index in range(num):
        button = driver.find_elements(By.CSS_SELECTOR, 'div.ms-list-imgs > a')[index]
        button.click()
        sleep(0.5)
        items = exhibition_setdefault()
        items['title'] = driver.find_element(By.CSS_SELECTOR, 'p.rn-big-title').text

        # 날짜 분리
        date = driver.find_element(By.CSS_SELECTOR, 'span.ps-date').text
        parse_date(date, items, '~')

        items['image'] = driver.find_element(By.XPATH,
                                             '//*[@id="mainForm"]/div[10]/div/div[1]/div[1]/div[1]/img').get_attribute(
            'src')
        items['place'] = driver.find_element(By.CSS_SELECTOR, 'span.ps-location').text
        items['timeinfo'] = driver.find_element(By.XPATH,
                                                '//*[@id="mainForm"]/div[10]/div/div[1]/div[2]/div[1]/dl/dd[2]').text
        items['link'] = driver.current_url

        age_texts = driver.find_element(By.XPATH, '//*[@id="mainForm"]/div[10]/div/div[1]/div[2]/div[1]/dl/dd[1]').text
        adult = "성인인증"
        if adult in age_texts:
            items['age'] = age_texts.replace(adult, "")
        else:
            items['age'] = age_texts

        detail_imgs = driver.find_elements(By.CSS_SELECTOR, 'img.txc-image')
        detail_imgs_src = []
        for detail_img in detail_imgs:
            detail_imgs_src.append(detail_img.get_attribute('src'))
        items['detail_img'] = detail_imgs_src

        list.append(items)
        print(items["title"])
        driver.back()
        sleep(0.5)

    duplicateCheck(list, "ex")
    exhibition_save(list)


def festival(driver):
    URL = "http://ticket.yes24.com/New/Genre/GenreList.aspx?genretype=2&genre=15464"
    driver.get(URL)

    dictList = []
    num = len(driver.find_elements(By.CSS_SELECTOR, 'div.ms-list-imgs > a'))
    for i in range(num):
        button = driver.find_elements(By.CSS_SELECTOR, 'div.ms-list-imgs > a')[i]
        button.click()
        sleep(0.5)
        fe = festival_setdefault()
        fe['title'] = driver.find_element(By.CSS_SELECTOR, 'p.rn-big-title').text #title

        date = driver.find_element(By.CSS_SELECTOR, 'span.ps-date').text
        parse_date(date, fe , '~')

        fe['image'] = driver.find_element(By.CSS_SELECTOR, 'div.rn-product-imgbox >img').get_attribute("src") #img
        fe['place'] = driver.find_element(By.CSS_SELECTOR, 'a#ps-location > span').text
        fe['timeinfo'] = driver.find_element(By.CSS_SELECTOR, 'dl > dd:nth-child(4)').text
        fe['age'] = driver.find_element(By.CSS_SELECTOR, 'dl > dd').text
        fe['link'] = driver.current_url

        fe['detail_img'] = []
        images = driver.find_elements(By.CLASS_NAME, 'txc-image')
        for image in images:
            if image.get_attribute('src') != None:
                fe['detail_img'].append(image.get_attribute('src'))


        dictList.append(fe)
        print(fe["title"])
        driver.back()
        sleep(0.5)

    duplicateCheck(dictList, "fe")
    festival_save(dictList)
