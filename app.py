from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")  
def home():
  return render_template('examples/home.html')

@app.route("/reward")  
def reward():
  return render_template('examples/reward.html')

  
@app.route("/annotation")  
def annotation():
  return render_template('examples/annotation.html')

if __name__ == "__main__":
  app.run(debug = True)