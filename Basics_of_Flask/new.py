from flask import Flask, render_template,redirect, url_for

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')
    # return "<h1> Welcome to the home page </h1>"
    # return "hello" 

@app.route('/aboutus')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return redirect('aboutus')

@app.route('/visitus')
def visit():
    return redirect(url_for('about'))

@app.route('/welcome/<int:id>')
def welcome(id):
    # id = int(input("Enter the id number: "))
    return f"hello {id}"
    # return render_template('welcome.html')
    # return f"hello {name}"

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html',  idname = name )

# @app.route('/hello/')
# def hello():
#     idname = input("Enter the name: ")
#     return render_template('hello.html',  idname = idname )

if __name__ == "__main__":
    app.run(debug = True,port = 8000)
    
    

    
    