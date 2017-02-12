"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2
import thinkplot
import nsfg
import relay


def PmfMean(pmf):
    """Returns the mean of the pmf.

    pmf: Pmf object

    returns: mean of the pmf
    """

    return sum([(x * p) for x, p in pmf.Items()])


def PmfVar(pmf):
    """Returns the variance of the pmf.

    pmf: Pmf object

    returns: variance of the pmf
    """

    mean = PmfMean(pmf)

    return sum([((x-mean)**2 * p) for x, p in pmf.Items()])
    

def Diffs(t):
    """List of differences between the first elements and others.

    t: list of numbers
    
    returns: list of numbers
    """
    first = t[0]
    rest = t[1:]
    diffs = [first - x for x in rest]
    return diffs


def PairWisePregLngthDiff():
    """Calculate pairwise differences for children of the same mother.
    """
    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome == 1]
    live_dict = nsfg.MakePregMap(live)

    diffs = []

    for caseid, indices in live_dict.items():
        lengths = live.loc[indices].prglngth.values
        if(len(lengths) > 1):
            diffs.extend(Diffs(lengths))

    mean = thinkstats2.Mean(diffs)
    print('Mean difference between pairs', mean)

    pmf = thinkstats2.Pmf(diffs)
    thinkplot.Hist(pmf, align='center')
    thinkplot.Show(xlabel='Difference in weeks',
                   ylabel='PMF')


def ObservedPmf(pmf, observer_speed, label=''):
    new_pmf = pmf.Copy(label=label)

    for s, p in pmf.Items():
        new_pmf.Mult(s, abs(s-observer_speed))
        
    new_pmf.Normalize()

    return new_pmf

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    pmf = thinkstats2.Pmf([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6])

    assert(pmf.Mean() == PmfMean(pmf))
    assert(pmf.Var() == PmfVar(pmf))

    PairWisePregLngthDiff();

    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)

    speeds = relay.BinData(speeds, 3, 12, 100)

    pmf = thinkstats2.Pmf(speeds, 'speeds')

    new_pmf = ObservedPmf(pmf, 7.5, 'observed')

    thinkplot.PrePlot(1)
    thinkplot.Pmfs([pmf, new_pmf])
    thinkplot.Show(xlabel='mph', ylabel='probability', axis=[2,13,0,0.06])

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
