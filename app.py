import json
from flask import Flask, request, render_template

startingPoints = 50


people = {
    "Jess": {"points": 10, "points_to_give": startingPoints},
    "Logan": {"points": 8, "points_to_give": startingPoints},
    "Camden": {"points": 12, "points_to_give": startingPoints},
    "Lily": {"points": 12, "points_to_give": startingPoints}
    # Add more people as needed
}


#people["Camden"] = people["camden"] + 10


file_path = "./data.json"
json_string = json.dumps(people,indent=4)

with open(file_path, 'w') as json_file:
   json_file.write(json_string)


#Spin Up Flask Server
#Anything before the site should be up needs to be before this
   
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#End of Flask Server