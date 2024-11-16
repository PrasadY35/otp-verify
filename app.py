from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mail import Mail, Message
import random
import os

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

# Configure Flask-Mail for SMTP (Gmail)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "prasadyammi2@gmail.com"
app.config["MAIL_PASSWORD"] = "oakc tqgf pgst klyh"  # Use an App Password here
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True

mail = Mail(app)

# OTP storage (for demonstration)
otp_storage = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_otp', methods=['POST'])
def send_otp():
    email = request.form['email']
    otp = str(random.randint(100000, 999999))  # Generate a 6-digit OTP

    # Save OTP (in a real application, save in database)
    otp_storage[email] = otp

    # Send email
    msg = Message("Your OTP Code", sender="prasadyammi2@gmail.com", recipients=[email])
    msg.body = f"Your  helllo pappa this is which i have genareted otp how it worked OTP is {otp}. Please use this to complete verification."
    try:
        mail.send(msg)
        flash("OTP sent to your email. Check your inbox!", "success")
        session['email'] = email  # Store email in session for verification
    except Exception as e:
        flash("Error sending OTP. Try again later.", "danger")

    return redirect(url_for('verify_otp'))

@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        email = session.get('email')
        entered_otp = request.form['otp']
        if email and otp_storage.get(email) == entered_otp:
            flash("OTP verified successfully!", "success")
            # Clear the OTP after successful verification
            otp_storage.pop(email, None)
            return redirect(url_for('index'))
        else:
            flash("Invalid OTP. Please try again.", "danger")
    return render_template('verify.html')

if __name__ == "__main__":
    app.run(debug=True)
