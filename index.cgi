#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi

print("Content-type: text/html\n")


print("""
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<title>Fasta-Dateien BLASTEN</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<link type="text/css" rel="stylesheet" href="/transfer/css/transfer.css" media="all">
</head>
<body>
	<h1>Fasta-Dateien BLASTEN</h1>
	<div id="content" class="center">
	<form enctype="multipart/form-data" action="file_chosen.cgi" method="post">
		<p>File: <input type="file" name="userfile" /></p>
		<p><input type="submit" value="Upload" /></p>
	</form>
	</div>
</body></html>""")
