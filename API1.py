from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check_access', methods=['POST'])
def check_access():
    # Get the user's country from the request body
    data = request.json
    user_country = data.get('country')

    # Check if the country is India or Singapore
    if user_country in ['India', 'Singapore']:
        return jsonify({'access': True}), 200
    else:
        return jsonify({'access': False}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
