from flask import Flask

main = Flask(__name__)  # http://127.0.0.1:5000

@main.route('/home')  # http://127.0.0.1:5000/home
def home():
    return "Hello, Flask!"


@main.route('/user/<string:username>')
def get_user_info(username):
    return f"Hello, {username}"

if __name__ == "__main__":
    main.run(debug=True)