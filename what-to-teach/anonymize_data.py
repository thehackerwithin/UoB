""" Script to anonymize THW data
"""

import sys

import pandas as pd

fname = sys.argv[1]

full_df = pd.read_table(fname, encoding='utf_16_le')

# Drop the first 19 questions (potentially identifying).
df = full_df.iloc[:, 19:].copy()

# The first row has a description of the questions.
descriptions = df.iloc[0, :]
# The second has an import-id.
# Drop these preliminaries.
df.drop([0, 1], inplace=True)

# Replace column names with more readable versions
replacements = {"Q11": "key_tools",
                "Q13": "languages",
                "Q14": "practices",
                "Q15": "libraries",
                "Q16": "tools"}

names = df.columns
for name, description in zip(names, descriptions):
    if not name.startswith('Q17'):
        continue
    d_type = description.split(' - ')[1].lower().replace(' ', '_')
    replacements[name] = 'category_' + d_type


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
