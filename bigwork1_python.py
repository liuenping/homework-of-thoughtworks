#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:lep time:2020/10/15

import pandas as pd
import csv
import os

# 一共有多少用户
def user_nums():
    df1 = pd.read_csv(os.path.join(root_dir,'tags.csv'))
    df2 = pd.read_csv(os.path.join(root_dir,'ratings.csv'))
    user1 = list(df1['userId'].unique())
    user2 = list(df2['userId'].unique())
    return len(set(user1 + user2))

# 一共有多少电影
def movie_nums():
    df = pd.read_csv(os.path.join(root_dir,'movies.csv'))
    return len(set(df['movieId']))

# 一共有多少种类型的电影
def movie_gen():
    df = pd.read_csv(os.path.join(root_dir,'movies.csv'))
    movie_genres = df['genres'].str.split('|')
    nums_type = []
    for g in movie_genres:
        if '(' not in g[0]:
            nums_type += g
    return len(set(nums_type))

# 一共有多少电影没有外部链接
def nolink():
    df = pd.read_csv(os.path.join(root_dir,'links.csv'))
    t0 = df['imdbId'].count()
    t1 = df['tmdbId'].count()
    return t0-t1

# 2018年一共有多少人进行过电影评分
def rate_user_2018():
    df = pd.read_csv(os.path.join(root_dir, 'ratings.csv'))
    df['year'] = pd.to_datetime(df['timestamp'], unit='s').dt.year
    df_2018 = df[df['year']==2018]
    return len(set(df_2018['userId']))

if __name__ == '__main__':
    root_dir = r'E:\zybank\tech_train\pre\ml-25m'
    files = os.listdir(root_dir)

    print("一共有 %d 不同的用户" % user_nums())
    print("一共有 %d 不同的电影" % movie_nums())
    print("一共有 %d 不同的电影种类" % movie_gen())
    print("一共有 %d 电影没有外部链接" % nolink())
    print("2018年一共有 %d 人进行过电影评分" % rate_user_2018())
