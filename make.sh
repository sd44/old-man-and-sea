cp theoldman_en.tex tmp.tex &&
latexmk -C theoldman.tex &&
xelatex theoldman.tex &&
bib2gls --group theoldman &&
xelatex theoldman.tex &&
bib2gls --group theoldman &&
xelatex theoldman.tex &&
xelatex theoldman.tex&&
cp theoldman.pdf 'The Old Man and the Sea 词汇注解版.pdf'&&
#
# 生成双解版pdf
#
python combine2file.py &&
cp theoldman_cn_en.tex tmp.tex&&
latexmk -C theoldman.tex &&
xelatex theoldman.tex &&
bib2gls --group theoldman &&
xelatex theoldman.tex &&
bib2gls --group theoldman &&
xelatex theoldman.tex &&
xelatex theoldman.tex
cp theoldman.pdf 'The Old Man and the Sea 双语 词汇注解版.pdf'
