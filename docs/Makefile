
.PHONY: diagram
diagram:
	dot -Tpng process_flow.dot -o process_flow.png
	dot -Tsvg process_flow.dot -o process_flow.svg

.PHONY: clean_diagram
clean_diagram:
	-rm process_flow.{png,svg}
