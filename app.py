from flask import Flask, render_template, make_response,request

app = Flask(__name__)


@app.route('/')
def index():
    admin_secret = request.cookies.get('admin_secret')
    flag = False
    if admin_secret == '1':
        flag = True
    response = make_response(render_template('index.html', flag=flag))
    if admin_secret != '1':
        response.set_cookie('admin_secret', '0')
    return response

@app.route('/testurl')
def testurl():
    return "error", 409

@app.route('/testbtn')
def testbtn():
    return "error", 500

@app.route('/testbtnd')
def testbtnd():
    return "error", 507

@app.route('/btncom')
def btncom():
    return "error", 444

@app.route('/hiddenurl')
def hiddenurl():
    return "error", 555

@app.route('/secreturl')
def secreturl():
    return "error", 577


if __name__ == '__main__':
    app.run(debug=True)
