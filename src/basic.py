from flask import Flask , render_template , url_for, abort
app = Flask(__name__)

@app.route('/Home/')
def Home():
    return render_template('basic.html') 


@app.route('/Home/SPL/')
def SPL():
      return render_template('spl.html')

@app.route('/Home/Aberdeen/')
def Aberdeen():
  start = '<img src="'
  url = url_for('static' , filename='aberdeen1.png')
  end = '">'
  return start+url+end , 200

@app.route('/Home/Celtic/')
def Celtic():
  start = '<img src="'
  url = url_for('static' , filename ='celtic1.png')
  end = '">'
  return start+url+end , 200

@app.route('/Home/Dundee/')
def dundee():
  start = '<img src="'
  url = url_for('static' , filename='dundee1.png')
  end = '">'
  return start+url+end , 200

@app.route('/Home/DundeeUnited/')
def dundee_united():
  start = '<img src="'
  url = url_for('static' , filename='dundee_united1.png')
  end = '">'
  return start+url+end , 200

@app.route('/Home/Hamilton/')
def hamilton():
  start = '<img src="'
  url = url_for('static' , filename='hamilton1.png')
  end = '">'
  return start+url+end , 200

@app.route('/Home/Hearts/')
def hearts():
  start = '<img src="'
  url = url_for('static' , filename='hearts1.png')
  end = '">'
  return start+url+end , 200

@app.route('/Home/Inverness/')
def inverness():
  start = '<img src="'
  url = url_for('static' , filename='inverness1.png')
  end = '">'
  return start+url+end , 200

@app.route('/Home/Kilmarnock/')
def killie():
  start = '<img src="'
  url = url_for('static' , filename='killie1.png')
  end = '">'
  return start+url+end , 200

@app.route('/Home/Motherwell/')
def motherwell():
  start = '<img src="'
  url = url_for('static' , filename='motherwell1.png')
  end = '">'
  return start+url+end , 200

@app.route('/Home/Partick/')
def partick():
  start = '<img src="'
  url = url_for('static' , filename='partick1.png')
  end = '">'
  return start+url+end , 200

@app.route('/Home/RossCounty/')
def ross():
  start = '<img src="'
  url = url_for('static' , filename='ross1.png')
  end = '">'
  return start+url+end , 200

@app.route('/Home/Saints/')
def saints():
  start = '<img src="'
  url = url_for('static' , filename='saints1.png')
  end = '">'
  return start+url+end , 200

@app.route('/Home/SPL/error404')
def error404():
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
  return "Coudln't find the page you requested.", 404

if __name__ == ("__main__"):
    app.run(host='0.0.0.0' , debug=True)

