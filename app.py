
from flask import Flask,render_template, url_for , request
from flask_mail import Mail, Message
import os


app = Flask(__name__)
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME']= 'elmondrivarez21@gmail.com'
app.config['MAIL_PASSWORD'] = 'qszafykwttrwvkwf'
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET","POST"] )
def contact():
    if request.method == "POST":
        message = request.form["message"]
        name = request.form["name"]
        email = request.form["email"]
        msg = Message(name, sender="noreply@demo.com",recipients=["elmondrivarez@gmail.com"])
        msg.body = f"{message}  {email}"
        mail.send(msg)
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)