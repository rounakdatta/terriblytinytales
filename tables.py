from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
 
    phrase = Col('Phrase')
    freq = Col('Frequency')