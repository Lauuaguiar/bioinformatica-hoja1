"""Ejercicio 5: Algunas proteínas "célebres".

Descarga de UniProt la ficha y el FASTA de tres proteínas humanas de la
lista (hemoglobina, mioglobina y oxitocina), muestra un resumen y calcula
algunas propiedades con Biopython. El informe completo está en
docs/ejercicio5_proteinas.md.
"""

import json
from urllib.request import urlopen

from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

from comun import RESULTADOS

UNIPROT = "https://rest.uniprot.org/uniprotkb"

PROTEINAS = {
    "Hemoglobina (subunidad beta)": "P68871",
    "Mioglobina": "P02144",
    "Oxitocina (precursor oxitocina-neurofisina 1)": "P01178",
}


def descargar_fasta(acceso):
    destino = RESULTADOS / f"{acceso}.fasta"
    with urlopen(f"{UNIPROT}/{acceso}.fasta") as respuesta:
        destino.write_bytes(respuesta.read())
    return SeqIO.read(destino, "fasta")


def descargar_ficha(acceso):
    with urlopen(f"{UNIPROT}/{acceso}.json") as respuesta:
        return json.load(respuesta)


def funcion(ficha):
    for comentario in ficha.get("comments", []):
        if comentario["commentType"] == "FUNCTION":
            return comentario["texts"][0]["value"]
    return "(sin descripción)"


registros = []
for nombre, acceso in PROTEINAS.items():
    ficha = descargar_ficha(acceso)
    registro = descargar_fasta(acceso)
    registros.append(registro)

    analisis = ProteinAnalysis(str(registro.seq))
    gen = ficha["genes"][0]["geneName"]["value"]
    nombre_uniprot = ficha["proteinDescription"]["recommendedName"]["fullName"]["value"]

    print("=" * 70)
    print(f"{nombre}  [UniProt {acceso}]")
    print(f"Nombre oficial: {nombre_uniprot} | Gen: {gen} | "
          f"Organismo: {ficha['organism']['scientificName']}")
    print(f"Longitud: {len(registro.seq)} aa | "
          f"Masa molecular: {analisis.molecular_weight() / 1000:.1f} kDa | "
          f"Punto isoeléctrico: {analisis.isoelectric_point():.2f}")
    print(f"Función: {funcion(ficha)}")
    print(f"Secuencia:\n{registro.seq}\n")

SeqIO.write(registros, RESULTADOS / "ejercicio5_proteinas.fasta", "fasta")
print(f"FASTA combinado guardado en {RESULTADOS / 'ejercicio5_proteinas.fasta'}")
