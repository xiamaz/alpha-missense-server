# AlphaMissense Server

Super simple alpha missense server which can be queried with chromosomal
positions.

This requires `tabix` to be installed in order to index the tsv file.

Run with:

```
$ uvicorn server:app --host "valid hosts"
```
