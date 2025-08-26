# amr-scout (MVP)

Et lite CLI-verktøy som (etter hvert) leser et genom-FASTA og rapporterer sannsynlig antibiotika-resistens basert på AMR-gener/mutasjoner.

## Plan
Fase 1: BLAST av genom mot AMR-gen-database → mappe funn til antibiotikaklasser → enkel rapport.

## Kjapp start
```bash
python -m amr_scout.cli --help
