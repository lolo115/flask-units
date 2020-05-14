from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def printLink():
    return render_template("example1.html", message="Hello Flask!", contacts = ['laurent', 'valerie', 'oscar', 'lison']);

if __name__ == "__main__":
        app.run(host='0.0.0.0', port= 8090, debug=True)
