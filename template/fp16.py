#!/usr/bin/env python

"""
Short floating point
"""

import pdb

T_SEC=1
T_MIN=60
T_HOUR=60*T_MIN
T_DAY=24*T_HOUR
T_WEEK=7*T_DAY
T_YEAR=365*T_DAY

def e2int(mant, expo, base=2):
    return mant * (base**expo)

def time2str(ttuple):
    rL = []
    (t_year, t_week, t_day, t_hour, t_min, t_sec, t_frac) = ttuple
    if t_year > 0:
        rL.append("%d year(s)"%(t_year,))
    if t_week > 0:
        rL.append("%d week(s)"%(t_week,))
    if t_day > 0:
        rL.append("%d day(s)"%(t_day,))
    if t_hour > 0:
        rL.append("%d hour(s)"%(t_hour,))
    if t_min > 0:
        rL.append("%d min(s)"%(t_min,))
    if t_sec > 0:
        rL.append("%d second(s)"%(t_sec,))
    if t_frac > 0:
        rL.append("%d ms."%(int(t_frac * 1000),))
    return ' '.join(rL)
            
def float2time(f):
    (t_year, t_week, t_day, t_hour, t_min, t_sec, t_frac) = (0, 0, 0, 0, 0, 0, 0.0)
    if f >= T_YEAR:
        t_year = int(f/T_YEAR)
        f -= t_year*T_YEAR
    if f >= T_WEEK:
        t_week = int(f/T_WEEK)
        f -= t_week*T_WEEK
    if f >= T_DAY:
        t_day = int(f/T_DAY)
        f -= t_day*T_DAY
    if f >= T_HOUR:
        t_hour = int(f/T_HOUR)
        f -= t_hour*T_HOUR
    if f >= T_MIN:
        t_min = int(f/T_MIN)
        f -= t_min*T_MIN
    t_sec = int(f)
    t_frac = f-t_sec

    ttuple = (t_year, t_week, t_day, t_hour, t_min, t_sec, t_frac)
    return time2str(ttuple)

if __name__ == '__main__':

    import sys

    bw_total = 16
    exp_bw = 3
    man_bw = (bw_total-exp_bw)
    base=10
    #base=2
    unit=0.001 
    print '# base=%(base)d, exp_bw=%(exp_bw)d, man_bw=%(man_bw)d, unit=%(unit)f'%locals()

    if len(sys.argv) == 1:
        for expo in range(0, (1<<exp_bw)):
            fmin = e2int(1, expo, base)*unit
            fmax = e2int((1<<man_bw)-1, expo, base)*unit
            print 'expo=%d'%(expo)
            print float2time(fmin)
            print float2time(fmax)
    elif len(sys.argv) == 3:
        expo = int(sys.argv[1])
        mantissa = int(sys.argv[2])
        print float2time(e2int(mantissa, expo, base) * unit)
        es = bin(expo)[2:]
        while len(es) < exp_bw:
            es = "0"+es
        ms = bin(mantissa)[2:]
        while len(ms) < man_bw:
            ms = "0"+ms
        print 'expo=', es
        print 'mantissa=', ms
        if len(es) > exp_bw or len(ms) > man_bw:
            raise ValueError, "overflow"
        print 'hex=', hex(int(es+ms, 2))
    else:
        raise SystemError, "%s {[expo] [mantissa]}"%(sys.argv[0])

