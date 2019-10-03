# Freeling Fast and Furious

Using Freeling 4's web-services instead of the APIs. 

You can of course use them directly from the shell, with the `analyzer`and `analyzer_client` programs that are part of Freeling.

Or you can write clients (wrappers for those programs) like the Python or Bash ones in this repository (documented below). 

##  Using _analyze_ and _analyzer_client_ directly from the shell

See Freeling's [doc](https://freeling-user-manual.readthedocs.io/en/v4.1/analyzer/)
 
For example, start the server with:

    analyze --server on -p 50000 -f es.cfg --outlv semgraph --output xml
    
Run a client with:

    analyzer_client 50000 input_file output_file

Or for several files:

    for fn in $(ls "/path/to/input_dir") ; do analyzer_client 50000 \
      "/path/to/input/dir/$x" > "/path/to/output_dir/${fn%.txt}.xml; done    

## Shell client

### Requirements

- Freeling 4 at path given in script itself 

### Usage

If server is not started, set options in script and run:

    ./start_server.sh

Once server is started, run a directory:

    ./run_client.sh PORT INDIR OUTDIR

(Do `chmod +x` on the shell files if they were not executable)


## Python client:

### Requirements

- Freeling 4 at the paths given in the config file `(./config/oconfig.py)`
- psutil

### Usage:

    python3 main3.py input_dir output_dir

or 

    python2 main2.py input_dir output_dir


[[Back]](http://github.com/pruizf/corpuswk)
