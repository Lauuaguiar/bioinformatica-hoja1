# Ejercicio 5: Algunas proteínas "célebres"

Proteínas elegidas: **hemoglobina**, **mioglobina** y **oxitocina** (todas humanas).
Las dos primeras están relacionadas: ambas son globinas que transportan o almacenan
oxígeno. La oxitocina sirve de contraste porque es una hormona peptídica.

Los archivos FASTA se descargan de [UniProt](https://www.uniprot.org) con
`ejercicio5_proteinas.py` y se guardan en `resultados/`:

| Proteína | UniProt | Gen | Longitud | Masa | FASTA |
|---|---|---|---|---|---|
| Hemoglobina, subunidad β | [P68871](https://www.uniprot.org/uniprotkb/P68871) | *HBB* (cromosoma 11) | 147 aa | ~16,0 kDa | `resultados/P68871.fasta` |
| Mioglobina | [P02144](https://www.uniprot.org/uniprotkb/P02144) | *MB* (cromosoma 22) | 154 aa | ~17,2 kDa | `resultados/P02144.fasta` |
| Oxitocina-neurofisina 1 (precursor) | [P01178](https://www.uniprot.org/uniprotkb/P01178) | *OXT* (cromosoma 20) | 125 aa | ~12,7 kDa | `resultados/P01178.fasta` |

`resultados/ejercicio5_proteinas.fasta` reúne las tres secuencias en un solo archivo.

---

## 1. Hemoglobina

- **Función:** transporta el O₂ desde los pulmones a los tejidos y devuelve parte del
  CO₂ y de los protones a los pulmones. Se encuentra en los glóbulos rojos.
- **Estructura:** es un **tetrámero** formado por dos cadenas α (*HBA1/HBA2*) y dos cadenas β
  (*HBB*), es decir, α₂β₂ en el adulto (HbA). Cada cadena contiene un grupo **hemo** con
  un ion Fe²⁺ que se une a una molécula de O₂, así que cada hemoglobina transporta hasta 4 O₂.
- **Cooperatividad:** cuando una subunidad se une al O₂, las demás aumentan su afinidad.
  Por eso la curva de saturación es **sigmoidea**. El pH, el CO₂ y el 2,3-BPG reducen la
  afinidad (efecto Bohr), lo que facilita que libere el O₂ en los tejidos que más lo necesitan.
- **Interés clínico:** la mutación puntual Glu6Val de la cadena β (codón GAG → GTG)
  produce la hemoglobina S, responsable de la **anemia falciforme**. Las talasemias se deben
  a una síntesis reducida de cadenas α o β. La HbA1c (hemoglobina glicada) se usa para
  vigilar la diabetes.

## 2. Mioglobina

- **Función:** **almacena O₂ en el músculo** (esquelético y cardíaco) y facilita su
  difusión hasta las mitocondrias. También actúa como nitrito reductasa (produce NO) y
  protege frente a especies reactivas de oxígeno.
- **Estructura:** es un **monómero** de 154 aminoácidos con 8 hélices α (A–H) y un solo
  grupo hemo. Fue la **primera proteína cuya estructura 3D se resolvió por cristalografía
  de rayos X** (John Kendrew, 1958, mioglobina de cachalote), lo que le valió el Premio
  Nobel de Química en 1962, compartido con Max Perutz por la hemoglobina.
- **Comparación con la hemoglobina:** al tener una sola subunidad no presenta cooperatividad.
  Su curva de saturación es **hiperbólica** y su afinidad por el O₂ es mayor, de modo que
  recoge el oxígeno que suelta la hemoglobina. Las dos proteínas comparten el plegamiento
  de las globinas porque tienen un origen evolutivo común.
- **Curiosidades:** da el color rojo a la carne. Los mamíferos buceadores (ballenas,
  focas) tienen concentraciones muy altas de mioglobina. En el diagnóstico clínico, su
  aparición en sangre u orina indica daño muscular (rabdomiólisis, infarto).

## 3. Oxitocina

- **Qué es:** una **hormona peptídica de solo 9 aminoácidos** (CYIQNCPLG-NH₂) con un
  puente disulfuro entre las dos cisteínas. Se sintetiza en el hipotálamo (núcleos
  supraóptico y paraventricular) y se libera desde la **neurohipófisis**.
- **Precursor:** el gen *OXT* codifica una preproteína de 125 aa (la secuencia del FASTA)
  formada por el péptido señal, la oxitocina, una señal de corte (GKR) y la
  **neurofisina 1**, que transporta la hormona por el axón. El nonapéptido maduro se
  ve dentro de la secuencia: `...SACYIQNCPLGGKRAAPD...`.
- **Funciones:**
  - Provoca las **contracciones uterinas** durante el parto (su análogo sintético se usa
    para inducirlo o acelerarlo).
  - Provoca la **eyección de leche** durante la lactancia (reflejo de succión).
  - Interviene en la conducta social: vínculo madre-hijo, confianza y apego. Por eso se
    la conoce popularmente como la "hormona del amor".
- **Dato:** fue la primera hormona peptídica sintetizada químicamente (Vincent du Vigneaud,
  1953). Le valió el Premio Nobel de Química en 1955. Está muy relacionada con la
  **vasopresina** (ADH): las dos se diferencian solo en 2 aminoácidos y sus genes están
  contiguos en el cromosoma 20.

---

## Fuentes

- UniProtKB: entradas P68871, P02144 y P01178 (función, secuencia y anotaciones).
- NCBI Gene: *HBB* (ID 3043), *MB* (ID 4151) y *OXT* (ID 5020).
- Nelson, D. L. y Cox, M. M. *Lehninger. Principios de Bioquímica*, cap. 5 (proteínas que unen oxígeno).
