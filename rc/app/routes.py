import secrets
import extools as ext
from datetime import datetime

from app import app, cache, db
from app.forms import SearchUser, SearchPost
from app.models import User, check_user, new_user
db.create_all()

from flask import render_template, request, url_for, redirect
from flask_login import login_user, current_user, logout_user

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
	return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
	global auth_token
	auth_token =secrets.token_hex(16)

	return render_template('login.html',
		user_id=request.headers['X-Replit-User-Id'],
		user_name=request.headers['X-Replit-User-Name'],
		auth_token=auth_token,
		auth=True
	)


@app.route('/auth/<username>/<int:id>/<aT>')
def auth_user(username, id, aT):
	if aT == auth_token:
		if check_user(username):
			user = User.query.filter_by(username=username).first()
			login_user(user, remember=False)
			return redirect(url_for('index'))
		else:
			rtUser = ext.genUser(username)
			new_user(
				uid = id,
				uname = username,
				upfp = rtUser.avatar,
				ujd = datetime.now()
			)
			return render_template('login.html', newAcc=True)
	else:
		return "Repl.it Account has not been authenticated."


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/settings')
def settings():
	return render_template("error.html",context='coming soon')

@app.route('/stats')
@app.route('/statistics')
@cache.cached(timeout=60)
def statistics():
    return render_template("statistics.html", ext=ext, datetime=datetime)


@app.route('/goto', defaults={'upath': ''})
@app.route('/goto/', defaults={'upath': ''})
@app.route('/goto/<path:upath>')
@cache.cached(timeout=60)
def goto_lboard(upath):
    if len(upath.split('.')) > 1:
        return redirect('/' + upath)
    return render_template("redir.html", url="/" + upath)


@app.route('/lboard')
@app.route('/leaderboard')
@cache.cached(timeout=60)
def lboard_loaded():
    return render_template("leaderboard.html", ext=ext)


@app.route('/users', methods=['GET', 'POST'])
def users():
    form = SearchUser()
    q = request.args.get('q')
    if q:
        return render_template(
            "redir.html", url=f'https://rc.irethekid.repl.co/users/{q}')
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
            redirect=url_for('users'))
    else:
        return render_template("users.html", ext=ext, res=True, user=user)


@app.route('/posts')
def posts():
    form = SearchPost()
    q = request.args.get('q')
    o = request.args.get('o')

    if q:
        return render_template(
            "redir.html",
            url=f'https://rc.irethekid.repl.co/posts/results/{q}-{o}')
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


@app.route('/info')
@app.route('/information')
def info():
    return render_template("info.html")
