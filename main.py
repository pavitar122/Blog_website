from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import Register_form

app = Flask(__name__)
app.config['SECRET_KEY'] = "dgiufhuhewhfuwhfuwbubwugbw"
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register")
def register():
    form = Register_form()
    return render_template("register.html", form=form)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
