#import modules
from flask import flask , jsonify
#get current date module
from  datetime import datetime
#create a flask instance class
app = flask(__name__)
#define the api route
@app.route('/time', methods=['GET'])
#Executes the api routes
def get_current_time():
    return jsonify({"current_time" :datetime.utcnow().isoformat()+ 'z'})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)