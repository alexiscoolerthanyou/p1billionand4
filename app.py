# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid = 'Enter your account_sid here'
        auth_token = 'Enter your auth_token here'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('Enter your service ID') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('Update user_error html file here')




def get_otp():
    print('processing')

    received_otp = request.form['received_otp']
    mobile_number = request.form['number']

    account_sid = 'ACa2c74b9ed94c01edae2c3af8e7a5cead'
    auth_token = 'fbb7e6938268d77c6c06be8326319bdc'
    client = Client(account_sid, auth_token)
                                            
    verification_check = client.verify \
        .services('IS5cb55c56064bb65fbd6259f3b70e7b06') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    print(verification_check.status)

    if verification_check.status == "pending":
        return render_template('otp_verify.html')    
    else:
        return redirect("https://project-c272.onrender.com/")








    verification_check = client.verify \
        .services('Enter your service ID') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    

   







if __name__ == "__main__":
    app.run()

