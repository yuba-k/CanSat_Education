from picamera2 import Picamera2
from datetime import datetime

def capture(height, width, cnt):

    picam2 = Picamera2()

    # 静止画用設定（解像度指定）
    config = picam2.create_still_configuration(main={"size": (width, height)})
    picam2.configure(config)

    # カメラ起動
    picam2.start()

    # ファイル名（撮影番号と日時入り）
    filename = ~~~~~~~~~~~~~~~

    # 撮影して保存
    picam2.capture_file(filename)

    # カメラ停止
    picam2.close()