from flask import Flask, request

app = Flask(__name__)

@app.route('/getcountrybyuser', methods=['POST'])
def check_access():
    # Get the user's information from the request body
    data = request.json
    user_country = data.get('user')

    # Check if the user belongs to India or Singapore
    if user_country in ['user1', 'user2']:
        return 'India', 200
    elif user_country in ['user3']:
        return 'Singapore', 200
    else:
        return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
