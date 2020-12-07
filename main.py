#print("Mourya")

from flask import Flask,request,jsonify
import coref

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

"""
    expected input:
     {
        "text" : "text that you need to send"     
    }
    expected ouput:
    {
        "text" : "output text"
    }
"""

@app.route('/getCoreRef', methods=['GET', 'POST'])
def perform_coreref():
    my_json = request.json
    text = my_json['text']
    text = coref.coref(text)
    my_dict = dict()
    my_dict['text'] = text
    return jsonify(my_dict)

app.run()