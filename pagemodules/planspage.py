from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class get_element:

    def __init__(self, driver):
        self.driver = driver

    def get_multi_text(self, parent_path, child_path):
        count = 0
        ele_text = []
        try:
            plans = WebDriverWait(self.driver, 30).until(lambda driver: driver.find_elements(By.XPATH, parent_path))
            for plan_itr in plans:
                button = WebDriverWait(self.driver, 10).until(lambda plan_itr: plan_itr.find_element(By.XPATH, child_path)).text
                ele_text.append(button)
                count = count + 1
            var1, var2 = ele_text, count

        except TimeoutException:
            var1, var2 = "Element Not Found", " "

        return var1, var2

    def get_ele_click(self, parent_path, child_path):

        try:
            plans = WebDriverWait(self.driver, 25).until(lambda driver: driver.find_element(By.XPATH, parent_path))
            (WebDriverWait(plans, 20).until(
                EC.element_to_be_clickable(plans.find_element(By.XPATH, child_path)))).click()
            var1 = "Done"
        except TimeoutException:
            var1 = "Element Not Found"

        return var1

    def get_ele_text(self, parent_path, child_path):

        try:
            plans = WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element(By.XPATH, parent_path))
            ele = WebDriverWait(self.driver, 15).until(lambda driver: plans.find_element(By.XPATH, child_path)).text
            var1 = ele
        except TimeoutException:
            var1 = "Element Not Found"

        return var1
