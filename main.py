from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from forms import Register_form
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "dgiufhuhewhfuwhfuwbubwugbw"
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class New_user(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = Register_form()
    if form.validate_on_submit():
        add_user = New_user(
            email=form.email.data,
            password=form.password.data,
            name=form.name.data
        )
        db.session.add(add_user)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("register.html", form=form)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
