from selenium import webdriver
import time
from tqdm import tqdm
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from numpy.random import randn
from chromedriver_py import binary_path  # this will get you the path variable
import os

insta_email = os.getenv('insta_email')
insta_password = os.getenv('insta_password')


class InstagramBot:
    def __init__(self, insta_email, insta_password, username, mu, sigma):
        self.insta_email = insta_email
        self.insta_password = insta_password
        self.username = username
        self.mu = mu
        self.sigma = sigma
    #
    def set_up_driver(self, mu):
        # Define instagram url
        insta_url = "https://www.instagram.com/?hl=fr"
        # Define the path of your webdrive
        # path_downloaded_webdriver = '/usr/bin/chromedriver'
        path_downloaded_webdriver = '/Users/elmbarki/Downloads/chromedriver'
        path_downloaded_webdriver = binary_path
        # service_object = Service(binary_path)
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # Call our Webdriver
        driver = webdriver.Chrome(path_downloaded_webdriver, options=chrome_options)  #
        time.sleep(mu)
        # Go to instagram page
        driver.get(insta_url)
        time.sleep(mu)
        # Accept cookies usage by clicking on the accept button
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]').click()
        time.sleep(mu)
        # Fill out our email and password to access to our insta account
        email = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.clear()
        email.send_keys(self.insta_email)
        time.sleep(mu)
        password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.clear()
        password.send_keys(self.insta_password)
        time.sleep(mu)
        # Validate our credentials
        driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(mu)
        # Ask to do save credentials later
        driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(mu)
        # Ask to activate notifactions later
        try:
            driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]').click()
            time.sleep(mu)
        except:
            try:
                driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]').click()
                time.sleep(mu)
            except:
                try:
                    driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]').click()
                    time.sleep(mu)
                except:
                    try:
                        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[3]/button[2]').click()
                        time.sleep(mu)
                    except:
                        try:
                            driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/button[2]').click()
                            time.sleep(mu)
                        except:
                            pass
        # There you are connected to your Instagram account
        print('Set up driver done!')
        driver.set_window_position(0, 0)
        driver.set_window_size(1024, 768)
        return driver
    #
    def follow_random(self, driver, followers):
        # Now, we should to navigate throuw instagram profile and follow randomly some of them
        driver.get("https://www.instagram.com/explore/people/")
        time.sleep(randn(1)[0] * self.sigma + self.mu)
        scroll_box = driver.find_element(By.XPATH, '/html')
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(randn(1)[0] * self.sigma + self.mu)
            # scroll down and retrun the height of scroll (JS script)
            ht = driver.execute_script(""" 
                        arguments[0].scrollTo(0, arguments[0].scrollHeight);
                        return arguments[0].scrollHeight; """, scroll_box)
        time.sleep(randn(1)[0] * self.sigma + self.mu)
        links = scroll_box.find_elements(By.TAG_NAME, 'a')
        futur_followers_list = [name.text for name in links if name.text != '']
        futur_followers_list = futur_followers_list[:-10]  # delete footer
        futur_followers_list = [x for x in futur_followers_list if x not in followers]
        for follower in tqdm(futur_followers_list):
            self.follow(follower)
        return {}
    #
    def follow(self, username):
        # To Do driver = set_up_driver()
        driver.get("https://www.instagram.com/%s/" % username)
        time.sleep(randn(1)[0] * self.sigma + self.mu)
        driver.find_element(By.XPATH, "//button[contains(.,'Follow')]").click()
        time.sleep(randn(1)[0] * self.sigma + self.mu)
        return {}
    #
    def unfollow(self, username):
        driver.get("https://www.instagram.com/%s/" % username)
        time.sleep(int(randn(1)[0]) * self.sigma + self.mu)
        driver.find_element(By.CSS_SELECTOR, "[aria-label=Following]").click()
        time.sleep(int(randn(1)[0]) * self.sigma + self.mu)
        driver.find_element(By.XPATH, "//button[contains(.,'Unfollow')]").click()
        time.sleep(int(randn(1)[0]) * self.sigma + self.mu)
        return {}
    #
    def get_my_following(self, driver):
        driver.get('https://www.instagram.com/%s' % self.username)
        time.sleep(abs(randn(1)[0]) * self.sigma + self.mu)
        driver.find_element(By.XPATH, "//a[contains(@href, '%s/following')]" % self.username).click()
        time.sleep(abs(randn(1)[0]) * self.sigma + self.mu)
        #scroll_box = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[3]")
        scroll_box = driver.find_element(By.CLASS_NAME, "isgrP")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(abs(randn(1)[0]) * self.sigma + self.mu)
            # scroll down and retrun the height of scroll (JS script)
            ht = driver.execute_script(""" 
                        arguments[0].scrollTo(0, arguments[0].scrollHeight);
                        return arguments[0].scrollHeight; """, scroll_box)
        time.sleep(abs(randn(1)[0]) * self.sigma + self.mu)
        links = scroll_box.find_elements(By.TAG_NAME, 'a')
        followers_list = [name.text for name in links if name.text != '']
        driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button/div").click()
        time.sleep(abs(randn(1)[0]) * self.sigma + self.mu)
        return followers_list
    #
    def get_my_follower(self, driver):
        driver.get('https://www.instagram.com/%s' % self.username)
        time.sleep(abs(randn(1)[0]) * self.sigma + self.mu)
        driver.find_element(By.XPATH, "//a[contains(@href, '%s/followers')]" % self.username).click()
        time.sleep(abs(randn(1)[0]) * self.sigma + self.mu)
        scroll_box = driver.find_element(By.CLASS_NAME, "isgrP")
        time.sleep(abs(randn(1)[0]) * self.sigma + self.mu)
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            # scroll down and retrun the height of scroll (JS script)
            ht = driver.execute_script(""" 
                        arguments[0].scrollTo(0, arguments[0].scrollHeight);
                        return arguments[0].scrollHeight; """, scroll_box)
            time.sleep(abs(randn(1)[0]) * self.sigma + self.mu)
        links = scroll_box.find_elements(By.TAG_NAME, 'a')
        followers_list = [name.text for name in links if name.text != '']
        driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button/div").click()
        time.sleep(abs(randn(1)[0]) * self.sigma + self.mu)
        return followers_list
    #
    def delete_all(self, driver, followings, followers):
        to_delete = [username for username in followings if username not in followers]
        chunck_size = 10
        nb_chunks = len(to_delete) // chunck_size + 1
        for i in tqdm(range(nb_chunks - 1)):
            to_delete_i = to_delete[i * chunck_size: (i + 1) * chunck_size]
            for x in tqdm(to_delete_i):
                print(x)
                try:
                    self.unfollow(x)
                    time.sleep(randn(1)[0] * self.sigma + self.mu)
                except:
                    pass
            driver.get('https://www.instagram.com/')
            time.sleep(randn(1)[0] * self.sigma + self.mu)
        return 'Deletion Done'


if __name__ == '__main__':
    instaBot = InstagramBot(insta_email, insta_password, 'haaply_travel', 20, 10)
    driver = instaBot.set_up_driver()
    followers = instaBot.get_my_follower(driver)
    followings = instaBot.get_my_following(driver)
    instaBot.delete_all(driver, followings, followers)
    instaBot.follow_random(driver, followers)
