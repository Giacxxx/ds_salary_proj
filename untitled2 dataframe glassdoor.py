#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 12:55:38 2020

@author: gm
"""


import glassdoor_scraper as gs
import pandas as pd

path= "/Users/gm/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',3,False,path, 15)
