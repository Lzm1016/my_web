#!/usr/bin/env python3

# @FileName : test.py
# @作者 : Liu
# @日期 : 2019年04月29日
# @时间 : 17时14分

import pandas as pd

df = pd.DataFrame([[1, 2]], columns=['id', 'age'])
print(df[df["id"] == 1].empty)
