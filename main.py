
import webapp2
import jinja2
import os
from google appengine.ext import db 
import datetime


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader_=_jinja2.FileSystemLoader(template_dir)

def render_str(template, **params):
	t = jinja_env.get_template(template)
     return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

        def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class Blog(BaseHandler):
    def get(self):

        posts = db.GqlQuery("SELECT * FROM Post LIMIT 10")

        posts_dic = {"posts": posts}
        self.render('index.html', **posts_dic)



class New(BaseHandler):
    def get(self):
        self.render('new.html)
        

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        blog_post = Post(title=subject, content=content)
        blog_post.put()
        self.redirect('/')

class About(BaseHandler):
	def get(self):
		self.render('about.html')

class Post(db.Model):
    title = db.StringProperty(required=True)
    content = db.StringProperty(required=True)
    adddate = db.dateTimeProperty(auto_now_add=True)

app = webapp2.WSGIApplication([
    ('/', Home),
    ('/about', About)
], debug=True)
