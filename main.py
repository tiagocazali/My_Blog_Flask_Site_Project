from flask import Flask, render_template

app = Flask(__name__)

users_list = ["Tiago", "Robert", "Ana", "Vanessa", "Marcus", "Andi"]

@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/users")
def users():
    return render_template("users.html", users_list=users_list)



if __name__ == "__main__":
    app.run(debug=True)