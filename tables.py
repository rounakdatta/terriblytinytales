from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
 
    phrase = Col('Phrase')
    freq = Col('Frequency')

def pylist_2_htmltable(pylist):

	table = '<table border="1"><thead><tr><th>Phrase</th><th>Frequency</th></tr></thead>'
	table += '<tbody>'
	for item in pylist:
		table += '<tr><td>' + str(item[0]) + '</td><td>' + str(item[1]) + '</td></tr>'
	table += '</tbody></table>'
	
	return table