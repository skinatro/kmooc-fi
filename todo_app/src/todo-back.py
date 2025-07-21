""" 
Backend for the ToDo app
"""
import os
from flask import Flask, request , jsonify, redirect

app = Flask(__name__)

# We will store the data in a dict
todo = []

@app.route('/todos', methods = ['GET','POST'])
def todos():
    """
    GET -> Request will retrieve the data
    POST -> Will store the data 
    """
    if request.method == 'GET':
        return jsonify(todo)

    if request.method == 'POST':
        new_task = request.form.get('todo')
        todo.append(new_task)
        return redirect("/")
 
if __name__ == '__main__':
    PORT = os.environ.get("PORT","5555")
    app.run(host="0.0.0.0",port=int(PORT), debug=False)
