import time
import random
import logging

from selenium import webdriver

def parsing_website(movie_name, number_of_times, duration):
    """
    Method to read the URL
    Parse the website and create new accounts on the IMDB website
    Rate the movie 10 stars
    Sign out of the website and repeat until loop exits, and 
    Close the browser in the end.

    :param movie_name: Name of the movie
    :param number_of_times: loop count
    :param duration: time duration set during HTML parsing
    return: loop count 
    """
    url = "https://www.imdb.com/"
    driver = webdriver.Chrome(r"C:\Users\VG\Downloads\chromedriver_win32\chromedriver.exe") # r(to produce a raw string)
    driver.get(url)
    with open("name_list.txt", "r") as fr:
        for name in fr:
            number = random.randint(1000, 9999)
            user = "{}_{}".format(name.strip(), str(number))

            driver.find_element_by_xpath("//*[@id='imdbHeader']/div[2]/div[6]/a/div").click()
            time.sleep(duration)
            driver.find_element_by_link_text("Create a New Account").click()
            time.sleep(duration)
            driver.find_element_by_id("ap_customer_name").send_keys(user)
            time.sleep(duration)
            driver.find_element_by_name("email").send_keys("{}@gmail.com".format(user))
            time.sleep(duration)
            driver.find_element_by_id("ap_password").send_keys("Password123$")
            time.sleep(duration)
            driver.find_element_by_id("ap_password_check").send_keys("Password123$")
            time.sleep(duration)
            driver.find_element_by_id("a-autoid-0").click()
            time.sleep(duration)
            driver.find_element_by_id("suggestion-search").send_keys(movie_name)
            time.sleep(duration)
            driver.find_element_by_id("react-autowhatever-1--item-0").click()
            time.sleep(duration)
            driver.find_element_by_xpath("//*[@id='star-rating-widget']/div/button/span[1]").click()
            time.sleep(duration)
            driver.find_element_by_xpath("//*[@id='star-rating-widget']/div/div/span[1]/span/a[10]").click()
            time.sleep(duration)
            driver.find_element_by_xpath("//*[@id='imdbHeader']/div[2]/div[6]/div/label[2]/div/span").click()
            time.sleep(duration)
            driver.find_element_by_xpath("//*[@id='navUserMenu-contents']/ul/a[7]").click()
            time.sleep(duration)
            driver.find_element_by_xpath("//*[@id='imdbHeader']/div[2]/div[6]/a/div").click()
            time.sleep(duration)
            number_of_times += 1
    driver.close()
    return number_of_times

if __name__ == "__main__":

    movie_name = "Chhapaak" # string value
    number_of_times = 0
    duration = 1

    try:
        count = parsing_website(movie_name, number_of_times, duration)
        logging.info("Number of accounts created on IMDB: {}".format(number_of_times))
    except:
        logging.warning("IMDB website asking for CAPTCHA during account creation to make sure it's not a robot.")
