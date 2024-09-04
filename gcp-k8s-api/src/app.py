from flask import Flask, jsonify
#get current date module
from datetime import datetime
import pytz  # Import pytz for time zone handling

#create a flask instance class
app = Flask(__name__)

#define the api route
@app.route('/time', methods=['GET'])
#Executes the api routes
def get_current_time():
    # Set the time zone for Nigeria
    timezone = pytz.timezone('Africa/Lagos')  # Nigeria's time zone
    current_time = datetime.now(timezone).isoformat() + 'Z'
    return jsonify({"current_time": current_time})

#  error handler for 404 errors
# @app.errorhandler(404)
# def not_found(error):
#     return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
