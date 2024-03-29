from flask import Flask, request, render_template
from NormalUser import NormalUser
from administrator import administrator
app = Flask(__name__ , static_folder='static')
doctors_data = []
patients_data= []
nurses_data=[]
Pharmacists_data=[]
Anesthesiologists_data=[]
Room_data=[]
Attendance=[]
medicines_data=[]
Request_data_list = []
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


@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/QuitNormalUser')
def QuitNormalUser():
    
    return render_template('NormalUser.html')


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

    return render_template('administrator.html', data=doctors_data)

@app.route('/display_doctor_info', methods=['GET'])
def display_doctor_info():
    return render_template('doctors_info.html', data=doctors_data)

@app.route('/display_doctor_info_Users', methods=['GET'])
def display_doctor_info_Users():
    return render_template('Doctors_info_for_users.html', data=doctors_data)


@app.route('/display_Nurse_info_Users', methods=['GET'])
def display_Nurse_info_Users():
    return render_template('Nurse_info_for_users.html', data=nurses_data)



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

    return render_template('administrator.html', data=patients_data)

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

    return render_template('administrator.html', data=nurses_data)

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

    return render_template('administrator.html', data=Pharmacists_data)

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

    return render_template('administrator.html', data=Anesthesiologists_data)

@app.route('/display_Anesthesiologist_info', methods=['GET'])
def display_Anesthesiologist_info():
    data=[]
    return render_template('Anesthesiologist_info.html', data=Anesthesiologists_data)





@app.route('/add_Room', methods=['POST'])
def add_Room():
    Room_data = {
        'Name': request.form.get(' patient_name_room'),
        'Age': request.form.get(' patient_age_room'),
        'ID': request.form.get(' patient_ID_Room'),
        'days_needed': request.form.get(' days_needed'),
    }

    Room_data.append(Room_data)

    return render_template('administrator.html', data=Room_data)

@app.route('/display_Room_info', methods=['GET'])
def display_Room_info():
    data=[]
    return render_template('Room_info.html', data=Room_data)


 


@app.route('/add_ Attendance', methods=['POST'])
def add_Attendance():
    Attendance_data = {
         'Name': request.form.get(' employee_name'),
        'salary': request.form.get(' employee_Salary '),
        'ID': request.form.get('  employee_ID'),
        'attendance': request.form.get(' employee_attdendance '),
    }

    Attendance_data.append(Attendance_data)

    return render_template('administrator.html', data=Attendance)

@app.route('/display_Attendance_info', methods=['GET'])
def display_Attendance_info():
    data=[]
    return render_template('Attendance_info.html', data= Attendance)



@app.route('/add_medicine', methods=['POST'])
def add_medicine():
    medicine_data = {
        'Name': request.form.get('Medicine_name'),
        'price': request.form.get('Medicine_price'),
        'stock': request.form.get('Medicine_stock'),
        'need': request.form.get('Medicine_need'),
     }

    medicines_data.append(medicine_data)

    return render_template('administrator.html', data=medicines_data)


@app.route('/display_medicine_info', methods=['GET'])
def display_medicine_info():
    data=[]
    return render_template('medicine_info.html', data=medicines_data)




 # ... (previous imports and variable definitions)

   # Renamed to avoid conflict with the function name

# ... (previous route handlers)

@app.route('/request_data', methods=['POST'])
def request_data():
    request_entry = {
        'Name1': request.form.get('request1_name'),
        'Name2': request.form.get('request2_name'),
        'Name3': request.form.get('request3_name'),
        'Date_need': request.form.get('request_need'),
    }

    Request_data_list.append(request_entry)  # Corrected variable name

    return render_template('administrator.html', data=Request_data_list)

@app.route('/display_request_info', methods=['GET'])
def display_request_info():
    return render_template('request_info.html', data=Request_data_list)

# ... (other routes and if __name__ == '__main__' block)




if __name__ == '__main__':
    app.run()






     