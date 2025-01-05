#/usr/bin/env python

import re

import bibtexparser
import openpyxl


def org_table_to_xlsx(org_table_file, xlsx_filename):
    """
    Converts an Org-mode table string to an Excel XLSX file.

    Args:
        org_table_file: The string containing the Org-mode table data.
        xlsx_filename: The desired filename for the output XLSX file.
    """

    with open(org_table_file, 'r') as f:
        org_table = f.read()

    # 1. Parse Org-mode table data
    table_data = []
    for line in org_table.splitlines():
        if line.startswith("|"):  # Check if it's a table row
            row = line.strip("|").split("|")
            row = [cell.strip() for cell in row]
            table_data.append(row)

    # 2. Create a new Excel workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # 3. Write data to Excel sheet
    for row_idx, row in enumerate(table_data):
        for col_idx, cell_value in enumerate(row):
            sheet.cell(row=row_idx + 1, column=col_idx + 1, value=cell_value)

    # 4. Save the workbook to XLSX file
    workbook.save(xlsx_filename)


def get_bibparser_val(worddict, field):

    if worddict.get(field):
        return worddict[field].value.strip()
    return ''


def bib2org(bibfile, orgfile):
    bib_database = bibtexparser.parse_file(bibfile)

    a = """| word   |  ipa |  desc   | pl      | v-ing  | v-ed | see |
|--------+----+------+----------------------+--------+------+----|
"""

    with open(orgfile, 'w') as org:
        org.write(a)

    # 遍历每个条目
    for entry in bib_database.entries:
        word_dict = entry.fields_dict  # The entry fields, as a dictionary by field key

        word = get_bibparser_val(word_dict, 'name')
        if not word:
            word = entry.key

        ipa = ''
        desc = get_bibparser_val(word_dict, 'description')
        # 匹配 desc中 '\doulos{xxx}' 大括号里的内容
        ipa_matches = re.match(r'\\doulos\{(.*?)\}', desc)
        if ipa_matches:
            ipa = ipa_matches.group(1)
            desc = desc[ipa_matches.end():]

        plural = get_bibparser_val(word_dict, 'plural')
        ving = get_bibparser_val(word_dict, r'ing')
        ved = get_bibparser_val(word_dict, r'ed')
        see = get_bibparser_val(word_dict, 'see')

        line = '|'.join((word, ipa, desc, plural, ving, ved, see))
        line = '|' + line + '|\n'

        with open(orgfile, 'a') as org:
            org.write(line)


if __name__ == '__main__':
    bib2org('example_table.bib', 'out_table.org')
    org_table_to_xlsx('out_table.org', 'out_table.xlsx')
