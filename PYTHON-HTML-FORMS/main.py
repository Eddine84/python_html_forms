from flask import Flask, render_template,request



app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('index.html')


@app.route('/login',methods=["GET","POST"])
def login():
   if request.method == "POST":
      username = request.form["username"]
      password = request.form["password"]
      return render_template('secret.html',username=username,password=password)
   
   else:
      return render_template('login.html')
      
   

# @app.route('/secret',methods=["GET","POST"])
# def receive_data():
#    return render_template('secret.html')



if __name__ == "__main__":
    app.run(debug=True)