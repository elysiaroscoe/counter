from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'lets make a secret counter'

@app.route('/')
def index():
    if 'visit' in session:
        print('yes')
        session['visit'] += 1
    else:
        session['visit'] = 1
        print('no')
    return render_template("index.html")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)