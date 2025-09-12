import time
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def browser_open(self):
    self.driver.get("http://localhost:801/frmLogin.aspx")


@staticmethod
def generar_codigo():
    """
    Genera el  cod concatenando el valor fijo con la parte dinámica:
    Código = "900332071" + ((día + mes + año) * 2 + 13)
    """
    hoy = datetime.now()
    dia = hoy.day
    mes = hoy.month
    anio = hoy.year

    parte_dinamica = (dia + mes + anio) * 2 + 13
    codigo = "900332071" + str(parte_dinamica)
    return codigo


def val_camp_obl(self, cantidad):
    campos = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "invalid-feedback")))
    assert len(campos) == cantidad, "** ERROR ** NO SE VISUALIZAN CAMPOS REQUERIDOS o no se visualiza l total de campos requeridos en el formulario"
