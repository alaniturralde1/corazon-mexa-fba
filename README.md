# corazon-mexa-fba

Este repositorio contiene scripts y utilidades para generar fichas de envíos FBA (Fulfillment by Amazon).

## Uso del script `generar_ficha_fba.py`

Ejemplo de uso:

```bash
python generar_ficha_fba.py --producto "Producto X" --sku 123ABC --cantidad 10 \
    --precio 5.99 --destinatario "Cliente Ejemplo" --salida ficha.json
```

El script generará un archivo JSON con la información de la ficha y el costo total.

