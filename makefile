# Inspired by https://goo.gl/SYWRbM
# Call it like: $ make notebook=<name_of_your_notebook_without_extension>

# detect OS
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
	OPEN_CMD = open
else
	ifeq ($(UNAME_S),Linux)
		OPEN_CMD = xgd-open
	else
		OPEN_CMD = start
	endif
endif

NOTEBOOK_FILE=$(notebook).ipynb
SLIDES_FILE=$(notebook).slides.html

# these custom keybindings allow right and left cursors to move slides even when vertical
# https://www.cambiaresearch.com/articles/15/javascript-char-codes-key-codes
# https://github.com/hakimel/reveal.js#api
REVEALJS_REF_SEARCH_STRING=Reveal.addEventListener('slidechanged', setScrollingSlide);
REVEALJS_SETTINGS=Reveal.configure({ keyboard: {37:'prev', 39:'next',} });

# these settings shows the equation numbers
MATHJAX_REF_SEARCH_STRING=MathJax.Hub.Config({
MATHJAX_SETTINGS=TeX: { equationNumbers: {autoNumber: \"AMS\"} },

.PHONY: all slides present clean

all: slides present

slides: ${NOTEBOOK_FILE}
	pipenv run jupyter nbconvert ${NOTEBOOK_FILE} --to slides
	sed -i "s/${REVEALJS_REF_SEARCH_STRING}/${REVEALJS_REF_SEARCH_STRING}${REVEALJS_SETTINGS}/" ${SLIDES_FILE}
	sed -i "s/${MATHJAX_REF_SEARCH_STRING}/${MATHJAX_REF_SEARCH_STRING}${MATHJAX_SETTINGS}/" ${SLIDES_FILE}

present: slides
	${OPEN_CMD} ${SLIDES_FILE}

jupyter:
	pipenv run jupyter notebook

pdf: ${NOTEBOOK_FILE}
	pipenv run jupyter nbconvert --to pdf  ${NOTEBOOK_FILE}

pdfall:
	find *.ipynb -exec pipenv run jupyter nbconvert --to pdf {} \;

install:
	pipenv install --three --skip-lock

update:
	pipenv run python update.py

clean:
	rm -fv *html
	rm -f *.pdf
