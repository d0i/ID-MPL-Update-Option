#!/usr/bin/env python

"""
make option string of MPL parameter option (for udhcpd of busybox)
"""

import types

def mkuint8hex(v):
    if not isinstance(v, types.IntType) or v < 0 or v > 255:
        raise ValueError
    return "%02x"%(v,)

def mkuint16hex(v):
    if not isinstance(v, types.IntType) or v < 0 or v > 65535:
        raise ValueError
    return "%04x"%(v,)
        

def mkoptstring(params):
    rstrL = []
    if params["P"]:
        rstrL.append("80")
    else:
        rstrL.append("00")
    rstrL.append(mkuint8hex(params["TUNIT"]))
    rstrL.append(mkuint16hex(params["SE_LIFETIME"]))
    rstrL.append(mkuint8hex(params["DM_K"]))
    rstrL.append(mkuint16hex(params["DM_IMIN"]))
    rstrL.append(mkuint16hex(params["DM_IMAX"]))
    rstrL.append(mkuint16hex(params["DM_T_EXP"]))
    rstrL.append(mkuint8hex(params["C_K"]))
    rstrL.append(mkuint16hex(params["C_IMIN"]))
    rstrL.append(mkuint16hex(params["C_IMAX"]))
    rstrL.append(mkuint16hex(params["C_T_EXP"]))
    if "MPL_DOMAIN_ADDR" in params:
        rstrL.append(mkipv6addrhex(params["MPL_DOMAIN_ADDR"]))
    return ''.join(rstrL)

if __name__ == '__main__':
    test_params = {
        "P": True,
        "TUNIT": 10,
        "SE_LIFETIME": 6000,
        "DM_K": 3,
        "DM_IMIN": 200,
        "DM_IMAX": 800,
        "DM_T_EXP": 3000,
        "C_K": 4,
        "C_IMIN": 50,
        "C_IMAX": 800,
        "C_T_EXP": 300
    }
    print mkoptstring(test_params)
