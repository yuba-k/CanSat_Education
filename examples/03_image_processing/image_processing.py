import cv2
import numpy as np
from typing import Dict

"""imgprocess

Args:
    cnt (int): 画像読込用．画像は「cnt_YYYYMMDD-HHMMSSmm.jpg」で保存されている．
    height (int): 画像の縦ピクセル数
    width (int): 画像の横ピクセル数

Returns:
    str: CanSatが進むべき方向を返す(forward | right | left)
"""

def imgprocess(cnt:int,height:int,width:int) -> str:
    #辞書の宣言
    x = {}; y = {}
    #赤色抽出の処理を記述

    # binary = 処理後の画像(二値化する)
    x, y = get_target_points(img = binary,height = height, width = width)

    # CanSatの進行方向を決める処理

    # dir = 進行方向
    return dir

def get_target_points(img:np.ndarray,height:int,width:int) -> Dict[str,int]:
    """get_target_points

    Args:
        img (np.ndarray): 処理済み二値画像(赤色抽出済み)
        height (int): 画像の縦ピクセル数
        width (int): 画像の横ピクセル数

    Returns:
        Dict[str,int]: 頂点の座標
    """
    coordinates_x = {}
    coordinates_y = {}
    temp = np.where(binary==255)
    coordinates_x["top"] = temp[1][0]
    coordinates_y["top"] = temp[0][0]
    binary = cv2.rotate(binary,cv2.ROTATE_90_CLOCKWISE)

    temp = np.where(binary==255)
    coordinates_x["left"] = temp[0][0]
    coordinates_y["left"] = abs(height-temp[1][0])
    binary = cv2.rotate(binary,cv2.ROTATE_90_CLOCKWISE)
    binary = cv2.rotate(binary,cv2.ROTATE_90_CLOCKWISE)

    temp = np.where(binary==255)
    coordinates_x["right"] = abs(width-temp[0][0])
    coordinates_y["right"] = temp[1][0]

    return coordinates_x, coordinates_y
