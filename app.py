from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Flask(__name__)
CORS(app)  


sender_email = "recruting.made.easy@gmail.com"
receiver_email = "itanzteste@gmail.com"
password = "RecrutingEasy1999"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submitForm', methods=['POST'])
def handle_form_submission():
    try:
        data = request.get_json()

        print("Received form data:", data)   
        
        name = data['name']
        email = data['email']
        info = data['info']
        
        
        
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "New Form Submission!"
        
    
        body = f"Name:{name}\nemail{email}\ninfo{info}"
        message.attach(MIMEText(body, "plain"))

        smtp_server = "smtp.gmail.com"
        port = 465

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        
        

        return jsonify({"message": "Form data received successfully!"})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True,port=3000)