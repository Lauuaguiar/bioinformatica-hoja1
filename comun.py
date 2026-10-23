"""Utilidades compartidas por los ejercicios que se conectan al NCBI."""

import os
from pathlib import Path

from Bio import Entrez

# El NCBI pide identificarse con un correo. Defínelo en la variable de entorno
# NCBI_EMAIL o cámbialo aquí directamente.
Entrez.email = os.environ.get("NCBI_EMAIL", "tu_correo@ejemplo.com")

RAIZ = Path(__file__).resolve().parent
DATOS = RAIZ / "data"
RESULTADOS = RAIZ / "resultados"
RESULTADOS.mkdir(exist_ok=True)
