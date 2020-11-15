from flask import  Flask  , render_template , request 

from flask_mysqldb import MySQL 



app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'fla_mysql'

mysql = MySQL(app)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/login' , methods = ['POST' , 'GET'])
def login():
    if request.method =='GET':
        return "Login via the login form"

    if request.method == "POST":
        name = request.form['name']
        age = request.form ['age']
        print(age)
        print (name)
        cursor = mysql.connection.cursor()
        cursor.execute ('''INSERT  INTO info_table VALUES(%s , %s)''', (name , age))
        mysql.connection.commit()
        cursor.close () 
        return f"Done!!"


if __name__ == '__main__':
    app.run(host= 'localhost' , port = 5000, debug=True)