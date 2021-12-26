from flask import *
from database import WorkspaceData

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template("Home.html")


@app.route('/Home.html', methods=['GET'])
def home1():
    return render_template("Home.html")


@app.route('/About.html', methods=['GET'])
def about():
    return render_template("About.html")


@app.route('/Contact.html', methods=['GET'])
def contact():
    return render_template("Contact.html")


@app.route('/Login.html', methods=['POST','GET'])
def login():
    return render_template("Login.html")


@app.route('/Sign-Up.html', methods=['GET'])
def signup():
    return render_template("Sign-Up.html")


# @app.route('/Login.html',methods=['POST','GET'])
# def signup1():
#   return render_template("Login.html")

@app.route('/Match-Schedule.html', methods=['GET'])
def matchschedule():
    return render_template("Match-Schedule.html")

@app.route('/Before-Profile.html', methods=['POST', 'GET'])
def beforeprofile():
    return render_template("Before-Profile.html")


@app.route('/Profile.html', methods=['POST', 'GET'])
def profile():
    return render_template("Profile.html",info_data=0)

@app.route('/Registration.html', methods=['POST', 'GET'])
def registration():
    return render_template("Registration.html")


@app.route('/FootBall.html', methods=['POST'])
def football():
    return render_template("FootBall.html")


@app.route('/Cricket.html', methods=['POST'])
def cricket():
    return render_template("Cricket.html")


@app.route('/Basket-Ball.html', methods=['POST'])
def basketball():
    return render_template("Basket-Ball.html")


@app.route('/Badminton.html', methods=['POST'])
def badminton():
    return render_template("Badminton.html")


@app.route('/register_game', methods=['POST', 'GET'])
def register_game():
    if request.method == 'POST':
            user_name = request.form.get('username')
            game1 = request.form.get('game')
            db = WorkspaceData()
            db.add('games', [(user_name, game1)])
            data = db.get('games', user_name)
            for s in data:
                if user_name == s['username'] and game1 == 'football':
                    return render_template('/FootBall.html', retry=True, errorType='registration')
                if user_name == s['username'] and game1 == 'basketball':
                    return render_template('/Basket-Ball.html', retry=True, errorType='registration')
                if user_name == s['username'] and game1 == 'badminton':
                    return render_template('/Badminton.html', retry=True, errorType='registration')
                if user_name == s['username'] and game1 == 'cricket':
                    return render_template('/Cricket.html', retry=True, errorType='registration')
            return render_template('Registration.html', retry=True, errorType='registration')


@app.route('/validate_login', methods=['POST', 'GET'])
def validate_login():
    if request.method == 'POST':
        if 'login' in request.form:
            user_name = request.form.get('username')
            password = request.form.get('password')
            db = WorkspaceData()
            data = db.get('signup1', user_name)
            for s in data:
                if user_name == s['username'] and password == s['password']:
                    info_data = dict()
                    for s in data:
                        if user_name == s[0]:
                            info_data['username'] = user_name
                            info_data['age'] = s[1]
                            info_data['fname'] = s[2]
                            info_data['mname'] = s[3]
                            info_data['email'] = s[4]
                            info_data['proat'] = s[5]
                            info_data['aboutme'] = s[6]
                            info_data['acheivements'] = s[7]
                            return render_template('Profile.html', info_data=info_data)

            return render_template('Login.html', retry=True, errorType='login')
        elif 'signup' in request.form:
            username = request.form.get('username')
            age = request.form.get('age')
            fname = request.form.get('fathername')
            mname = request.form.get('mothername')
            email = request.form.get('email')
            proat = request.form.get('proat')
            aboutme = request.form.get('aboutme')
            acheivements = request.form.get('acheivements')
            password = request.form.get('password')
            password1 = request.form.get('password1')
            if (str(password) == str(password1)):
                db = WorkspaceData()
                db.add('signup1',
                       [(username, age, fname, mname, email, proat, aboutme, acheivements, password, password1)])
                return render_template('Login.html', retry=True, errorType='signup')
            #   return render_template('Login.html')
            else:
                return render_template('Sign-Up.html', retry=True, errorType='signup')

if __name__ == '__main__':
    app.run(debug=True)
