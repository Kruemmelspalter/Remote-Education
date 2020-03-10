import imagezmq
import cv2

image_hub = imagezmq.ImageHub()
while True:
    hostname, frame = image_hub.recv_image()
    if frame is not None:
        cv2.imshow(hostname, frame)
        cv2.waitKey(1)
        image_hub.send_reply(b'OK')