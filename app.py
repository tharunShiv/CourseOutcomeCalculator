"""from flask import Flask,render_template
from data import articless

app = Flask(__name__)
Article = articless()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def aboutus():
    return render_template('aboutus.html')

@app.route('/articles')
def articles():
    return render_template('articles.html',Articlepara = Article)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html',id =id)

if __name__ == '__main__':
    app.run(debug=True)
    """
from flask import Flask, render_template, request,redirect
from dscecalc import Cal
from newCalc import Cal2
app =Flask(__name__,static_folder = 'C:\\Users\\tharu\\Desktop\\myflaskapp\\static')

@app.route('/')
def upload():
   return render_template('home.html')

@app.route('/co-calc', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      pathf = "NewFile/"+(f.filename)
      f.save(pathf)
      answer = Cal(pathf)
      extradict_ans = Cal2(pathf)

      print(answer)
      print(extradict_ans)
      #print(extradict_ans)
      return render_template('upload.html',ans = answer,extra_dict=extradict_ans)
   else:
       return redirect("/", code=302)


if __name__ == '__main__':
   app.run(debug = True)
