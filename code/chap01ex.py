"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. impo
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

from collections import defaultdict
import numpy as np
import sys
import nsfg
import thinkstats2


def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):
    """Reads the NSFG pregnancy data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    CleanFemResp(df)
    return df


def CleanFemResp(df):
    """Recodes variables from the pregnancy frame.

    df: DataFrame
    """
    na_vals = [97, 98, 99]


def MakeRespMap(df):
    """Make a map from caseid to list of preg indices.

    df: DataFrame

    returns: dict that maps from caseid to list of indices into preg df
    """
    d = defaultdict(list)
    for index, caseid in df.caseid.iteritems():
        d[caseid].append(index)
    return d

def ValidatePregNum(resp):
	preg = nsfg.ReadFemPreg()
	preg_map = nsfg.MakePregMap(preg)

	for index, pregnum in resp.pregnum.iteritems():
		caseid = resp.caseid[index]
		indices = preg_map[caseid]

		# check that pregnum from the respondent file equals
		# the number of records in the pregnancy file
		if len(indices) != pregnum:
			print(caseid, len(indices), pregnum)
			return False

	return True

def main(script):
    """Tests the functions in this module.

    script: string script name
    """

    resp = ReadFemResp()

    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)
    assert(ValidatePregnum(resp))

    print('%s: All tests passed.' % script)

if __name__ == '__main__':
    main(*sys.argv)
