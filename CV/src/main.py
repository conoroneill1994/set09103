from flask import Flask ,flash , render_template , url_for , abort, request , redirect
app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route("/private/")
def private():
    return redirect(url_for('Main'))

@app.route('/Home/')
def Main():
        return render_template('home.html')

@app.route('/Home/Review/')
def review():
        return render_template('review.html')

@app.route('/Home/Thankyou/')
def thanks():
        return render_template('apply.html')

@app.route('/')
def index():
    return render_template('index.html')

    return "Root Page"

@app.route('/login/<message>')
def login(message):
    if (message != None):
      flash(message)
    flash("A default message")
    return "Login Isn't working jsut now Please Try again later"


@app.route('/Home/error404/')
def error404():
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page you requested.", 404

@app.route('/account/', methods=['GET' , 'POST'])
def account():
  if request.method == 'POST':
    return "POST'ed to /account root\n"
  else:
    return "GET /account root"

@app.route('/display/')
def display():
  return '<img src="'+url_for('static' , filename='uploads/file.png')+'"/>'

@app.route('/Home/Apply/')
def apply():
  if request.method == 'POST':
    f = request.files['datafile']
    f.save('static/uploads/file.png')
    return "File Uploaded"
  else:
    page='''
    <html>
    <head>
    <title>Job Finder | Apply Page</title>
    <link rel="stylesheet" type="text/css" href="/static/main.css">
    </head>
    <body>
    <div id="header">
    <div class="heading">
    Job Finder -<span style="font-size:20px"> Find the job your looking
    for</span></div>
    </div>
    <div id="nav">
    <div class="nav2">
    <a href="/Home">Home</a></div>
    <div class="nav3">
    <a href="/Home/Review">Review</a></div>
    </div>
    <img id="logo" src="/static/cv.png"/>
    </div>
    <div class="main">
    Apply For job Below !!
    </div>
    <form action="" id="upload" method="post" name="form" enctype="multipart/form-data">
    First name: <input type="text" name="fname"></br></br>
    Last name: <input type="text" name="lname"></br></br>
    Email Address: <input type="text" name="email"></br></br>
    Please Upload Your CV Below!!</br></br>
    <input type="file" name="datafile" />
    </form>
    
    <div class="button">
    <a href="/Home/Thankyou">Apply</a>
    </div>
        <div id="footer">
    <div class="copyright">
    &#169; Copyright 2015 | Conor O'Neill
    </div>
    <img id="fb" src="/static/fb.png"/></div>
    <img id="twitter" src="/static/twitter.png"/></div>
    <img id="linked" src="/static/linkedIn.png"/></div>
    </div>
    </body>
    </html>
    '''
    return page , 200

if __name__ == ("__main__"):
    app.run(host='0.0.0.0' , debug=True)
