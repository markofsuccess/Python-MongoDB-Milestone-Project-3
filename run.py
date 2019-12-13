import os
from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MONGO_DBNAME'] = os.getenv('MONGO_DBNAME')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")
    
@app.route('/services')
def services():
    return render_template("services.html")


@app.route('/itemone_review',methods=['GET','POST'])
def itemone_review():
    review=mongo.db.specifications.find()
    return render_template("itemone_review.html", review=review)
    
@app.route('/insert_text', methods=['GET','POST'])
def insert_text():
    if request.method == 'POST':
        specifications = mongo.db.specifications
        specifications.insert_one(request.form.to_dict())
    return redirect(url_for('itemone_review',))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)