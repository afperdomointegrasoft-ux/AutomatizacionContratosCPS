import unittest
import time
from Functions.login import login

class pagina(unittest.TestCase):

    def setUp(self):
        self.home = login()


    def test_01_login(self):
        self.home.ingreso_pagina("standard_user","secret_sauce")

    def test_02_val_campo_req(self):
        self.home.ingreso_pagina(" "," ")
        self.home.val_camp_obli(2)

    def test_03_seleccionarProducto(self):
        self.home.ingreso_pagina("standard_user", "secret_sauce")
        self.home.seleccionar_producto()

    def test_04_checkout(self):
        self.home.ingreso_pagina("standard_user", "secret_sauce")
        self.home.seleccionar_producto()
        self.home.checkout("Andres","Perdomo","420005")
        self.home.finalizar_compra()
    def test_05_removerProductos(self):
        self.home.ingreso_pagina("standard_user", "secret_sauce")
        self.home.seleccionar_producto()
        self.home.remover_producto()

    def test_06_cancelarCompra(self):
        self.home.ingreso_pagina("standard_user", "secret_sauce")
        self.home.seleccionar_producto()
        self.home.checkout("Andres", "Perdomo", "420005")
        self.home.cancelar()


    def tearDown(self):
        time.sleep(1)
        print('¡Se ha completado el Test Aumatico!')
        self.home.close()