SRC=middle.pdc back.pdc
# This assumes double quotes in the docName!
TITLE=$(shell grep docName template.xml | sed -e 's/.*docName=\"//' -e 's/\">//')
PANDOC2RFC=../ext/pandoc2rfc/pandoc2rfc
TRANSFORM_XSL=../ext/pandoc2rfc/transform.xsl
SINGLE_XML=../ext/pandoc2rfc-old/xml-single
.PHONY: txt html xml clean realclean

title::
	@echo 
	@echo This directory makes 
	@echo $(TITLE)	
	@echo you can use .txt, .html, .xml suffix
	@echo

default:	draft.txt

txt:	$(TITLE).txt

html:	$(TITLE).html

xml:	$(TITLE).xml

draft.txt:	$(SRC) template.xml
	bash $(PANDOC2RFC) -t template.xml -x $(TRANSFORM_XSL) $(SRC)

draft.html: 	$(SRC) template.xml
	bash $(PANDOC2RFC) -t template.xml -x $(TRANSFORM_XSL) -M $(SRC)

draft.xml:	$(SRC) template.xml
	#bash $(PANDOC2RFC) -t template.xml -x $(TRANSFORM_XSL) -X $(SRC)
	$(SINGLE_XML) template.xml > draft.xml

$(TITLE).txt:	draft.txt
	cp $< $@

$(TITLE).html:	draft.html
	cp $< $@

$(TITLE).xml:	draft.xml
	cp $< $@

nits:   $(TITLE).txt
	if idnits --help 2>/dev/null >&2; then idnits --year $(date +%Y) --verbose $<; fi

clean:
	rm -f $(XML) $(TITLE).txt $(TITLE).html  $(TITLE).xml

realclean:	clean
	rm -f draft.txt draft.html draft.xml $(TITLE).txt $(TITLE).html $(TITLE).xml

