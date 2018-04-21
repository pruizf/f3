#!/usr/bin/env bash

SERVER=/usr/bin/analyze

port=50000
#options="-f es.cfg --outlv semgraph --output xml"
options="-f es.cfg --outlv coref --output naf"

# start server if needed
if [[ -z $(netstat -tlnp | grep ":$port") ]] ; then
  $SERVER --server on -p $port $options &
fi
