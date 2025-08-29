# 🧬 amr-scout

Et lite CLI-verktøy (MVP) for å skanne bakterielle genomer og rapportere sannsynlig antibiotikaresistens basert på kjente AMR-gener og mutasjoner.  
🎯 Fokus: diagnostikk fremfor taksonomi – målrettet antibiotikabruk.

---

## 🚀 Status
- MVP-skjelett på plass ✅
- Input-validering fungerer (genom + regler) ✅
- Neste steg: koble inn **BLAST+** for genmatching

---

## 📦 Installasjon
Klon repoet og sett opp et virtuelt miljø:

```bash
git clone https://github.com/camillastokland28-dotcom/amr-scout.git
cd amr-scout
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # (kommer snart)
