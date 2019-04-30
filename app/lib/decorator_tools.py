#!/usr/bin/env python3

# @FileName : decorator_tools.py
# @作者 : Liu
# @日期 : 2019年04月29日
# @时间 : 16时15分

'''
暂时没有用到
'''

def list_to_dict(fun):
    def to_json(*args, **kwargs):
        all_data = fun(*args, **kwargs)
        columns = args[0].cursor.description
        for i in all_data:
            for index, value in enumerate(columns):
                print((value[0], i[index]))
        return fun(*args, **kwargs)

    return to_json
