# Made by Dante Fernando 2020
# Github.com/dantefernando
# WIP, This code IS NOT PERFECT and was BUILT FOR MY USE!
# Feel free to change up the code!
# Credits: https://github.com/aj-4/ig-followers


from selenium import webdriver
import time
from account import username    # I made an account.py file with my discord username and password here.
from account import password


class DiscordBot:
    def __init__(self, username1, password1):
        self.driver = webdriver.Chrome("C:/Users/Fernpe2/Downloads/chromedriver.exe") # CHANGE THIS VALUE TO DIR OF
        # WEBDRIVER!!!
        self.driver.get(
            "https://discordapp.com/channels/626436080672964628/671821869707427851")  # Opens up Specific Discord
        time.sleep(10)
        self.driver.find_element_by_xpath("//input[@type=\"email\"]")\
            .send_keys(username1)  # Finds Email box and types username into it
        self.driver.find_element_by_xpath("//input[@type=\"password\"]")\
            .send_keys(password1)  # Finds pw box and types pw into it
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
            .click()    # Presses submit
        time.sleep(10)
        self.driver.find_element_by_xpath(  # Types into the Discord Text box "!p daily" and presses enter
            "/html/body/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div[3]/div[2]")\
            .send_keys("!p daily" + "\n")
        time.sleep(3)
        self.driver.get("https://discordbots.org/bot/pancake/vote")
        time.sleep(12)   # Heads to the voting page for the Pancakes
        button = self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/div[4]/button[2]")
        self.driver.execute_script("arguments[0].click();", button)   # Accept Cookies
        time.sleep(4)
        self.driver.find_element_by_xpath(
            "/html/body/section/article/div[2]/div[2]/div/div/div[2]/span")\
            .click()   # Clicks Vote
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/section/article/div[1]/div[2]/p/a/strong")\
            .click()    # Clicks Login
        time.sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[1]/div/div[3]/div/div/div[2]/button[2]")\
            .click()    # Clicks Authorize
        time.sleep(4)
        self.driver.find_element_by_xpath(
            "/html/body/section/article/div[2]/div[2]/div/div/div[2]/span") \
            .click()  # Click Vote
        time.sleep(5)
        print("Successfully received daily pancake!")


DiscordBot(username, password)
