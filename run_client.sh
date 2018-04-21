#!/usr/bin/env bash

port="$1"
indir="$2"
outdir="$3"

CLIENT=/usr/bin/analyzer_client

# run directory
[[ ! -d "$outdir" ]] && mkdir "$outdir"

for fn in $(ls "$indir") ; do
  "$CLIENT" $1 <"$indir/$fn" > "$outdir/${fn%.txt}.xml"
done