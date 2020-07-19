import extools as ext
from datetime import datetime
from app import app, cache
from app.forms import SearchUser, SearchPost
from flask import render_template, request, url_for

@app.route('/')
@app.route('/home')
@app.route('/index')
@cache.cached(timeout=60)
def index():
	return render_template("index.html")

@app.route('/stats')
@app.route('/statistics')
@cache.cached(timeout=60)
def statistics():
	return render_template("statistics.html", ext=ext, datetime=datetime)

@app.route('/lboard')
@app.route('/leaderboard')
@cache.cached(timeout=60)
def lboard():
	return render_template("leaderboard.html", ext=ext)

@app.route('/users', methods=['GET', 'POST'])
def users():
	form = SearchUser()
	q = request.args.get('q')
	if q:
		return render_template(
			"redir.html",
			url=f'https://rc.irethekid.repl.co/users/{q}'
		)
	else: 
		return render_template("users.html", ext=ext, form=form)

@app.route('/users/<name>')
@cache.cached(timeout=60)
def usersPage(name):
	q = name
	q = q.lower().replace('@', '', 1)
	user = ext.genUser(q)
	if not user:
		return render_template(
			"error.html",
			context=f"User \"{q}\" was not found.",
			redirect=url_for('users')
		)
	else:
		return render_template("users.html",ext=ext,res=True,user=user)

@app.route('/posts')
def posts():
	form = SearchPost()
	q = request.args.get('q')
	o = request.args.get('o')

	if q:
		return render_template(
			"redir.html",
			url=f'https://rc.irethekid.repl.co/posts/results/{q}-{o}'
		)
	else:
		return render_template("posts.html", ext=ext, form=form, res=False)

@app.route('/posts/results/<query>-<order>')
def postsQ(query, order):
	q = str(query).replace('+', '')
	o = str(order)
	results = ext.genPostResults(q, o)

	return render_template("posts.html", ext=ext, r=results, q=q, res=True)

@app.route('/posts/page/<i>')
def postsP(i):
	p = ext.genPost(int(i))
	return render_template("posts.html", ext=ext, post=p, page=True, res=True)