from ..utilities import utilitiesCPS
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

class login:
    # Inicia el servicio del webdriver
    def __init__(self):
        serv = Service(ChromeDriverManager().install())
        opt = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=serv, options=opt)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

    def ingreso_pagina(self, usuario, password):
        utilitiesCPS.browser_open(self)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="//input[contains(@placeholder,'Username')]").send_keys(usuario)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//input[contains(@placeholder,'Password')]").send_keys(password)
        self.driver.find_element(by=By.XPATH, value="//input[contains(@type,'submit')]").click()

    def val_camp_obli(self,cantidad):
        utilitiesCPS.val_camp_obl(self,cantidad)

    def seleccionar_producto(self):
        self.driver.find_element(by=By.XPATH, value="//div[@class='inventory_item_name '][contains(.,'Sauce Labs Backpack')]").click()
        self.driver.find_element(by=By.XPATH, value="//button[@class='btn btn_primary btn_small btn_inventory'][contains(.,'Add to cart')]").click()
        self.driver.find_element(by=By.XPATH, value="//a[@class='shopping_cart_link'][contains(.,'1')]").click()

    def remover_producto(self):
        self.driver.find_element(by=By.XPATH, value="//button[@class='btn btn_secondary btn_small cart_button'][contains(.,'Remove')]").click()

    def checkout (self, nombre,apellido,codigo):
        self.driver.find_element(by=By.XPATH, value="//button[@class='btn btn_action btn_medium checkout_button '][contains(.,'Checkout')]").click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="//input[contains(@placeholder,'First Name')]").send_keys(nombre)
        self.driver.find_element(by=By.XPATH, value="//input[contains(@placeholder,'Last Name')]").send_keys(apellido)
        self.driver.find_element(by=By.XPATH, value="//input[contains(@placeholder,'Zip/Postal Code')]").send_keys(codigo)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//input[contains(@type,'submit')]").click()

    def finalizar_compra (self):
        self.driver.find_element(by=By.XPATH, value="//button[@class='btn btn_action btn_medium cart_button'][contains(.,'Finish')]").click()
        self.driver.find_element(by=By.XPATH, value="//button[@class='btn btn_primary btn_small'][contains(.,'Back Home')]").click()

    def cancelar (self):
        self.driver.find_element(by=By.XPATH, value="//button[@class='btn btn_secondary back btn_medium cart_cancel_link'][contains(.,'Cancel')]").click()

    def close(self):
        self.driver.close()
