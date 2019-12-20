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
    
@app.route('/itemtwo_review',methods=['GET','POST'])
def itemtwo_review():
    samsung=mongo.db.samsung.find()
    return render_template("itemtwo_review.html", samsung=samsung)

@app.route('/insert_samsung', methods=['GET','POST'])
def insert_samsung():
    if request.method == 'POST':
        samsung = mongo.db.samsung
        samsung.insert_one(request.form.to_dict())
    return redirect(url_for('itemtwo_review',))

@app.route('/itemthree_review',methods=['GET','POST'])
def itemthree_review():
    huawei=mongo.db.huawei.find()
    return render_template("itemthree_review.html", huawei=huawei)

@app.route('/insert_huawei', methods=['GET','POST'])
def insert_huawei():
    if request.method == 'POST':
        huawei = mongo.db.huawei
        huawei.insert_one(request.form.to_dict())
    return redirect(url_for('itemthree_review',))

@app.route('/itemfour_review',methods=['GET','POST'])
def itemfour_review():
    google=mongo.db.google.find()
    return render_template("itemfour_review.html", google=google)

@app.route('/insert_google', methods=['GET','POST'])
def insert_google():
    if request.method == 'POST':
        google = mongo.db.google
        google.insert_one(request.form.to_dict())
    return redirect(url_for('itemfour_review',))
    
@app.route('/itemfive_review',methods=['GET','POST'])
def itemfive_review():
    iphone=mongo.db.iphone.find()
    return render_template("itemfive_review.html", iphone=iphone)

@app.route('/insert_iphone', methods=['GET','POST'])
def insert_iphone():
    if request.method == 'POST':
        iphone = mongo.db.iphone
        iphone.insert_one(request.form.to_dict())
    return redirect(url_for('itemfive_review',))

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)