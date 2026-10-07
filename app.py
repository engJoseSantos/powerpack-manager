
from flask import Flask, render_template
from models import Battery

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')


def test_models():
    new_b = Battery(1,"Parkside", 20, 2.4, 3)
    print(new_b)

if __name__ == "__main__":
    #test_models()
    app.run(debug=True)