from flask import Flask
app= Flask(__name__)

@app.route('/',methods=["GET"])
def route1():
    return "<h1> this is python running on port: 5500 </h1>"

@app.route('/version',methods=["GET"])
def route2():
    return "<h1>version is : 10.0v</h1>"

@app.route('/update',methods=["GET"])
def route3():
    return "<h1>update is available: 1.5</h1>"

app.run(port=5500,host="0.0.0.0",debug=True)