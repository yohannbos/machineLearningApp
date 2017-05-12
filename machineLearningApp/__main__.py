from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    customers = ["Hafid Traikzi","Yohann Bosco", "Carole Gombauld", "Yannick François"]
    return render_template('home.html', customers=customers)

if __name__ == "__main__":
    app.run()

