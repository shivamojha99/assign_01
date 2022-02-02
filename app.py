from crypt import methods
from distutils.log import debug
from flask import Flask,render_template, request,url_for
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        return 'Congratulation! for entering the data'
    else:    
        return render_template('index.html')

        

if __name__ =="__main__":
    app.run(debug=True)
