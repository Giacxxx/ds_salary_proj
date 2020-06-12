#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 12:48:05 2020

@author: gm
"""


import glassdoor_scraper2 as gs
import pandas as pd

path = "/Users/gm/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 100, False, path, 15)



