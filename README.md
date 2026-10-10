# pre-entrega-automation-testing-ana-lubari


## Pre Entrega de Proyecto Final: 

En este proyecto automatizamos pruebas en la página web Saucedemo.


### Setup:

```
pip install pytest pytest-html selenium
```

### Ejecutar tests:

```
pytest tests/test_saucedemo.py -v --html=reporte.html
```

### Ver reporte:

Para abrir el reporte generado en el navegador:
```bash
xdg-open reporte.html

