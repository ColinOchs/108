from flask import Flask

app = Flask("Server")


@app.route("/")
def home():
    return "Greetings! Welcome to the site"

@app.route("/me")
def about_me():
    return "Colin Ochs"


app.run(debug=True)