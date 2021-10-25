from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

try:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(
        "https://hh.ru/search/vacancy?area=1&fromSearchLine=true&st=searchVacancy&text=Python&from=suggest_post"
    )
    print(driver.title)

except BaseException as e:
    print(e)

finally:
    driver.close()

# Список вакансий
vacancies_list = driver.find_elements_by_xpath(
    "//span[@class='g-user-content']/a[@class='bloko-link']"
)
