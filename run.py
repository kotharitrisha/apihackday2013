import os
from flask import Flask, request, redirect
#import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello():
    print request.values.get('From', None)
   # resp=twilio.twiml.Response()
   # resp.sms("Hello, Mobile Monkey")
   # return str(resp)

if __name__=="__main__":
    app.run(debug=True)
