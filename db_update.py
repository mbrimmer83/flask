import pg

db = pg.DB(dbname='github')

db.update('coder', {'id': 1, 'name': 'Matt', 'email': 'matt@gmail.com'})
