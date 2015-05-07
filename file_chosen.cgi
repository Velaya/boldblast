#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi, cgitb
from Bio import SeqIO

cgitb.enable()

form = cgi.FieldStorage()

fileitem = form['userfile']

print("Content-type: text/html\n")

print("""
<html><body>
%s
""")
#% fileitem

for seq_record in SeqIO.parse(fileitem, "fasta"):
	print("""
	{0}<br>
	{1}<br>
	{2}<br>
	<br>
	""").format(seq_record.id, repr(seq_record.seq), len(seq_record))

print("""
</body></html>
""")
