from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


def saveAverageValue():
    url = "http://localhost:9090/graph?g0.expr=sum(sum_over_time(gunicorn_request_duration%7Bapp%3D%22httpbin%22%7D%5B1h%5D))%20%2Fsum(count_over_time(gunicorn_request_duration%7Bapp%3D%22httpbin%22%7D%5B1h%5D))&g0.tab=1&g0.stacked=0&g0.show_exemplars=0&g0.range_input=1h"
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            lambda s: s.find_element(By.CLASS_NAME, "execute-btn").is_displayed())
    except TimeoutException:
        return saveAverageValue()

    time.sleep(2)

    executeButton = driver.find_element(By.CLASS_NAME, "execute-btn")
    executeButton.click()

    while True:
        try:
            tableRowElement = driver.find_element(By.TAG_NAME, "tr")
            tdElement = tableRowElement.find_elements(By.TAG_NAME, "td")[1]

            break
        except:
            time.sleep(2)
            executeButton.click()

    os.chdir("C:/Users/Player Ghost/PycharmProjects/prometheusScrappingTest/")

    with open("outputs.txt", "a") as file:
        file.write(f'{tdElement.text} \n')


def runCommmands(path, fileName):
    with open(path + "/" + fileName, "r", encoding="utf8") as f:
        lines = f.readlines()

        for i in lines:
            os.chdir("C:/model-aval-prometeheu-av3")
            os.system("docker compose up -d")

            time.sleep(12)

            os.chdir(path)
            os.system(i)

            time.sleep(3)

            saveAverageValue()

            time.sleep(2)

            os.chdir("C:/model-aval-prometeheu-av3")
            os.system("docker compose down")

            time.sleep(2)


if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')

    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    print("Rodando...")

    runCommmands("C:/Users/Player Ghost/Desktop/Load-test-tools-benchmark/Tools/K6", "runByScriptAv3.sh")
    runCommmands("C:/Users/Player Ghost/Desktop/Load-test-tools-benchmark/Tools/VegetaTestScript", "runByScript.bat")
    runCommmands("C:/Users/Player Ghost/Desktop/Load-test-tools-benchmark/Tools/wrk", "runByScript.bat")
    runCommmands("C:/Users/Player Ghost/Desktop/Load-test-tools-benchmark/Tools/jmeter", "run.bat")
