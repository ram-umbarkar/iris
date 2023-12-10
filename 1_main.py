from flask import Flask,render_template,request,jsonify

my_app = Flask(__name__)

@my_app.route('/')   ### Default API
def index():
    return render_template('1_index.html')

# @my_app.route('/get_data', methods = ['GET','POST'])  ### Default GET Method 
# def get_data():
#     data = request.form['var']
#     data1 = request.form['var1']
#     print(f"{data=},{data1=}")
    
#     return "Data Receieved"

# @my_app.route('/get_data',methods=['GET','POST'])
# def get_data():
#     data1=request.form['value1']
#     data2=request.form['value2']
#     data3=request.form['value3']
    
#     if request.method=='POST':
#         print(f"{data1=},{data2=}")
#         return'Post method is used here'
#     else:
#         print(f"{data3=}")
#         return'post method not used here'
    


# @my_app.route('/get_data', methods = ['GET','POST'])  ### Default GET Method 
# def get_data():
#     data = request.form 
    
#     print(f"{data=}")
#     print(type(data))
#     data_from_imm = data['var1']
#     print(data_from_imm)
#     return render_template('1_index.html')
        


# @my_app.route('/get_data', methods = ['GET','POST'])  ### Default GET Method 
# def get_data():
#     data = request.form 
    
#     print(f"{data=}")
#     print(type(data))
#     data_from_imm = data['var1']
#     print(data_from_imm)
#     return jsonify(data)
        

# @my_app.route('/get_data', methods = ['GET','POST'])  ### Default GET Method 
# def get_data():
#     data = request.get_json() ### DATA in form in dict(this req.get_json object accept json datatype only from frontend input)
    
#     print(f"{data=}")
#     print(type(data))
#     frontend_input = data['var1']
#     print(frontend_input)
#     return "Data Receieved"

# @my_app.route('/json_data',methods=["GET","POST"])
# def json_op():
#     Data=request.json # its similar to request.get_json() object return similar output result in dict format
#     print(f"{Data=}")
#     print(type(Data))
#     frontend_input=Data["var1"] 
#     print(frontend_input)# 1st input value here print from frontend value we input there
#     return "Data Recieve"   
 

@my_app.route('/login')
def login():
    """ this is login route"""
    a=10
    print(a)
    

if __name__ == "__main__":
    my_app.run(debug=True)