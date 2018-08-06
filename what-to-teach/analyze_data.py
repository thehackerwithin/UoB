""" Analyze cleaned survey data
"""
from __future__ import division

import pandas as pd

df = pd.read_csv('thw_survey.csv')


def ana_question(df, q_root):
    yes_qs = [q for q in df.columns
              if q.startswith(q_root + '-ranks-yes')]
    maybe_qs = [q for q in df.columns
              if q.startswith(q_root + '-ranks-maybe')]
    yes_rescaled = (ana_part(df[yes_qs]) + 1).fillna(0).as_matrix()
    maybe_rescaled = ana_part(df[maybe_qs]).fillna(0).as_matrix()
    values = (yes_rescaled + maybe_rescaled).sum(axis=0)
    names = [q.split('-')[-1] for q in yes_qs]
    return dict(zip(names, values))


def ana_part(cols):
    n = len(cols.columns)
    return (n - (cols - 1)) / n


categories = [q for q in df.columns if q.startswith('category')]
cat_names = [q.split('-')[-1] for q in categories]
cat_rank_mean = dict(zip(cat_names, df[categories].mean()))

cat_scores = {c_name: ana_question(df, c_name) for c_name in cat_names}
