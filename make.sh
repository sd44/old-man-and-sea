#!/bin/sh
#
set -e # 遇到任何命令失败时立即退出脚本
#
# 生成词汇注解版老人与海
#
cp theoldman_en.tex tmp.tex
latexmk -C theoldman.tex
xelatex theoldman.tex
bib2gls --group theoldman
latexmk theoldman.tex
cp theoldman.pdf 'The Old Man and the Sea 词汇注解版.pdf'
#
# 生成双解词汇注解版老人与海
#
python tools/combine2file.py
cp theoldman_cn_en.tex tmp.tex
xelatex theoldman.tex
bib2gls --group theoldman
latexmk theoldman.tex
cp theoldman.pdf 'The Old Man and the Sea 双语 词汇注解版.pdf'
rm theoldman.pdf
