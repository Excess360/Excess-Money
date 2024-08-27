from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your own secret key

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'aderibigbeahmedadebayo.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'aderibigbeahmedadebayoemail@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'Aderibigbe1'  # Replace with your email password

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        if not name or not email or not message:
            flash('Please fill out all fields.')
            return redirect('/')
        
        # Send email
        try:
            msg = Message(subject=f"New message from {name}",
                          sender=email,
                          recipients=['aderibigbeahmedadebayoemail@gmail.com'],  # Replace with your email
                          body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")
            mail.send(msg)
            flash('Thank you for your message! We will get back to you shortly.')
            return redirect('/')
        except Exception as e:
            flash('Sorry, something went wrong. Please try again later.')
            return redirect('/')

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
