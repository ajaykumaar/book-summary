from datetime import datetime
from flask import *
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_db.sqlite3'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(50))
    author = db.Column(db.String(50))
    summary_p = db.Column(db.String(500))
    summary_l = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)


@app.route('/',methods=['GET','POST'])
def show_book():
    user = User.query.all()
    return render_template('books_home.html',user=user)

@app.route('/add_book',methods=['GET','POST'])
def add_book():
    
    return render_template('add_book.html')

@app.route('/save_book',methods=['GET','POST'])
def save_book():
    book_name=request.form['name']
    author=request.form['author']
    sp=request.form['summary_p']
    sl=request.form['summary_l']
    user = User(book_name=book_name, author=author, summary_p=sp, summary_l=sl)
    db.session.add(user)
    db.session.commit()
    user = User.query.all()

    return render_template('books_home.html',user=user)



@app.route('/del_book',methods=['GET','POST'])
def del_books():
    return render_template('del_book.html')

@app.route('/delete_book',methods=['GET','POST'])
def delete_books():
    book_id=request.form['id']
    bookToDelete = db.session.query(User).filter_by(id=book_id).one()
    db.session.delete(bookToDelete)
    db.session.commit()
    user = User.query.all()
    return render_template('books_home.html',user=user)

if __name__ == '__main__':
   app.run(debug = True)
