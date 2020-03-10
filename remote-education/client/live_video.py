import imagezmq
import socket
import imutils.video
import time

sender = imagezmq.ImageSender(connect_to="tcp://{}:5555".format("localhost"))
hostname = socket.gethostname()
vs = imutils.video.VideoStream().start()
time.sleep(2)

while True:
    frame = vs.read()
    sender.send_image(hostname, frame)

