# main.py
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()



templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == '__main__':
    uvicorn.run(app)



######################################################
# from flask import Flask, render_template, request, jsonify
# from flask_sslify import SSLify
# from flask_socketio import SocketIO, send, emit


# app = Flask(__name__)
# #sslify = SSLify(app)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)



# gameresolution = [680,480]


# @app.route("/")
# def hello():
#     return render_template("index.html")

# @app.route('/playgame', methods=['POST'])
# def playgame():

#     #Calibrate

#     #Start Game
#     #now you can add a buffer and make it a video file

#     anger = request.form['anger']


# if __name__ == "__main__":
#     app.run(debug=True)