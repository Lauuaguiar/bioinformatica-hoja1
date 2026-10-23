"""Ejercicio 3: La COVID-19.

Lista los genes del genoma de referencia del SARS-CoV-2 (NC_045512)
con sus coordenadas, ignorando el resto de características.
"""

from Bio import Entrez, SeqIO

from comun import RESULTADOS

ACCESO = "NC_045512"

# 1. Descarga en formato GenBank
descarga = Entrez.efetch(db="nucleotide", id=ACCESO, rettype="gb", retmode="text")
registro = SeqIO.read(descarga, "genbank")
descarga.close()
SeqIO.write(registro, RESULTADOS / f"{ACCESO}.gb", "genbank")

print(f"{registro.id}: {registro.description}\n")

# 2-3. Recorrer las características quedándonos solo con los genes
genes = [f for f in registro.features if f.type == "gene"]

# 4-5. Nombre del gen y coordenadas (inicio en base 1, como en GenBank)
print(f"{'Nº':>3}  {'Gen':<10}{'Inicio':>8}{'Fin':>8}")
for i, gen in enumerate(genes, start=1):
    nombre = gen.qualifiers.get("gene", ["(sin nombre)"])[0]
    inicio = int(gen.location.start) + 1
    fin = int(gen.location.end)
    print(f"{i:>3}  {nombre:<10}{inicio:>8}{fin:>8}")

print(f"\nTotal de genes: {len(genes)}")
