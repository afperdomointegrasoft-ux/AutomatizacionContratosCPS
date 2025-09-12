import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def browser_open(self):
    self.driver.get("https://www.saucedemo.com/")


def val_camp_obl(self, cantidad):
    campos = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "invalid-feedback")))
    assert len(campos) == cantidad, "** ERROR ** NO SE VISUALIZAN CAMPOS REQUERIDOS o no se visualiza l total de campos requeridos en el formulario"
