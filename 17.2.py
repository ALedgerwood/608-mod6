# Project 2 - I saved just the commands from an ipython session - I've filled out the ch. 17 practice in the notebook file
import sqlite3
connection = sqlite3.connect('books.db')
import pandas as pd
pd.options.display.max_columns = 10
pd.read_sql('Select * FROM authors', connection, index_col=['id'])
pd.read_sql('SELECT * FROM titles', connection)
df = pd.read_sql('SELECT * FROM author_ISBN', connection)
df.head()
pd.read_sql("""SELECT title, edition, copyright FROM titles WHERE copyright > '2016'""", connection)
pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)
