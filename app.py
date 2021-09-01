from flask import Flask, render_template, request, jsonify
from flask_sslify import SSLify
from flask_socketio import SocketIO, send, emit
import eventlet


app = Flask(__name__)
#sslify = SSLify(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)



gameresolution = [680,480]


@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/playgame', methods=['POST'])
def playgame():

    #Calibrate

    #Start Game
    #now you can add a buffer and make it a video file

    anger = request.form['anger']


if __name__ == "__main__":
    app.run(debug=True)