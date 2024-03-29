import pyrealsense2 as rs
import numpy as np
import cv2

pipe = rs.pipeline()
cfg = rs.config()

cfg.enable_stream(rs.stream.color, 640,480, rs.format.bgr8, 30)
cfg.enable_stream(rs.stream.depth, 640,480, rs.format.z16, 30)

pipe.start(cfg)

point = (320,240)

while True:
    frame = pipe.wait_for_frames()
    depth_frame = frame.get_depth_frame()
    color_frame = frame.get_color_frame()

    depth_image = np.asanyarray(depth_frame.get_data())
    color_image = np.asanyarray(color_frame.get_data())
    depth_cm = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha = 0.5), cv2.COLORMAP_JET)
    color_image = cv2.circle(color_image, point, 2, (0, 0, 255), -1) 


    cv2.imshow('rgb', color_image)
    # cv2.imshow('depth', depth_image)
    cv2.imshow('cm', depth_cm)

    print(depth_frame.get_distance(320,240))

    if cv2.waitKey(1) == ord('q'):
        break

pipe.stop()
