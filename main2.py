"""
To run Freeling web service on a directory, Py2 version.
Uses config options in L{config.oconfig}
"""

__author__ = 'Pablo Ruiz'
__date__ = '21/04/18'
__email__ = 'pabloruizfabo@gmail.com'

import os
import sys
from time import sleep

from nlp import freeling_p3 as fl


def usage():
    print("USAGE:\n{} input_dir output_dir".format(sys.argv[0]))


if __name__ == "__main__":
    # IO
    try:
        indir = sys.argv[1]
        outdir = sys.argv[2]
    except IndexError:
        usage()
        sys.exit()
    if len(sys.argv) > 1 and sys.argv[1] == "-h":
        usage()
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    # Process files
    fl.start_server_if_down()
    sleep(3)
    # set last argumnent to True to skip already done files
    runner = fl.run_fl_client_dir(indir, outdir, False)
    # run the runner (generator)
    for ff in runner:
        pass
