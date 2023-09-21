#!/bin/bash
wget https://storage.googleapis.com/dm_alphamissense/AlphaMissense_hg19.tsv.gz
tabix -b 2 -e 2 -s 1 -c '#' AlphaMissense_hg19.tsv.gz
