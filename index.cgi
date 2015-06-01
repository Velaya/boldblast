#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi

print("Content-type: text/html\n")


print("""
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<title>BLAST Fasta-files</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
	<script type="text/javascript">
	function checkForm(form) {
		$("#submit_field").hide();
		$("#messages").html('<p>Fetching results - this may take a few minutes...');
		return true;
	}
	</script>
</head>
<body>
	<h1>BLAST Fasta-files with the BOLD ID Engine Web Service</h1>
	<div id="content" class="center">
		<form enctype="multipart/form-data" action="file_chosen.cgi" method="POST" onsubmit="return checkForm(this);">
			<p>File: <input type="file" name="userfile" required/></p>
			<p>Database:
			<fieldset>
				<input type="radio" id="cox" name="db" value="COX1">
				<label for="cox"> COX1</label>
				<br>
				<input type="radio" id="coxspec" name="db" value="COX1_SPECIES">
				<label for="coxspec"> COX1_SPECIES</label>
				<br>
				<input type="radio" id="coxspecpub" name="db" value="COX1_SPECIES_PUBLIC" checked="checked">
				<label for="coxspecpub"> COX1_SPECIES_PUBLIC</label>
				<br>
				<input type="radio" id="cox640" name="db" value="COX1_L640bp">
				<label for="cox640"> COX1_L640bp</label>
			</fieldset><p>
			<p>Number of results per Sequence:
				<input type="number" name="quantity" min="1" max="10" required>
			<p>Results:
			<fieldset>
				<input type="radio" id="single" name="csv" value="single" checked="checked">
				<label for="single"> One .csv file for all sequences</label>
				<br>
				<input type="radio" id="multi" name="csv" value="multi">
				<label for="multi"> One .csv file for each sequence</label>
			</fieldset><p>
			<div id="submit_field"><input type="submit" value="Upload" /></div>
		</form>
		<div id="messages"/></div>
	</div>
</body></html>""")
