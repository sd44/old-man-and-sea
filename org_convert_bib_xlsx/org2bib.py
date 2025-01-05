#/usr/bin/envpython

import pathlib


# 解析org表格为列表
def parse_org_table(org_table):
    rows = org_table.strip().split("\n")
    table = [row.strip("|").split("|") for row in rows if row.strip()]
    return [[cell.strip() for cell in row] for row in table]


# 修改表格
def update_cell(table, row, col, value):
    table[row][col] = value


# 转回 Org 格式
def generate_org_table(table):
    formatted_rows = ["| " + " | ".join(row) + " |" for row in table]
    return "\n".join(formatted_rows)


def org2bib(table_file, bib_file):
    rows = []
    with open(table_file, 'r') as f:
        content = f.read()
        table = parse_org_table(content)

    for row in table[2:]:
        word = row[0].replace(' ', '_')
        if row[1]:
            ipa = '\\doulos{' + f"{row[1]}" + '} '
        else:
            ipa = ''

        bib_filed = f'''
@index{{{word}}},
        name = {{{row[0]}}},
        description = {{{ipa}{row[2]}}},
        plural = {{{row[3]}}},
        ing = {{{row[4]}}},
        ed = {{{row[5]}}}
}}
        '''
        rows.append(bib_filed)
    with open(bib_file, 'w') as f:
        f.write('\n'.join(rows))


if __name__ == '__main__':
    table_file = pathlib.Path('example_word.org')
    bib_file = pathlib.Path('table.bib')
    org2bib(table_file, bib_file)
    print(f"Converted {table_file} to {bib_file}")
