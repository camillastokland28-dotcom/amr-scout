#!/usr/bin/env python3
import argparse, sys
from pathlib import Path

def main():
    p = argparse.ArgumentParser(prog="amr-scout", description="Scan genome FASTA against AMR rules (MVP skeleton).")
    sub = p.add_subparsers(dest="cmd", required=True)

    scan = sub.add_parser("scan", help="(MVP) Validate inputs and show planned steps")
    scan.add_argument("--genome", type=Path, required=True, help="Genome FASTA (RefSeq .fna/.fa)")
    scan.add_argument("--amr-db", type=Path, required=False, help="AMR genes FASTA (to be used with BLAST later)")
    scan.add_argument("--rules", type=Path, default=Path("rules/amr_map.csv"), help="CSV mapping genes -> antibiotic classes")

    args = p.parse_args()

    if args.cmd == "scan":
        ok = True
        if not args.genome.exists():
            print(f"[ERR] Genome not found: {args.genome}", file=sys.stderr); ok=False
        if args.amr_db and not args.amr_db.exists():
            print(f"[ERR] AMR DB not found: {args.amr_db}", file=sys.stderr); ok=False
        if not args.rules.exists():
            print(f"[ERR] Rules CSV not found: {args.rules}", file=sys.stderr); ok=False

        if not ok: sys.exit(1)

        print("[OK] Inputs validated.")
        print("[PLAN] Next steps for MVP:")
        print("  1) makeblastdb -in <AMR_FASTA> -dbtype nucl")
        print("  2) blastn -query <GENOME_FASTA> -db <AMR_DB> -outfmt 6 -perc_identity 90 -qcov_hsp_perc 80")
        print("  3) parse hits -> map gene IDs via rules CSV -> report antibiotic classes")
        print("  4) (later) SNP rules (gyrA, rpoB, pbp...)")

if __name__ == "__main__":
    main()
