from flask import Flask
app = Flask(__name__)

@app.route("/")
def trust():
  return "All services ok"
