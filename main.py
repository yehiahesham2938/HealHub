from flask import Flask, request, render_template
from NormalUser import NormalUser
from administrator import administrator
app = Flask(__name__ , static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usertype = request.form.get('usertype')
        if usertype == 'Administrator':
            username = request.form.get('username')
            password = request.form.get('password')
            print("Username:", username)
            print("Password:", password)
            if username == 'admin' and password == 'admin':
                return administrator()
            else:
                return 'Invalid username or pass'
        else:
            return NormalUser()
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()

