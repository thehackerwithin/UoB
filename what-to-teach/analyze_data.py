""" Analyze cleaned survey data

See anonymize_data.py for structure of data frame.

Run tests with::

    pytest test_analyze_data.py
"""
from __future__ import division


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


def process_data(df):
    categories = [q for q in df.columns if q.startswith('category')]
    cat_names = [q.split('-')[-1] for q in categories]
    cat_rank_mean = dict(zip(cat_names, df[categories].mean()))
    cat_scores = {c_name: ana_question(df, c_name) for c_name in cat_names}
    return cat_rank_mean, cat_scores


def main():
    from pprint import pprint
    import pandas as pd
    df = pd.read_csv('thw_survey.csv')
    cat_rank_mean, cat_scores = process_data(df)
    print('Mean rank of categories')
    pprint(cat_rank_mean)
    print('Composite ranking score within categories')
    pprint(cat_scores)


if __name__ == '__main__':
    main()
