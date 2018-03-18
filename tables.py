def pylist_2_htmltable(pylist):

	html = """<HTML>
	 <head>
    <title>Terribly Tiny Tales</title>
  </head>
  <body>
    <h1>Terribly Tiny Tales</h1>
    <form method="POST" action="">
      <div>Count (N)<input style="margin-left:15px;" type="text" name="count">
        <input style="margin-left:15px;" type="submit" name="submit" value="Submit">
      </div>
    </form>
	<body>
	    <table border="1">
	    <thead><tr><th>Keyword</th><th>Frequency</th></tr></thead>
	        {0}
	    </table>
	</body>
	</HTML>"""
	
	tr = "<tr>{0}</tr>"
	td = "<td>{0}</td>"
	subitems = [tr.format(''.join([td.format(a) for a in item])) for item in pylist]
	with open('./templates/result.html', 'w') as f:
		f.write(html.format("".join(subitems)))
	#return (html.format("".join(subitems)))