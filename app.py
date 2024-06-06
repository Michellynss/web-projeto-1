from flask import Flask, render_template
import gunicorn

app = Flask(__name__)

@app.route("/")
def clone():
  return render_template('clone.html')
