# 将 "blalba" 转换为TeX的 ``blalba''

with open('1984.tex', 'r') as f:
    quotes = f.read()

a = 1

result = ''
for quote in quotes:
    if quote == r'"':
        if a == 1:
            result += '``'
            a = 2
        else:
            result += '\'\''
            a = 1
    else:
        result += quote

with open('1984.tex', 'w') as f:
    f.write(result)
