from craw_func import festival_setdefault, exhibition_setdefault, festival_save, exhibition_save, duplicateCheck, parse_date
from selenium.webdriver.common.by import By
from time import sleep

def exhibition(driver):
    driver.get("http://ticket.interpark.com/TPGoodsList.asp?Ca=Eve&SubCa=Eve_O&tid4=Eve_O&Sort=2")

    name = driver.find_elements(By.CSS_SELECTOR, "span.fw_bold")
    links = []
    for a in name:
        links.append(a.find_element(By.TAG_NAME, "a").get_attribute("href"))


    dictList = []

    for link in links:
        driver.get(link)
        dict = exhibition_setdefault()
        sleep(0.5)

        title = driver.find_element(By.CSS_SELECTOR,"h2.prdTitle").get_attribute("innerText")
        dict["title"] = title

        # 사진 링크 저장
        ticketImg = driver.find_element(By.CSS_SELECTOR,"img.posterBoxImage").get_attribute("src")
        dict['image'] = ticketImg

        # 장소, 기간, 관람 연령 정보 저장
        info = driver.find_elements(By.CSS_SELECTOR, 'li.infoItem')
        for i in info:
            label = i.find_element(By.CSS_SELECTOR, 'strong.infoLabel').get_attribute("innerText")
            content = i.find_element(By.CSS_SELECTOR, 'div.infoDesc').get_attribute("innerText")
            if "장소" in label:
                if "(자세히)" in content:
                    content = content.strip("(자세히)")
                dict["place"] = content
            elif "기간" in label:
                parse_date(content, dict, '~')
            elif "관람시간" in label:
                dict["timeinfo"] = content
            elif "관람연령" in label:
                dict["age"] = content


        imgs = driver.find_elements(By.CSS_SELECTOR, 'div.contentDetail img')

        img_list = []
        for img in imgs:
            img_list.append(img.get_attribute("src"))
        dict["detail_img"] = img_list

        dict["link"] = link
        dictList.append(dict)
        print(dict["title"])

        sleep(0.5)

    duplicateCheck(dictList, "ex")
    exhibition_save(dictList)



def festival(driver):
    driver.get("http://ticket.interpark.com/TPGoodsList.asp?Ca=Liv&SubCa=Fes&tid4=Fes")

    name = driver.find_elements(By.CSS_SELECTOR, "span.fw_bold")

    links = []
    dictList = []

    for a in name:
        links.append(a.find_element(By.TAG_NAME, "a").get_attribute("href"))

    for link in links:
        driver.get(link)
        dict = festival_setdefault()
        sleep(0.5)


        # 타이틀
        title = driver.find_element(By.CSS_SELECTOR,"h2.prdTitle").get_attribute("innerText")
        dict["title"] = title

        # 사진 링크 저장
        ticketImg = driver.find_element(By.CSS_SELECTOR, "img.posterBoxImage").get_attribute("src")
        dict["image"] = ticketImg

        # 장소, 기간, 관람 연령 정보 저장
        info = driver.find_elements(By.CSS_SELECTOR, 'li.infoItem')
        for i in info:
            label = i.find_element(By.CSS_SELECTOR, 'strong.infoLabel').get_attribute("innerText")
            content = i.find_element(By.CSS_SELECTOR, 'div.infoDesc').get_attribute("innerText")
            if "장소" in label:
                if "(자세히)" in content:
                    content = content.strip("(자세히)")
                dict["place"] = content
            elif "관람연령" in label:
                dict["age"] = content
            elif "공연시간" in label:
                dict["timeinfo"] = content
            elif "기간" in label:
                parse_date(content, dict, '~')


        #캐스팅 정보 받아와서 문자열 만들기
        # castingActor = []
        # actors = driver.find_elements(By.CSS_SELECTOR, 'div.castingName')
        #
        # for a in actors:
        #     castingActor.append(a.get_attribute("innerText"))
        #
        # casting = ', '.join(castingActor)
        # dict["casting"] = casting

        imgs = driver.find_elements(By.CSS_SELECTOR, 'div.contentDetail img')

        img_list = []
        for img in imgs:
            img_list.append(img.get_attribute("src"))
        dict["detail_img"] = img_list

        dict["link"] = link

        dictList.append(dict)
        print(dict["title"])
        sleep(0.5)

    duplicateCheck(dictList, "fe")
    festival_save(dictList)
