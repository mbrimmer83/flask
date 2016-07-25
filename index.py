from flask import Flask, render_template, request, redirect, session
import pg

db = pg.DB(dbname='restaurant_db')

app = Flask('MyApp')

# @app.route('/')
# def restaurants():
#     query = db.query('''select * from reviews order by stars desc limit 5''')
#     return render_template('topReviews.html', title='Top Restaurant Reviews', projects=query.namedresult())

# @app.route('/newrestaurant')
# def form():
#     return render_template('form.html', title='Enter new restaurant')

# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#     project_name = request.form['project_name']
#     project_address = request.form['project_address']
#     project_category = request.form['project_category']
#     db.insert('restaurants', name=project_name, address=project_address, category=project_category)
#     return redirect('/')

@app.route('/')
def home():
    if 'name' in session:
        return redirect('/session-reviews')
        return render_template('topReviews.html', name=session['name'])
    else:
        return render_template('session-get-user.html')

@app.route('/submit_name', methods=['POST'])
def get_user():
    session['name'] = request.form['name']
    return redirect('/')

@app.route('/session-reviews')
def reviews():
    query = db.query("select users.id from users where name = '%s'" % session['name'])
    print query
    result = query.namedresult()[0]
    query2 = db.query('''select reviews.title, reviews.review, reviews.stars from reviews left outer join users on reviews.author_user_id = users.id where users.id = %d''' % result.id)
    print query2
    return render_template('session-reviews.html', title='Top Restaurant Reviews', projects=query2.namedresult())

app.secret_key = 'CSF686CCF85C6FRTCHQDBJDXHBHC1G478C86GCFTDCR'

if __name__ == '__main__':
    app.run(debug=True)
