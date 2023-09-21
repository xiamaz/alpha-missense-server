import pysam
import re
from fastapi import FastAPI, HTTPException


app = FastAPI()

tbx = pysam.TabixFile("./AlphaMissense_hg19.tsv.gz")

header = ["CHROM", "POS", "REF", "ALT", "genome", "uniprot_id", "transcript_id", "protein_variant", "am_pathogenicity", "am_class"]


@app.get("/{query}")
async def root(query):
    if m := re.search("(chr[XxYymt0-9]+)[ :-](\d+)", query):
        predictions = []
        chrname = m.group(1)
        posa = int(m.group(2)) - 1
        posb = int(m.group(2))
        for row in tbx.fetch(chrname, posa, posb):
            entry = dict(zip(header, row.split("\t")))
            predictions.append(entry)
        return predictions
    raise HTTPException(status_code=400, detail="Malformed query, expects chr<name>:<pos>")
