

![UTN](https://transmedia.frba.utn.edu.ar/img/logo_alta.png)

# TP Bioinformatica


El caso que elegimos para analizar es la enfermedad de Huntington, la cual se manifiesta debido a una mutacion en el gen HTT.

[HTT mRNA NCBI](https://www.ncbi.nlm.nih.gov/nuccore/NM_001388492.1)
NCBI Reference Sequence: `NM_001388492.1`

## _Ejercicio 1_
A partir del archivo GenBank descargado de la pagina NCBI (_sequence.gb_), transcribe la secuencia en un formato FASTA (_HTT.fasta_).


```sh
py ejercicio1/main.py
```

## _Ejercicio 2_
A partir del archivo GenBank descargado de la pagina NCBI, realiza un BLAST de la secuencia (_blast_result.xml_).
Esto lo realizamos ejecutando el BLAST de manera remota desde la pagina de NCBI.
Lo que logramos con esto es obtener una serie de secuencias similares a las de este gen, con esto se puede inferir relaciones funcionales y evolutivas entre distintas secuencias.

Con nuestro resultado podemos ver el parecido con distintos organismos tales como
 - Mandrillus leucophaeus (mono)
 - Sapajus apella (mono)
 - Lemur catta (lemur)
 

``TODO chequear interpretacion``

```sh
py ejercicio2/main.py
```

## Ejercicio 3
Descargamos las secuencias de los siguientes organismos
| Organismo | Reference | Link |
| ------ | ---- | -----|
| Mandrillus leucophaeus | `XM_012002185` | https://www.ncbi.nlm.nih.gov/nuccore/XM_012002185 |
| Sapajus apella | `XM_032254021` |https://www.ncbi.nlm.nih.gov/nuccore/XM_032254021 |
| Lemur catta | `XM_045528220` | https://www.ncbi.nlm.nih.gov/nuccore/XM_045528220 | 

Para ejecutar secuenciamiento multiple 
[Click aqui](https://www.ebi.ac.uk/Tools/services/web/toolresult.ebi?jobId=clustalo-I20220507-234725-0072-42290853-p2m)

``TODO agregar interpretacion``
