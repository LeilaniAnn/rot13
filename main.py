
import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
							   autoescape=True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		# **params = extra paramaters
		t = jinja_env.get_template(template)
		# load and render template
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainHandler(Handler):
    def get(self):
    	# .get_all function that returns a list of all values that 
    	# belong to string that matches a key in our query parameter
    	self.render("index.html")

app = webapp2.WSGIApplication([('/', MainHandler),
], debug=True)
