from flask import Flask, request, render_template
from NormalUser import NormalUser
from administrator import administrator
app = Flask(__name__ , static_folder='static')
doctors_data = []
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


@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    doctor_data = {
        'Name': request.form.get('doctor_name'),
        'Age': request.form.get('doctor_age'),
        'ID': request.form.get('doctor_id'),
        'Office Number': request.form.get('doctor_office_number'),
        'Salary': request.form.get('doctor_salary'),
        'Gender': request.form.get('doctor_gender')
    }

    doctors_data.append(doctor_data)

    return render_template('doctors_info.html', data=doctors_data)

@app.route('/display_doctor_info', methods=['GET'])
def display_doctor_info():
    return render_template('doctors_info.html', data=doctors_data)


if __name__ == '__main__':
    app.run()