import pg

db = pg.DB(dbname='restaurant_db')

# query1 = db.query('select * from restaurants')

# named_result = query1.namedresult()
# for restaurants in named_result:
#     print "Name: %s, address: %s" % (restaurants.name, restaurants.address)
#
# query2 = db.query('select * from reviews')
# named_result = query2.namedresult()
# for reviews in named_result:
#     print "Title: %s, review: %s" % (reviews.title, reviews.review)
#
# query3 = db.query('select * from users')
# named_result = query3.namedresult()
# for users in named_result:
#     print "Name: %s, email: %s, karma: %s" % (users.name, users.email, users.karma)

# db.insert('users', name='Regan', email='regan@email.com', karma='7')

# user_name = raw_input('Enter name')
# user_email = raw_input('Enter email')
# user_karma = raw_input('Enter karme between 1 and 7')
#
# db.insert('users', name=user_name, email=user_email, karma=user_karma)

user_id = raw_input('Enter user id')
user_name = raw_input('Enter name')
user_email = raw_input('Enter email')
user_karma = raw_input('Enter karme between 1 and 7')

db.update('users', {'id': user_id, 'name': user_name, 'email': user_email, 'karma': user_karma})
