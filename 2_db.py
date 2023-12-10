from flask import Flask,render_template,request,jsonify
import mysql.connector
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('1_index.html')

@app.route('/student_data',methods=['POST'])
def student_data():
    s_name=request.form['std_name']
    s_no=request.form['std_roll_no']
    s_sub1=request.form['std_sub1']
    s_sub2=request.form['std_sub2']
    s_sub3=request.form['std_sub3']
    print(f"student_Name={s_name}")
    
    conn = mysql.connector.connect(host = 'localhost',
                              database='flask_api',
                              user='root',
                              password='Dt-Mysql51')
    cursor = conn.cursor()
    query= "INSERT INTO Students(Name,Roll_no,subject_1,subject_2,subject_3) VALUES(%s,%s,%s,%s,%s)" # %s is use for mapping(or catch) following table name value from data varaiable one by one
    data = (s_name,s_no,s_sub1,s_sub2,s_sub3) # passed in the tuple value
    cursor.execute(query,data)

    conn.commit()
    conn.close()
    return "Student Data Recieved"
    
if __name__ == "__main__":
    app.run(debug=True)

