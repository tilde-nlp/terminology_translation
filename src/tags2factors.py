#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Toms Bergmanis
# Created Date: July 2020
# =============================================================================
"""Convert data with terms indicated using tags to factors. 
<b> begining of source term 
<t> target term
<\\t> end of target term."""

import sys

for line in sys.stdin:
    lcontent = line.strip().split()
    term = False
    translation = False
    factors = []

    for e in lcontent:
        if e == "<b>":
            term = True
        elif e == "<t>":
            term = False
            translation = True
        elif e == "<\\t>":
            translation = False
        else:
            if term == True:
                factors.append("S")
            elif translation:
                factors.append("T")
            else:
               factors.append("W")
    print(" ".join(factors))

