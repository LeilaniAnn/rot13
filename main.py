
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
		self.render("text_area.html")
	def post(self):
		rot13=""
		user_input = self.request.get('text')
		if user_input:
			rot13=user_input.encode("rot13")
		self.render("text_area.html", user_input=rot13)




app = webapp2.WSGIApplication([('/', MainHandler),
], debug=True)
