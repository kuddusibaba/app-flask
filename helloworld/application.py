#!flask/bin/python
import json
from flask import Flask, Response
import optparse

application = Flask(__name__)

@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

@application.route('/greeting', methods=['GET'])
def greeting():
    return Response(json.dumps({'Output': 'Hello World Greeting of the day'}), mimetype='application/json', status=200)

@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello World POST'}), mimetype='application/json', status=200)
@application.route('/hello')
def hello_get():
   return 'Hello GET'

@application.route('/sum/<a>/<b>')
def sum(a,b):
   return f"""{int(a)+int(b)}"""

@application.route('/sub/<a>/<b>')
def sub(a,b):
   return f"""{int(a)-int(b)}"""


@application.route('/mul/<a>/<b>')
def mul(a,b):
   return f"""{int(a)*int(b)}"""

@application.route('/div/<a>/<b>')
def div(a,b):
   return f"""{int(a)/int(b)}"""

@application.route('/mod/<a>/<b>')
def mod(a,b):
   return f"""{int(a)%int(b)}"""

@application.route('/hello',methods=['POST'])
def hello_post():
   return 'Hello POST'


@application.route('/hello',methods=['HEAD'])
def hello_head():
   return 'Hello HEAD'

@application.route('/hello',methods=['PUT'])
def hello_put():
   return 'Hello PUT'

@application.route('/hello',methods=['PATCH'])
def hello_patch():
   return 'Hello PATCH'

@application.route('/hello',methods=['DELETE'])
def hello_delete():
   return 'Hello DELETE'

@application.route('/helloAll',methods=['GET','POST','PUT','DELETE','PATCH','HEAD'])
def hello_all():
   return 'Hello ALL'


@application.route('/greet')
def greet():
   return f""" Greeting :

Id     :{request.args.get("id")}
Name   :{request.args.get("name")}
Salary :{request.args.get("salary")}

"""

@application.route('/template/welcome')
def template_welcome():
   return f""" 
    <html>
    <head></head>
    <body>
    <h2>Welcome To Flask HTML Template<h2/>
    </body>
    </html>
    """


@application.route('/template/welcome1')
def template_welcome1():
   return render_template('welcome.html')

@application.route('/template/greeting')
def template_greeting():
   user=request.args.get("username");
   return render_template('greeting.html',user=user,
                          messages=['Hello','Greeting','Good Bye','Hi All'],
                          employee={'id':101,'name':'ram','salary':20000},
                          student=(101,'Mohan',15000))

@application.route('/template/employeeform')
def template_employeeform():
   return render_template('employeeform.html')



@application.route('/showdetails',methods=['GET','POST'])
def showdetails():
   if request.method == 'GET':
      return f""" Greeting :
Id     :{request.args.get("id")}
Name   :{request.args.get("name")}
Salary :{request.args.get("salary")}
DOJ    :{request.args.get("doj")}
Methd :{request.method}"""
   else:
      return f""" Greeting :
      Id     :{request.form.get("id")}
      Name   :{request.form.get("name")}
      Salary :{request.form.get("salary")}
      DOJ    :{request.form.get("doj")}
      Methd   :{request.method}"""


if __name__ == '__main__':
    default_port = "80"
    default_host = "0.0.0.0"
    parser = optparse.OptionParser()
    parser.add_option("-H", "--host",
                      help=f"Hostname of Flask app {default_host}.",
                      default=default_host)

    parser.add_option("-P", "--port",
                      help=f"Port for Flask app {default_port}.",
                      default=default_port)

    parser.add_option("-d", "--debug",
                      action="store_true", dest="debug",
                      help=optparse.SUPPRESS_HELP)

    options, _ = parser.parse_args()

    application.run(
        debug=options.debug,
        host=options.host,
        port=int(options.port)
    )
