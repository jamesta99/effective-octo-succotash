from blog_app import db

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   author = db.Column(db.String(64), index=True, unique=True)
   message = db.relationship('Post', backref='author')
   def __repr__(self):
      return f'<User {self.author}>'

class Messages(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   message = db.Column(db.String(256))
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

   def __repr__(self):
	return f'<Message: {self.message}>'
