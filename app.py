from flask import Flask, render_template, Response
import configparser
from VideoStreamSubscriber import VideoStreamSubscriber

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config/app.ini')
HOSTNAME = config['PUBLISHER']['HOSTNAME']
PORT = int(config['PUBLISHER']['PORT'])

receiver = VideoStreamSubscriber(HOSTNAME, PORT)


def gen():

    while True:
        msg, frame = receiver.receive()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@ app.route('/')
def index():
    # """Video streaming"""
    return render_template('index.html')


@ app.route('/video_feed')
def video_feed():
    # """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run()
