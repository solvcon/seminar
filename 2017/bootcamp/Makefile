MD_BIN = python markdown2.py

default: Makefile index.md
	$(MD_BIN) \
	-x tables \
	-x fenced-code-blocks \
	index.md > index.html
