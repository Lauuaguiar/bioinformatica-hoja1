"""Ejercicio 2: El sarampión.

Descarga automáticamente el genoma oficial (RefSeq) del virus del sarampión.
"""

from Bio import Entrez, SeqIO

from comun import RESULTADOS

# 1. Búsqueda en "nucleotide" restringida a la base de datos secundaria RefSeq
busqueda = Entrez.esearch(
    db="nucleotide",
    term="Measles morbillivirus[Organism] AND refseq[filter]",
)
resultado = Entrez.read(busqueda)
busqueda.close()

# 2. Primer ID de la lista
id_genoma = resultado["IdList"][0]
print(f"Resultados encontrados: {resultado['Count']}, usando el ID {id_genoma}")

# 3. Descarga del registro en formato FASTA
descarga = Entrez.efetch(db="nucleotide", id=id_genoma, rettype="fasta", retmode="text")
registro = SeqIO.read(descarga, "fasta")
descarga.close()

SeqIO.write(registro, RESULTADOS / "sarampion_genoma.fasta", "fasta")

# 4. Descripción y primeros 100 nucleótidos
print(f"Descripción: {registro.description}")
print(f"Longitud: {len(registro.seq)} nt")
print(f"Primeros 100 nucleótidos:\n{registro.seq[:100]}")
