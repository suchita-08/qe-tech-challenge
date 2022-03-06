from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class sticky_display:

    def __init__(self, driver):
        self.driver = driver

    def get_sticky_cart_text(self, parent_path, child_path):
        try:
            str1 = WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(By.XPATH, child_path)).text
            ele_text = str1

        except TimeoutException:
            ele_text = "Element Not Found"

        return ele_text

    def get_sticky_button_click(self, parent_path, child_path):
        try:
            plans_b = WebDriverWait(self.driver, 25).until(lambda driver: driver.find_element(By.XPATH, parent_path))
            (WebDriverWait(plans_b, 15).until(
                EC.element_to_be_clickable(plans_b.find_element(By.XPATH, child_path)))).click()
            ele_text = "Done"

        except TimeoutException:
            ele_text = "Element Not Found"

        return ele_text
