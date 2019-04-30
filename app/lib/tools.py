#!/usr/bin/env python3

# @FileName : tools.py
# @作者 : Liu
# @日期 : 2019年04月29日
# @时间 : 15时27分

import pandas as pd


def data_contrast(mysql, username, password):
    data = mysql.get_oneline(username)
    df = pd.DataFrame(list(data), columns=['username', 'password'])
    data = df[df['password'] == password]
    return not data.empty
