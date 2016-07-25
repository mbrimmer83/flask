import pg

db = pg.DB(dbname='github')

db.insert('coder', name='Marty McFly', email='mmc@aol.com')
