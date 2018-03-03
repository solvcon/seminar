#!/usr/bin/env python

import sys
import markdown2 as md2

html = md2.markdown_path(
        sys.argv[1],
        extras=["tables", "fenced-code-blocks"])

html = """<!DOCTYPE html><html>
<head>
<title>2017 SOLVCON Bootcamp</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
<div class="page">
%s
</div>
</body></html>""" % html

with open(sys.argv[2], "w") as fobj:
    fobj.write(html.encode('utf8'))
