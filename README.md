# AlphaMissense Server

Super simple inofficial alpha missense server which can be queried with chromosomal
positions.

This requires `tabix` to be installed in order to index the tsv file.

Download the hg19 tsv.gz and index it with the provided `download.sh` script.

Run with:

```
$ uvicorn server:app --host "valid hosts"
```

## References

Jun Cheng et al. ,Accurate proteome-wide missense variant effect prediction with AlphaMissense.Science0,eadg7492DOI:10.1126/science.adg7492
