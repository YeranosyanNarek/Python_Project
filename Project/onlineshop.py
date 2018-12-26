from flask import Flask, request, render_template, redirect, url_for, flash, session, escape
from Projects import Registr_LoginForm as RLF
from Projects import product as PD
from Projects import mongodb as MD
from Projects import user as USR

app = Flask(__name__)
app.secret_key = '4444'
db = MD.Mongo()

@app.route('/')
def Home():
    results = PD.product(db.prod_inf_db['model'], db.prod_inf_db['price'], db.prod_inf_db['img'], db.prod_inf_db['desc'], db.prod_inf_db['url']).prod_inf()
    return render_template('home.html', results=results, my_title="Home")

@app.route('/about')
def about():
    return render_template('about.html', my_title="About")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RLF.RegistrationForm(request.form)

    if request.method == 'POST':
        if form.validate():
            try:
                USR.Register(request.form['username'], request.form['email'], request.form['password']).register()
                flash(f"welcome dear {form.username.data}!!!", 'success')

                return redirect(url_for('Home'))
            except Exception:
                flash(f"E-Mail already exist", 'danger')
                return redirect(url_for('register'))

    return render_template('register.html', my_title="Register", form=form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = RLF.LoginForm(request.form)
    if request.method == 'POST':
        if form.validate():
            email = request.form['email']
            password = request.form['password']

            while USR.Login(email, password).email_not():
                flash(f"User doesn't exist, go to registration", 'danger')
                return redirect(url_for('login'))

            while USR.Login(email, password).email_verif():
                if USR.Login(email, password).pas_verif():
                    name = MD.Mongo.user_inf.find_one({'email': email})['username']
                    session['email'] = request.form['email']
                    flash(f"Welcome dear " + name + "!!!", 'success')
                    return redirect(url_for('Home'))
                else:
                    flash(f"Password are wrong", 'danger')
                    return redirect(url_for('login'))

    return render_template('login.html', my_title="Login", form=form)

@app.route('/<name>', methods=['GET', 'POST'])
def prod(name):
    res = MD.Mongo.prod_inf.find_one({'url': name})
    results = PD.product(res['model'], res['price'], res['img'], res['desc'], res['url']).prod_inf()
    if 'email' in session:
        sess = 'buy_success'
    else:
        sess = 'buy_quest'
    return render_template(name,  my_title= res['model'], results = results, sess = sess)

@app.route('/buy_quest', methods=['GET', 'POST'])
def buy_quest():
    return render_template('buy_quest.html',  my_title= 'buy quest')

@app.route('/buy_success', methods=['GET', 'POST'])
def buy_success():
    return render_template('buy_success.html',  my_title= 'buy success')

@app.route('/logout')
def logout():
   session.pop('email', None)
   return redirect(url_for('Home'))

if __name__ == '__main__':
    app.run(debug=True)


