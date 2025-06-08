#!/usr/bin/env python3
"""Genera una ficha para envíos FBA en formato JSON."""
import argparse
import json
from datetime import datetime


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genera una ficha FBA a partir de los datos proporcionados"
    )
    parser.add_argument("--producto", required=True, help="Nombre del producto")
    parser.add_argument("--sku", required=True, help="SKU o identificador")
    parser.add_argument("--cantidad", type=int, required=True, help="Cantidad")
    parser.add_argument("--precio", type=float, required=True, help="Precio unitario")
    parser.add_argument(
        "--destinatario",
        required=True,
        help="Nombre del destinatario o cliente",
    )
    parser.add_argument(
        "-o",
        "--salida",
        default="ficha_fba.json",
        help="Archivo de salida (JSON)",
    )
    return parser.parse_args()


def generar_ficha(args: argparse.Namespace) -> dict:
    ficha = {
        "fecha": datetime.now().isoformat(timespec="seconds"),
        "producto": args.producto,
        "sku": args.sku,
        "cantidad": args.cantidad,
        "precio_unitario": args.precio,
        "destinatario": args.destinatario,
        "costo_total": round(args.cantidad * args.precio, 2),
    }
    with open(args.salida, "w", encoding="utf-8") as f:
        json.dump(ficha, f, indent=2, ensure_ascii=False)
    return ficha


def main() -> None:
    args = parse_args()
    ficha = generar_ficha(args)
    print(f"Ficha guardada en {args.salida}")
    print(json.dumps(ficha, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

