#/usr/bin/env python

import bibtexparser

bib_database = bibtexparser.parse_file('oldman.bib',
                                       ignore_nonstandard_types=True)

# 遍历每个条目
# for entry in bib_database.entries:
# word = ''

# if entry.entry_type == 'index':
#     word = entry.key()

# word_dict = entry.fields_dict  # The entry fields, as a dictionary by field key

# if word_dict['name']:
#     word = word_dict['name']

# desc = word_dict['description']

# print(f'{word} {desc}')

# plural = word_dict['plural']
# ving = word_dict['ving']
# ved = word_dict['ved']
# see = word_dict['see']

# print(f'{word} {desc} {plural} {ving} {ved} {see}')

# import pandas as pd

# desc = [item[0] for item in description_matches]  # 第一列数据
# ipa = [item[2] for item in description_matches]  # 第二列数据

# df = pd.DataFrame({'word': name_matches, 'ipa': ipa, 'desc': desc})

# df['desc'] = df['desc'].str.replace(r'\\do.*?\}', '', regex=True)
# df['desc'] = df['desc'].str.replace(r'\\', '')
# df['desc'] = df['desc'].str.strip(' ,')
# df = df.sort_values(by='word')

# df.to_excel('oldman.xlsx', index=False)
