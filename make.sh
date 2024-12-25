latexmk -C theoldman.tex &&
xelatex theoldman.tex &&
bib2gls --group theoldman &&
xelatex theoldman.tex &&
bib2gls --group theoldman &&
xelatex theoldman.tex &&
xelatex theoldman.tex
cp theoldman.pdf 'The Old Man and the Sea 词汇注解版(加粗).pdf'
