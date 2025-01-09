def read_file_by_blankline(filename):
    """读取UTF-8 编码的text文件，每段落之间用空行间隔，并返回各段落组成的数组

    """
    with open(filename, 'r') as f:
        a = f.read().split('\n\n')
        return a


def combin_file(enfile, cnfile):
    """合并两个文件，每段落对应

    """

    paracol_beg = '\\begin{paracol}{2}'
    paracol_end = '\n\\end{paracol}'

    swith_en_col = '\n\\switchcolumn*\n'
    swith_cn_col = '\n\\switchcolumn\n'

    a = read_file_by_blankline(enfile)
    b = read_file_by_blankline(cnfile)

    comb_file = 'combine.tex'

    if len(a) != len(b):
        print(f'Warning:\n {enfile}: {len(a)}段落, but {cnfile}: {len(b)}段落\n')

    with open(comb_file, 'w') as comb:
        comb.writelines(paracol_beg)

        for i in zip(a, b):
            comb.writelines('\n'.join(
                ('', i[0], swith_cn_col, i[1], swith_en_col)))

        comb.writelines(paracol_end)


if __name__ == '__main__':
    combin_file('1984.tex', '1984-cn.tex')
