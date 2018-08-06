""" Script to anonymize THW data
"""

import sys

import pandas as pd

fname = sys.argv[1]

full_df = pd.read_table(fname, encoding='utf_16_le')

# Drop the first 19 questions (potentially identifying).
df = full_df.iloc[:, 19:].copy()

# Drop the last column (doesn't have any useful data)
df.drop(columns='Q3 - Topics', inplace=True)

# The first row has a description of the questions.
descriptions = df.iloc[0, :]
# The second has an import-id.
# Drop these preliminaries.
df.drop([0, 1], inplace=True)

# Replace column names with more readable versions
replacements = {}


def desc_to_word(in_str):
    parts = in_str.lower().strip().split()
    if parts[0] == 'the':
        parts.pop(0)
    return parts[0]


def to_var(in_str):
    return '_'.join(in_str.lower().strip().split())


names = df.columns
for name, description in zip(names, descriptions):
    d_parts = description.split(' - ')
    if name.startswith('Q17'):
        d_type = to_var(d_parts[1])
        replacements[name] = 'category-' + d_type
        continue
    # A group / rank question
    area = to_var(d_parts[0].split('.')[0])
    grp_rank = to_var(d_parts[1])
    y_m = to_var(d_parts[2].split(' ')[0])
    name_parts = [area, grp_rank, y_m]
    if grp_rank == 'ranks':
        name_parts.append(desc_to_word(d_parts[3]))
    replacements[name] = '-'.join(name_parts)


new_names = []
for name in names:
    for key, value in replacements.items():
        if name.startswith(key):
            name = value + name[len(key):]
            break
    new_names.append(name)
df.columns = new_names

# Save cleaned data to csv
df.to_csv('thw_survey.csv', index=False)
