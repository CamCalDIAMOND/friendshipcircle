import json
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

startingPoints = 1000


people = {   
   "jess": startingPoints,
   "lily": startingPoints,
   "logan": startingPoints,
   "camden": startingPoints
}

people["camden"] = people["camden"] + 10


file_path = "./data.json"
json_string = json.dumps(people,indent=4)

with open(file_path, 'w') as json_file:
   json_file.write(json_string)
