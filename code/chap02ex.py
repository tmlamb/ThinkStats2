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


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    p, x = max([(p, x) for x, p in hist.Items()])

    return x


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """

    #return sorted(hist.Items(), key=lambda tup: tup[1], reverse=True)
    #Apparently itemgetter is faster than the above?

    return sorted(hist.Items(), key=itemgetter(1), reverse=True)


def CompareFirstBabyWeight(firsts, others):
    d1 = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

    print('Mean first baby weight (lbs)', firsts.totalwgt_lb.mean())
    print('Mean other baby weight (lbs)', others.totalwgt_lb.mean())
    print('Cohen\'s d of first and other babies weight', d1)

    d2 = thinkstats2.CohenEffectSize(firsts.prglngth, others.prglngth)

    print('Mean first baby pregnancy length (weeks)', firsts.prglngth.mean())
    print('Mean other baby pregnancy length (weeks)', others.prglngth.mean())
    print('Cohen\'s d of first and other babies pregnancy length', d2)


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert(mode == 39)

    # test AllModes
    modes = AllModes(hist)
    assert(modes[0][1] == 4693)

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)

    CompareFirstBabyWeight(firsts, others)


if __name__ == '__main__':
    main(*sys.argv)
