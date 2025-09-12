# PruebaTecnicaQA
Prueba Técnica QA - R5

# Como clonar el repositorio
Paso 1: Instalar git
Windows: https://git-scm.com/download/win
MAC: https://git-scm.com/download/mac
General: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git

Paso 2: Abrir git por terminal
Windows: CMD
MAC: Terminal

Paso 3: Ingresar a la carpeta donde se va a clonar el proyecto.
    -ls 
    -cd Documents/
    
Paso 4: Para clonar el proyecto se debe ejecutar el siguiente comando git clone
    -git clone https://github.com/123andres-per/PruebaTecnicaQA.git
    


## Como configurar el entorno de desarrollo

Paso 1: Descargar e instalar python en la versión estable: https://www.python.org/downloads/
Paso 2: Descargar e instalar selenium en la versión estable: https://www.selenium.dev/downloads/
Paso 3: Descargar e instalar pycharm en la versión community:
    -Windows: https://www.jetbrains.com/es-es/pycharm/download/#section=windows
    -MAC: https://www.jetbrains.com/es-es/pycharm/download/#section=mac
    
Paso 4: Descargar y configurar el Chrome webdriver (puede hacerse con PATH o en el script) 
Configuracion del WebDriver mediante PATH
-Verificar la version del navegador Google Chrome que tiene actualmente el sistema
-De acuerdo a la version descargar el WebDriver en la pagina https://chromedriver.chromium.org/downloads
-Para la instalacion del PATH puede guiarse de la siguiente pagina: https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
-En el punto 2 "The PATH Environment Variable" se indica como instalarlo

Paso 5: Configuracion del WebDriver en el script
-Abrir Pycharm como administrador, abrir el proyecto de automatizacion

Paso 6: Abrir el Terminal

Paso 7: Instalar las librerias de Selenium, Pytest y Webdriver Manager
-pip install selenium o py -m pip install selenium
-pip install pytest o py -m pip install pytest
-pip install webdriver-manager o py -m pip install webdriver-manager
En caso de que para SO Windows No se visualicen cambios, abrir cmd, ejecutarlo como administrador y ejecutar los mismos codigos mencionados anteiormente


NOTA: Para la ejecución de scripts se establecíó como navegador predeterminado Google chrome
