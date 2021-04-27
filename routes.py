from flask import render_template, redirect, request

from blog_app import db
from blog_app import blog_app
from blog_app.forms import MessageForm
from blog_app.models import User, Messages

@blog_app.route("/",methods = ['POST', 'GET'])
def blog():
   form = MessageForm()
   return render_template('home.html', title='Blogging', form=form)
def home():
   form = MessageForm()
   user_list = User.query.all()
   if form.validate_on_submit():
	input_name = request.form['author']
	for User in user_list:
	    if User.author == input_name:
		#found
	    else
		#create user, add to database
   user_list = User.query.all()
   for User in user_list:
	 posts = [{'author':User.author,'message':User.message}]
   
   return render_template('home.html', posts=posts, form=form)
