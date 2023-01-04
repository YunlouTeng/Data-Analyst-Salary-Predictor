#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 16:24:44 2022

@author: lavine
"""

import os
import pandas as pd

def read_folder(csv_folder):
   files = os.listdir(csv_folder)
   df = []
   for f in files:
     print(f)
     csv_file = csv_folder + "/" + f
     df.append(pd.read_csv(csv_file))
   df_full = pd.concat(df, ignore_index=True)
   return df_full