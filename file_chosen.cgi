#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi, cgitb
import csv 
import urllib2
import xml.etree.ElementTree as ET
from Bio import SeqIO

form = cgi.FieldStorage()

fileitem = form['userfile']
db = form.getvalue('db')
quan = form.getvalue('quantity')

print("Content-type: text/html\n")

print("""
<html><body>
""")

x = 1

for seq_record in SeqIO.parse(fileitem.file, "fasta"):
	print("""
	{0}<br>
	{1}<br>
	{2}<br>
	<br>
	""").format(seq_record.id, repr(seq_record.seq), len(seq_record))
	boldurl = "http://boldsystems.org/index.php/Ids_xml?db=" + str(db) + "&sequence=" + seq_record.seq
	#with os.fdopen(os.open('output'+str(x)+'.csv'), 'wb') as csvfile
	#fieldnames = ['ID', 'Database', 'Taxonomic identification', 'Similarity', 'Specimen']
	#writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	#writer.writeheader()
	#root = ET.fromstring(boldurl)
	s = open('output'+str(x)+'.csv', 'wb')
	writer = csv.writer(s)   
	r = urllib2.Request(str(boldurl))
	opener = urllib2.build_opener()
	tree = ET.parse(opener.open(r))
	root = tree.getroot()
	matchdetails = []
	m = 1
	for match in root.findall('match'):
		if m <= quan:
			idvalue = match.find('ID').text
			dbvalue = match.find('database').text
			tivalue = match.find('taxonomicidentification').text
			simvalue = match.find('similarity').text
			specvalue = match.find('url').text
			print("""
			{0}<br>
			{1}<br>
			<br>
			""").format(idvalue, dbvalue)
			sublist = [idvalue, dbvalue, tivalue, simvalue, specvalue]
			matchdetails.append(sublist)
			#writer.writerow({'ID': idvalue, 'database': dbvalue, 'Taxonomic identification': tivalue, 'Similarity': simvalue, 'Specimen': specvalue})
		m += 1
	writer.writerows(matchdetails)
	s.close()
	x += 1

print("""
</body></html>
""")
