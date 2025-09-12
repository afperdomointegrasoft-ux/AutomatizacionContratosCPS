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



    def ingreso_pagina(self, usuario):
        utilitiesCPS.browser_open(self)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="//input[@id='txtUsuario']").send_keys(usuario)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//input[@id='btnSiguiente']").click()
        time.sleep(3)
        codigo = utilitiesCPS.generar_codigo()
        print(f"Código generado: {codigo}")  # solo para verificar
        campo = self.driver.find_element(by=By.XPATH, value="//input[@id='txtContrasenia']")
        campo.send_keys(codigo)
        self.driver.find_element(by=By.XPATH, value="//input[@id='BtnAceptar']").click()
        time.sleep(5)

    def cerrar(self):
        """Cerrar el navegador correctamente"""
        self.driver.close()



