# pre-entrega-automation-testing-ana-lubari

## Pre Entrega de Proyecto Final

En este proyecto automatizamos pruebas end-to-end (E2E) en la página web [SauceDemo](https://www.saucedemo.com/).

---


## 🎯 Propósito del Proyecto

El objetivo es automatizar los siguientes flujos en la aplicación SauceDemo:

- Login con credenciales válidas e inválidas
- Verificación del catálogo de productos
- Interacción con el carrito de compras (añadir productos y verificar su contenido)
- Cierre de sesión

---

### 🛠️ Tecnologías utilizadas

* **[Python 3](https://www.python.org/)**: Lenguaje de programación principal para el desarrollo de las pruebas automatizadas.
* **[Selenium WebDriver](https://www.selenium.dev/)**: Herramienta de automatización web para interactuar con la interfaz (clicks, inputs, locators, esperas explícitas con `WebDriverWait`).
* **[pytest](https://docs.pytest.org/)**: Framework de pruebas para estructurar las aserciones, test cases y fixtures del navegador.
* **[pytest-html](https://pytest-html.readthedocs.io/)**: Plugin de pytest para la generación automática de reportes de ejecución en formato HTML.
* **Firefox / GeckoDriver**: Navegador web y driver utilizado para la ejecución de las pruebas (en modo headless).
* **[SauceDemo](https://www.saucedemo.com/)**: Aplicación web e-commerce de prueba sobre la cual se ejecutaron los flujos automatizados (Login, Catálogo y Carrito).

---

### ⚙️ Setup e Instalación

#### 1. Requisitos previos
Asegúrate de contar con **Python 3** y el navegador **Firefox** en tu sistema operativo:

* **Linux (Ubuntu / Debian):**
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip firefox
  ```
* **macOS:**
  ```bash
  brew install python firefox
  ```

#### 2. Clonar el repositorio
```bash
git clone https://github.com/lubari/pre-entrega-automation-testing-ana-lubari.git
cd pre-entrega-automation-testing-ana-lubari
```

#### 3. Instalar dependencias de Python
```bash
pip install selenium pytest pytest-html
```
*(En Linux si recibes restricción de sistema):*
```bash
pip install selenium pytest pytest-html --break-system-packages
```

#### 4. WebDriver (GeckoDriver para Firefox)
> **Nota:** Gracias a Selenium 4+ (*Selenium Manager*), **GeckoDriver** se descarga y administra automáticamente. Solo se requiere tener instalado el navegador Firefox.

---

### 🚀 Ejecutar tests

Para ejecutar las pruebas en modo detallado y generar el reporte HTML:

```bash
pytest tests/test_saucedemo.py -v --html=reporte.html
```

---

### 📊 Ver reporte

Para abrir el reporte generado en el navegador predeterminado:

```bash
xdg-open reporte.html
```

o levantando un servidor local HTTP:

```bash
python3 -m http.server 8000
```
*(luego ingresar a `http://localhost:8000/reporte.html` en el navegador)*.
