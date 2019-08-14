from flask import render_template
from application import app, is_student

@app.route("/")
def index():    
    return render_template("index.html")
