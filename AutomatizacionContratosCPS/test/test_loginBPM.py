import unittest
import time
from ..functions.loginBPM import login

class pagina(unittest.TestCase):

    def setUp(self):
        self.home = login()


    def test_01_login(self):
        self.home.ingreso_pagina("soporte")



    def tearDown(self):
        time.sleep(1)
        print('¡Se ha completado el Test Aumatico!')
        self.home.driver.quit()
