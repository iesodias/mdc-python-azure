from flask import Flask, render_template, make_response, Request, jsonify, json
from flask_restful import Resource, Api
import socket, os

app = Flask(__name__, template_folder='templates_folder')

@app.route("/bootcamp/app1/goku")
def goku():
  return render_template('goku.html')

@app.route("/bootcamp/app1/ping/<host>", methods=['GET'])
def ping_host(host):
    result = os.system(f'ping -c 3 {host}')

    if result == 0:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failure"})

@app.route("/bootcamp/app1/host")
def host():
  return render_template('host.html', id_container=socket.gethostname())

@app.route("/bootcamp/app1/success", methods=["GET"])
def success():
    response = make_response("<h1>Success</h1>", 200)
    return response

@app.route("/bootcamp/app1/denied", methods=["GET"])
def denied():
    response = make_response("<h1>Denied</h1>", 500)
    return response

@app.route("/bootcamp/app1/notfound", methods=["GET"])
def notfound():
    response = make_response("<h1>NotFound</h1>", 404)
    return response

if __name__ == "__main__":
 port = int(os.environ.get('PORT', 5000))
 app.run(debug=True, host='0.0.0.0', port=port)

# from flask import Flask, render_template, make_response, Request
# from flask_restful import Resource, Api
# import socket, os

# app = Flask(__name__, template_folder='templates_folder')

# @app.route("/bootcamp/app1/goku")
# def goku():
#   return render_template('goku.html')

# @app.route("/bootcamp/app1/host")
# def host():
#   return render_template('host.html', id_container=socket.gethostname())

# @app.route("/bootcamp/app1/success", methods=["GET"])
# def success():
#     response = make_response("<h1>Success</h1>", 200)
#     return response

# @app.route("/bootcamp/app1/denied", methods=["GET"])
# def denied():
#     response = make_response("<h1>Denied</h1>", 500)
#     return response

# @app.route("/bootcamp/app1/notfound", methods=["GET"])
# def notfound():
#     response = make_response("<h1>NotFound</h1>", 404)
#     return response

# if __name__ == "__main__":
#  port = int(os.environ.get('PORT', 5000))
#  app.run(debug=True, host='0.0.0.0', port=port)





# # @app.route("/userDetails", methods=["GET", "POST"])
# # def user_details():

# #     if request.method == "POST":
        
# #         username = request.form.get("username")
# #         firstname = request.form.get("firstname")
# #         lastname = request.form["lastname"]

# #         response = make_response("<h1>Success</h1>", 201)
# #         return response

# # @app.route("/userSignUp", methods=["POST"])
# # def sign_up():

# #     if request.method == "POST":

# #         username = request.form.get("username")
# #         password = request.form.get("password")
        
# #         response = make_response("<h1>Success</h1>")
# #         response.status_code = 200
# #         return response