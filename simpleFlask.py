from flask import Flask
 
app = Flask(__name__)
 
@app.route('/hello')
def helloWorldHandler():
    return 'Hello World from Flask!'

@app.route('/')
def printLink():
    return "Hello <a href='/hello'>click here</a>";
    
if __name__ == "__main__":
	app.run(host='0.0.0.0', port= 8090, debug=True)

