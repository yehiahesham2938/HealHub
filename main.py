from flask import Flask, request, render_template
from NormalUser import NormalUser
from administrator import administrator
app = Flask(__name__ , static_folder='static')
doctors_data = []
patients_data= []
nurses_data=[]
Pharmacists_data=[]
Anesthesiologists_data=[]

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
        'Gender': request.form.get('doctor_Gender')
    }

    doctors_data.append(doctor_data)

    return render_template('doctors_info.html', data=doctors_data)

@app.route('/display_doctor_info', methods=['GET'])
def display_doctor_info():
    return render_template('doctors_info.html', data=doctors_data)



@app.route('/Add_Patient', methods=['POST'])
def Add_Patient():
    patient_data = {
        'Name': request.form.get('patient_name'),
        'Age': request.form.get('patient_age'),
        'ID': request.form.get('patient_id'),
        'Height': request.form.get('patient_height'),
        'Weight': request.form.get('patient_weight'),
        'Blood Type': request.form.get('patient_blood_type'),
        'patient_condition': request.form.get('patient_condition'),
        'Gender': request.form.get('Patient_gender'),
        'prescription': request.form.get('patient_prescription')
    }

    patients_data.append(patient_data)

    return render_template('patient_info.html', data=patients_data)

@app.route('/display_patients_info' , methods=['GET'])
def display_patients_info():
    data = [] 
    return render_template('patient_info.html', data=patients_data)


@app.route('/add_nurse', methods=['POST'])
def add_nurse():
    nurse_data = {
        'Name': request.form.get('Nurse_name'),
        'Age': request.form.get('Nurse_age'),
        'ID': request.form.get('Nurse_id'),
        'Salary': request.form.get('Nurse_salary'),
        'Gender': request.form.get('Nurse_Gender')
    }

    nurses_data.append(nurse_data)

    return render_template('Nurse_info.html', data=nurses_data)

@app.route('/display_nurse_info', methods=['GET'])
def display_nurse_info():
    data=[]
    return render_template('Nurse_info.html', data=nurses_data)


@app.route('/add_Pharmacist', methods=['POST'])
def add_Pharmacist():
    Pharmacist_data = {
        'Name': request.form.get('Pharmacist_name'),
        'Age': request.form.get('Pharmacist_age'),
        'ID': request.form.get('Pharmacist_ID'),
        'Salary': request.form.get('Pharmacist_Salary'),
        'Gender': request.form.get('Pharmacist_gender')
    }

    Pharmacists_data.append(Pharmacist_data)

    return render_template('Pharmacist_info.html', data=Pharmacists_data)

@app.route('/display_Pharmacist_info', methods=['GET'])
def display_Pharmacist_info():
    data=[]
    return render_template('Pharmacist_info.html', data=Pharmacists_data)



@app.route('/add_Anesthesiologist', methods=['POST'])
def add_Anesthesiologist():
    Anesthesiologist_data = {
        'Name': request.form.get('Anesthesiologist_name'),
        'Age': request.form.get('Anesthesiologist_age'),
        'ID': request.form.get('Anesthesiologist_ID'),
        'Salary': request.form.get('Anesthesiologist_Salary'),
        'Gender': request.form.get('Anesthesiologist_Gender')
    }

    Anesthesiologists_data.append(Anesthesiologist_data)

    return render_template('Anesthesiologist_info.html', data=Anesthesiologists_data)

@app.route('/display_Anesthesiologist_info', methods=['GET'])
def display_Anesthesiologist_info():
    data=[]
    return render_template('Anesthesiologist_info.html', data=Anesthesiologists_data)





if __name__ == '__main__':
    app.run()