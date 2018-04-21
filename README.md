# F3: Freeling Fast and Furious

Using Freeling 4's  web-services with a Python or shell client (instead of using the Python API).

Starts the web service with options given in a config file and runs Freeling on a directory.

These are wrappers to Freeling's `analyzer` and `analyzer_client` programs.

Those programs can also be used directly from the shell (see below)

## Shell client

### Requirements

- Freeling 4 at path given in script itself 

### Usage

    ./main.sh PORT INDIR OUTDIR

(Do `chmod +x main.sh` if the file was not executable)

## Python client:

### Requirements

- Freeling 4 at the paths given in the config file `(./config/oconfig.py)`
- psutil

### Usage:

    python3 main3.py input_dir output_dir

or 

    python2 main2.py input_dir output_dir

##  Using _analyze_ and _analyzer_client_ directly from the shell

See Freeling's [doc](https://talp-upc.gitbooks.io/freeling-4-0-user-manual/content/analyzer.html)
 
For example, start the server with:

    analyze --server on -p 50000 -f es.cfg --outlv semgraph --output xml
    
Run a client with:

    analyzer_client 50000 input output

