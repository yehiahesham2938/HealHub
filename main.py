from flask import Flask, request, render_template
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
            if username == 'yaya' and password == 'admin':
                return render_template('administrator.html')
            else:
                return 'Invalid username or password'
        else:
            return render_template ("NormalUser.html")
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()

