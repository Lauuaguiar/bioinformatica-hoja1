"""Ejercicio 4: Bacterias, a la caza de proteínas de resistencia.

Descarga el plásmido pT181 de Staphylococcus aureus, localiza sus regiones
CDS y las traduce a proteínas.

Nota: el enunciado indica el código NC_001371, pero en el NCBI ese código
corresponde al plásmido ColE1 de Escherichia coli (y es un registro CON sin
secuencia). El plásmido pT181 de S. aureus es NC_001393.
"""

from Bio import Entrez, SeqIO
from Bio.Data import CodonTable
from Bio.SeqRecord import SeqRecord

from comun import RESULTADOS

ACCESO = "NC_001393"

# Términos habituales en las anotaciones de genes de resistencia
PALABRAS_RESISTENCIA = (
    "resistance", "efflux", "tetracycline", "lactamase",
    "aminoglycoside", "chloramphenicol", "erythromycin", "vancomycin",
)

# "gbwithparts" garantiza que el registro incluya la secuencia completa
descarga = Entrez.efetch(db="nucleotide", id=ACCESO, rettype="gbwithparts", retmode="text")
plasmido = SeqIO.read(descarga, "genbank")
descarga.close()
SeqIO.write(plasmido, RESULTADOS / f"{ACCESO}.gb", "genbank")

print(f"{plasmido.id}: {plasmido.description} ({len(plasmido.seq)} pb)\n")

proteinas = []
for cds in (f for f in plasmido.features if f.type == "CDS"):
    gen = cds.qualifiers.get("gene", ["?"])[0]
    producto = cds.qualifiers.get("product", ["desconocido"])[0]
    id_proteina = cds.qualifiers.get("protein_id", [gen])[0]

    # extract() respeta la hebra y las uniones; tabla 11 = código bacteriano.
    # cds=True traduce los codones de inicio alternativos (TTG, GTG) como M.
    adn = cds.extract(plasmido.seq)
    try:
        proteina = adn.translate(table=11, cds=True)
    except CodonTable.TranslationError:
        # Pseudogenes: tienen paradas internas, se traduce hasta la primera
        proteina = adn.translate(table=11, to_stop=True)

    # Comprobación con la traducción que trae anotada el propio GenBank
    anotada = cds.qualifiers.get("translation", [None])[0]
    if "pseudo" in cds.qualifiers:
        coincide = "pseudogén, sin traducción anotada"
    else:
        coincide = "sí" if anotada == str(proteina) else "no"

    es_resistencia = any(p in producto.lower() for p in PALABRAS_RESISTENCIA)
    resistencia = "  <-- PROTEÍNA DE RESISTENCIA" if es_resistencia else ""
    print(f"{id_proteina} | gen {gen} | {producto}{resistencia}")
    print(f"  Posición {cds.location} | {len(proteina)} aa | coincide con la anotación: {coincide}")
    print(f"  {proteina}\n")

    proteinas.append(
        SeqRecord(proteina, id=id_proteina, description=f"{gen} {producto} [{plasmido.id}]")
    )

salida = RESULTADOS / "pT181_proteinas.fasta"
SeqIO.write(proteinas, salida, "fasta")
print(f"{len(proteinas)} proteínas guardadas en {salida}")
