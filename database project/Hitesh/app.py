from flask import Flask,render_template,request
from flaskext.mysql import MySQL
app=Flask(__name__)
mysql=MySQL()


app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='Hitesh@MySQL'
app.config['MYSQL_DATABASE_DB']='customers'
mysql.init_app(app)


# data = cursor.fetchone()
# print(data)


#Default Route
@app.route('/')
def default_route():
    return render_template('index.html')

# Signup route
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username-s']
        email = request.form['email-s']
        password = request.form['password-s']

        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO users(username, password, email) VALUES (%s, %s, %s)", (username, password, email))
        conn.commit()
        cur.close()
        conn.close()

        return render_template('homepage.html')

# Login route
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username-l']
        password = request.form['password-l']
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            return render_template('homepage.html')
        else:
            error_message='!!Account does not exist!!'
            return render_template('index.html', login_error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
