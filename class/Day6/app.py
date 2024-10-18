from flask import Flask,request,render_template
import test
# from mod1 import greetings

# Create the Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/home')
def diplay():
    return "coming from home"

@app.route('/contactUs')
def contactUs():
    return 'call us at mobile number  is : 8623038879'

@app.route('/aboutUs')
def aboutUs():
    return 'we are small start up company where provide training'

@app.route('/services')
def sevices():
    return 'call us at mobile number  is : 8623038879'
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/createUser',methods=['post'])
def postReq():
    print(request.get_json())
    return 'user created suucessfully'

@app.route('/updateUser',methods=["put"])
def updateUser():
    return 'user update successfully'

@app.route('/smallUpdateUser',methods=['patch'])
def smallUpdateUser():
    return 'user small Update successfully '

@app.route('/deleteUser',methods=['delete'])
def deleteUser():
    return 'user deleted successfully'

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)