# Hoja de ejercicios 1: Bioinformática con Biopython

Soluciones a los ejercicios de la hoja 1: análisis de secuencias FASTA, descargas
automáticas desde el NCBI con `Bio.Entrez`, lectura de archivos GenBank y búsqueda de
información sobre proteínas.

## Requisitos

- Python 3.9 o superior
- Biopython

```bash
pip install -r requirements.txt
```

Los ejercicios 2, 3 y 4 se conectan al NCBI, que pide un correo para identificar a quien
hace las peticiones. Defínelo antes de ejecutarlos (o edítalo en `comun.py`):

```bash
export NCBI_EMAIL="lauraaguiarperez@gmail.com"      # Linux/macOS/Git Bash
$env:NCBI_EMAIL = "lauraaguiarperez@gmail.com"      # PowerShell
```

## Ejercicios

| Script | Ejercicio | Qué hace |
|---|---|---|
| `ejercicio1_gc.py` | 1. Porcentaje GC | Lee `data/secuencias_adn.fasta`, muestra el %GC de cada secuencia, las traduce y guarda las proteínas en `resultados/ejercicio1_proteinas.fasta` con los mismos ID y descripciones. Admite otros archivos: `python ejercicio1_gc.py entrada.fasta salida.fasta` |
| `ejercicio2_sarampion.py` | 2. El sarampión | `esearch` en *nucleotide* con `Measles morbillivirus[Organism] AND refseq[filter]`, toma `IdList[0]`, lo descarga con `efetch` en FASTA y muestra la descripción y los primeros 100 nt (genoma NC_001498.1). |
| `ejercicio3_covid.py` | 3. La COVID-19 | Descarga NC_045512 en GenBank, filtra las *features* de tipo `gene` y muestra la lista numerada de genes con sus coordenadas (11 genes). |
| `ejercicio4_plasmido.py` | 4. Proteínas de resistencia | Descarga el plásmido pT181 de *S. aureus*, extrae las CDS, las traduce (tabla 11, bacteriana) y marca las de resistencia. Encuentra **Tet(K)**, una bomba de expulsión que da **resistencia a la tetraciclina**. |
| `ejercicio5_proteinas.py` | 5. Proteínas célebres | Descarga de UniProt la ficha y el FASTA de hemoglobina β, mioglobina y oxitocina y calcula su masa y su punto isoeléctrico. El informe está en [`docs/ejercicio5_proteinas.md`](docs/ejercicio5_proteinas.md). |

```bash
python ejercicio1_gc.py
python ejercicio2_sarampion.py
python ejercicio3_covid.py
python ejercicio4_plasmido.py
python ejercicio5_proteinas.py
```

Todos los archivos generados (FASTA y GenBank) se guardan en `resultados/`.

## Notas

- **Ejercicio 4:** el enunciado da el código `NC_001371`, pero en el NCBI ese registro
  corresponde al plásmido **ColE1 de *Escherichia coli*** (y es un registro CON, sin secuencia).
  El plásmido pT181 de *S. aureus* es **`NC_001393`**, y es el que usa el script.
- **Ejercicio 4:** en el RefSeq actual, *tet(K)* está anotado como pseudogén
  (`/pseudo`, tiene un codón de parada interno). El script lo traduce hasta la primera
  parada y lo indica en la salida.
- **Ejercicio 1:** las secuencias de `data/secuencias_adn.fasta` son ejemplos (la última es
  el inicio real del gen *HBB* humano). Si su longitud no es múltiplo de 3, se recortan al
  último codón completo antes de traducirlas.

## Estructura

```
├── comun.py                  # Configuración de Entrez y rutas compartidas
├── ejercicio1_gc.py ... ejercicio5_proteinas.py
├── data/secuencias_adn.fasta # Entrada del ejercicio 1
├── docs/ejercicio5_proteinas.md
└── resultados/               # Salidas generadas
```
