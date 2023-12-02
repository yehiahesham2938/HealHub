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
                return '''
                <html>
                    <title>
                         Invalid 
                    </title>

                    <body>
                        <style>
                            body 
                            {
                                font-size: 29px;
                                text-align: center;
                            }
                            input
                            {
                                font-size: 19px;
                            }
                        </style>
                        <form>
                           <b> username or password is incorrect please try again!</b>
                            <br>
                            <br>
                            <input type="submit" value="Tryagain" style="width: 450px;">
                        </form>
                    </body>
                </html>
                '''
        else:
            return NormalUser()
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()

