import interpark, melon, yes

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


    # 각 사이트 크롤링 함수가 들어올 위치#
    # 중복이 있을 경우 먼저 실행하는 함수의 행사 정보가 저장 됩니다.
    # 따라서 사이트 우선순위가 있다면 우선 순위대로 함수를 실행하면 됩니다.

    interpark.festival(driver)
    interpark.exhibition(driver)

    yes.festival(driver)
    yes.exhibition(driver)

    melon.festival(driver)
    melon.exhibition(driver)

    driver.close()




