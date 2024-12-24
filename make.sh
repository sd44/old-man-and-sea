latexmk -C theoldman.tex &&
xelatex theoldman.tex &&
bib2gls --group theoldman &&
xelatex theoldman.tex &&
bib2gls --group theoldman &&
xelatex theoldman.tex &&
xelatex theoldman.tex
