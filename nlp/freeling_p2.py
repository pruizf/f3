"""
Interaction with Freeling web service
"""

__author__ = 'Pablo Ruiz'
__date__ = '16/01/18'
__email__ = 'pabloruizfabo@gmail.com'


import codecs
import os
import psutil
import re
import subprocess
import sys
import time


# manage sys.path
import inspect
here = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
sys.path.append(here)
sys.path.append(os.path.join(here, os.pardir))


from config import oconfig as oc


def check_server(port=oc.fl_port):
    """
    Check if Freeling server is running on port
    """
    flprocs = [p for p in psutil.process_iter()
               if p.name() == "analyze"]
    if len(flprocs) > 0:
        print("\n- Freeling server already started\n")
        return True
    return False


def start_server_if_down():
    """
    Start Freeling server.
    """
    server_started = check_server()
    waited = 0
    interval = 1
    while not server_started:
        for op in oc.fl_options:
            if op not in oc.fl_server:
                oc.fl_server.append(op)
        comstr = "{} {} &".format(oc.anaser, " ".join(oc.fl_server))
        if oc.DBG:
            print("\n- Start server with: [{}]\n".format(comstr))
        os.system(comstr)
        if not waited % 10:
             print("- Waiting for server to start")
        time.sleep(interval)
        waited += interval
        server_started = check_server()


def stop_freeling_server():
    """
    Stop the Freeling server based on running process names
    """
    flprocs = [p for p in psutil.process_iter()
               if p.name() == "analyzer"]
    for flp in flprocs:
        flp.terminate()


def clean_fl_naf_output(st):
    """
    Remove extra info around the XML response, that will break XML
    """
    cleanout = re.sub(r'<OUTPUT SRC.+?\">\n', '', st)
    cleanout = re.sub(r'\n</OUTPUT>', '', cleanout)
    return cleanout


def run_fl_client_file(infn, outfn=None):
    """
    Run a FreeLing client on a file, return as a string.
    If config asks for it, write out to a file.
    @return: string with Freeling response
    @rtype: str
    """
    port = oc.fl_port
    if os.path.isfile(infn):
        p = subprocess.Popen([oc.anacli, str(port), infn], stdout=subprocess.PIPE)
        out, err = p.communicate()
        cleanout = clean_fl_naf_output(out)
        if oc.log_nlp:
            assert outfn is not None
            with codecs.open(outfn, "w", "utf8") as ofd:
                ofd.write(cleanout.decode("utf8"))
    return cleanout


def run_fl_client_dir(idir, odir, noclobber, keeplist=("*")):
    """
    Run a Freeling client on a directory.
    @return: filename and Freeling response for file, as strings
    @rtype: tuple
    """
    if oc.DBG:
        print(u"- Running dir {}\n  Total: {} files\n".format(
            os.path.realpath(idir.decode("utf8")),
            len(os.listdir(idir))))
    for fn in sorted(os.listdir(idir)):
        # to skip bad files (we have this naming convention)
        if keeplist[0] != "*" and fn not in keeplist:
            continue
        if fn.startswith("__"):
            continue
        ffn = os.path.join(idir, fn)
        if os.stat(ffn).st_size == 0:
            if oc.DBG:
                print(u"  - Skip empty file [{}]".format(
                      os.path.realpath(ffn.decode("utf8"))))
            continue
        ofn = os.path.join(odir, "".join((os.path.splitext(fn)[0], ".naf")))
        # skip dones
        if noclobber and os.path.exists(ofn) and os.stat(ffn).st_size > 0:
            if oc.DBG:
                print(u"  - Skip done file [{}]".format(
                      os.path.realpath(ffn.decode("utf8"))))
            continue
        # run
        if oc.DBG:
            print(u"  fl: {}".format(os.path.basename(ffn.decode("utf8"))))
        out = run_fl_client_file(ffn, ofn)
        yield fn, out
