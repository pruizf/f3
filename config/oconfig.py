"""Overall config"""

__author__ = 'Pablo Ruiz'
__date__ = '16/01/18'
__email__ = 'pabloruizfabo@gmail.com'


import os


# basic
DBG = True
run_nlp = False  # if already have NLP results, no need to rerun
noclobber = False  # won't rewrite non-empty files in nlp directory

# result / log basedir
basedir = "/home/pablo/projects/pd/projects/lab/metrics/p/results3"

## freeling

# bin paths
anaser = "/usr/bin/analyze"
anacli = "/usr/bin/analyzer_client"

# server
fl_port = 50000
fl_server = ["--server on", "-p {}".format(fl_port)]

# config
fl_options = ["-f es.cfg",                   # modern spanish
              "--nortk",                     # the 'no...' opts are for ok tokenization
              "--nortkcon",
              "--noloc",
              "--noner",
              "--nonumb",
              "--nodate",
              "--noquant",
              "--outlv coref "               # full pipeline up to coreference
              "--output naf"]                # compatible with IXA pipes

stop_fl = False                              # kill Freeling after running batch


## logs
log_nlp = True                               # writes NAF to its own directory

