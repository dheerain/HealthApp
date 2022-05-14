from flask import *  
from config import food_config,disease_config,general_instruction
from  student_module import saveNewUser,loadData,storeData
from datetime import timedelta
import os


app = Flask(__name__, static_url_path="", static_folder="templates")  
app.secret_key ='dheerain'


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=10)

@app.route('/')  
def index():
      return render_template('dashboard.html')
      

@app.route('/dashboard')  
def dashboard():
      return render_template('dashboard.html')  

# @app.route('/submit',methods = ['POST'])  
# def submit():  
#       isSuccessful = False
#       if request.method == 'POST':
#             result = request.form
#             print(result)
#             isSuccessful = authenticate(result.get('username'),result.get('password'))
#       if isSuccessful:
#             session['username'] = result.get('username')
#             user = session['username'].upper() if session['username'] else None
#             table = getFeesDelayTable(user.lower())
#             return render_template('index.html',user=user ,session_toggle = "Logout",renderTable = table )
#       else:
#             return render_template('login.html',response= "Invalid Credentials")
      
@app.route('/newadmission')  
def newadmission(): 
      return render_template('newStudent.html',food=food_config.keys(),disease =disease_config.keys() )

# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return result


@app.route('/submitadmissiondata',methods = ['POST'])
def submitAdmissionData():
      
      if request.method == 'POST': 
            result = request.form.to_dict(flat=False)
            data_dict = saveNewUser(result)
            # print(request.form)
            # print(request.form)
            # status  = saveStudentData(result)
            protein = round(sum([keyData[1]*food_config[keyData[0]]['Protein'] for keyData in data_dict['diet']]),2)
            carbs = round(sum([keyData[1]*food_config[keyData[0]]['Carbs'] for keyData in data_dict['diet']]),2)
            fat =round(sum([keyData[1]*food_config[keyData[0]]['Fat'] for keyData in data_dict['diet']]),2)
            calories =round(sum([keyData[1]*food_config[keyData[0]]['Calories'] for keyData in data_dict['diet']]),2)
            a,b,c =data_dict['date'].split('-')
            data_dict['date']='-'.join([c,b,a])
            for keyData in data_dict['diet']:
                  keyData.append(round(keyData[1]*food_config[keyData[0]]['Protein'],2))
                  keyData.append(round(keyData[1]*food_config[keyData[0]]['Carbs'],2))
                  keyData.append(round(keyData[1]*food_config[keyData[0]]['Fat'],2))
                  keyData.append(round(keyData[1]*food_config[keyData[0]]['Calories'],2))
      
      return render_template('dopayment.html' , data = data_dict,disease_config=disease_config,food_config=food_config,general_instruction=general_instruction,protein=protein,carbs=carbs,fat=fat,calories=calories)
      
# @app.route('/attendance_pte')
# def attenance_pte():
#       user = session.get('username', None)
#       if user == None:
#             return redirect("/login")      
#       data = getPTEStudentList()
#       # print(data)
#       return render_template('attendance_pte.html',user=user ,session_toggle = "Logout",date = datetime.date.today().strftime('%Y-%m-%d'),data =enumerate(data))

# @app.route('/attendance_ielts')
# def attenance_ielts():
#       user = session.get('username', None)
#       if user == None:
#             return redirect("/login")      
#       data = getIELTSStudentList()
#       return render_template('attendance_ielts.html',user=user ,session_toggle = "Logout",date = datetime.date.today().strftime('%Y-%m-%d'),data =enumerate(data))

# @app.route('/submit_attendance_data_pte',methods = ['POST'])
# def submit_attenance_pte():
#       user = session.get('username', None)
#       if user == None:
#             return redirect("/login" )      
#       if request.method == 'POST':
#             print("Dheerain")
#             result = request.form
#             print(result)
#             saveAttendanceDataPTE(result)
      
#       return render_template('success.html',user= user,session_toggle = "Logout", head1='Attendance For ' ,head2=  result.to_dict().get('attendanceDate'),information = 'Successfully Saved ')
      
# @app.route('/submit_attendance_data_ielts',methods = ['POST'])
# def submit_attenance_ielts():
#       user = session.get('username', None)
#       if user == None:
#             return redirect("/login" )      
#       if request.method == 'POST':
#             print("Dheerain")
#             result = request.form
#             print(result)
#             saveAttendanceDataIELTS(result)
      
#       return render_template('success.html',user= user,session_toggle = "Logout", head1='Attendance For' ,head2=  result.to_dict().get('attendanceDate'),information = 'Successfully Saved')

@app.route('/search',methods= ['GET','POST'])
def search():
      data =loadData()
      return render_template('search.html', head1='Search For Data' ,head2= '',information = '', data=enumerate(data))

# @app.route('/getStudentData',methods= ['POST'])
# def getStudentData():
#       user = session.get('username', None) 
#       if user == None:
#             return redirect("/login" )
#       if request.method == 'POST':
#             result = request.form.to_dict().get('name')
#             return  render_template('success.html' ,user= user,session_toggle = "Logout", head1='Search For Student Data' ,head2= '',information = '')


@app.route('/showstudentdata/<studentid>',methods= ['GET','POST'])
def showStudentData(studentid):
      print(studentid)
      data =loadData()
      filteredData = data[int(studentid)]
      print(filteredData)
      return  render_template('show_edit_student_data.html' , head1='Search For Student Data' ,head2= '',information = '',data=filteredData,disease =disease_config.keys(),food=food_config.keys(),index=studentid)
      
# @app.route('/dopayment/<studentid>')
# def doPayment(studentid):
#       print(studentid)
#       user = session.get('username', None) 
#       if user:
#             userData = userCredentialDict.get(user.lower())
#             if userData.get('adminAccess') :
#                   data = getPendingInstallmentStatus(studentid)
#                   data['date'] = datetime.date.today()
#                   return  render_template('dopayment.html' ,user= user,session_toggle = "Logout", data = data)
#             else:
#                   return redirect("/")
#       else:
#             return  redirect("/login" )


# @app.route('/savepayment/<studentid>')
# def confirmpayment(studentid):
#       print(studentid)
#       user = session.get('username', None) 
#       if user:
#             data = savePayment(studentid)
#             return  redirect('/')
#       else:
#             return redirect("/login" )

@app.route('/updatestudentdata',methods= ['GET','POST'])
def updateStudentData():
      if request.method == 'POST':
            result = request.form.to_dict(flat=False)
            index =int(result['index'][0])
            data_dict = saveNewUser(result,update=True,index=index)
            protein = round(sum([keyData[1]*food_config[keyData[0]]['Protein'] for keyData in data_dict['diet']]),2)
            carbs =round(sum([keyData[1]*food_config[keyData[0]]['Carbs'] for keyData in data_dict['diet']]),2)
            fat =round(sum([keyData[1]*food_config[keyData[0]]['Fat'] for keyData in data_dict['diet']]),2)
            calories =round(sum([keyData[1]*food_config[keyData[0]]['Calories'] for keyData in data_dict['diet']]),2)
            a,b,c =data_dict['date'].split('-')
            data_dict['date']='-'.join([c,b,a])

            for keyData in data_dict['diet']:
                  keyData.append(round(keyData[1]*food_config[keyData[0]]['Protein'],2))
                  keyData.append(round(keyData[1]*food_config[keyData[0]]['Carbs'],2))
                  keyData.append(round(keyData[1]*food_config[keyData[0]]['Fat'],2))
                  keyData.append(round(keyData[1]*food_config[keyData[0]]['Calories'],2))

            return render_template('dopayment.html' , data = data_dict,disease_config=disease_config,food_config=food_config,general_instruction=general_instruction,protein=protein,carbs=carbs,fat=fat,calories=calories)


# @app.route('/<name>.html')
# def restrictFileAccess(name):
#       print(name)
#       if name == 'components':
#             return render_template('components.html')
#       user = session.get('username', None) 
#       if not user:
#             return redirect("/login" )
#       else:
#             return redirect("/" )

if __name__ == '__main__':  
      if not os.path.exists('userData.db'):
            storeData()
      loadData()
      app.run( host='::',debug = True,port=5000)  