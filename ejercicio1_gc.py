"""Ejercicio 1: Porcentaje GC.

Lee un FASTA con varias secuencias de ADN, muestra el %GC de cada una,
las traduce a aminoácidos y guarda las proteínas en un nuevo FASTA
conservando los identificadores y descripciones originales.

Uso:
    python ejercicio1_gc.py [entrada.fasta] [salida.fasta]
"""

import sys

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import gc_fraction

from comun import DATOS, RESULTADOS


def main():
    entrada = sys.argv[1] if len(sys.argv) > 1 else DATOS / "secuencias_adn.fasta"
    salida = sys.argv[2] if len(sys.argv) > 2 else RESULTADOS / "ejercicio1_proteinas.fasta"

    proteinas = []
    for registro in SeqIO.parse(entrada, "fasta"):
        gc = gc_fraction(registro.seq) * 100
        print(f"{registro.id}: {len(registro.seq)} nt, GC = {gc:.2f}%")

        # Se recorta al último codón completo para evitar avisos de Biopython
        longitud = len(registro.seq) - len(registro.seq) % 3
        proteina = registro.seq[:longitud].translate()
        print(f"  Proteína: {proteina}")

        proteinas.append(
            SeqRecord(proteina, id=registro.id, description=registro.description)
        )

    SeqIO.write(proteinas, salida, "fasta")
    print(f"\n{len(proteinas)} secuencias de aminoácidos guardadas en {salida}")


if __name__ == "__main__":
    main()
