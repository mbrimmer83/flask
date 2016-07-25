import pg
db = pg.DB(dbname='github')

query = db.query('select * from coder limit 10')

for coder in query.namedresult():
    print coder.name
