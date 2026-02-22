from picamera2 import Picamera2, Preview

class Camera(object):
    def __init__(self):
        self.camera = Picamera2()
        # 配置预览
        preview_config = self.camera.create_preview_configuration(
            main={"size": (640, 480)},
            controls={"FrameRate": 30}
        )
        self.camera.configure(preview_config)
        self.camera.start()


    def get_frame(self):
        return self.camera.capture_array()

if __name__ == "__main__":
    camera = Camera()
    while True:
        frame = camera.get_frame()
        print(frame)
    # camera.__del__()
    # cv2.destroyAllWindows()
