# 各関数の仕様書(参考)
以下に各週における成果物(CanSat制御に使用するプログラム/関数)の仕様を示す．<br>
目次<br>
* <a href = "#01"> motor.py </a>
* <a herf = "02"> camera.py </a>

<h2 id = "01">1. motor.py </h2>

**関数一覧**
|関数名|概要|
|-|-|
|motor|モータ制御一般を提供する|

**依存ライブラリ**
- RPi.GPIO
- time

### 1.1 関数仕様
#### 1.1.1 `move(duty:int, dir:str) -> None`
**引数**<br>
- `duty`(int)：PWM制御におけるDuty比を指定<br>
- `dir`(str)：機体の移動方向を指定( forward | right | left )

**返り値**<br>
- `None`：返り値はない

**用法**<br>
```py
move(duty = 40 , dir = "forward")
```

<h2 id = "#02"> 2. camera.py </h2>

**関数一覧**
|関数名|機能|
|-|-|
|capture|picameraで静止画を撮影をする|

**依存ライブラリ**
- picamera2

### 2.1 関数仕様
#### 2.1.1 `capture(height:int,width:int,cnt:int) -> None`
**引数**
- `height`(int)：静止画の縦のピクセル数
- `width`(int)：静止画の横のピクセル数
- `cnt`(int)：画像保存の際のファイル名に使用する値

**返り値**
- `None`：返り値はない

**用法**
```py
capture(height=480,width=680,cnt=0)
```
実行すると「cnt_YYYYMMDD-HHMMSSmm.jpg」が保存される．

<h2 id = "#03"> 3. image_processing.py </h2>

**関数一覧**
|関数名|機能|
|-|-|
|imgprocess|画像からカラーコーンの座標を取得する|

**依存ライブラリ**
- OpenCV
- NumPy

### 3.1 関数仕様
#### 3.1.1 `imgprocess(cnt:int,height:int,width:int) -> dir:str`
**引数**
- `cnt`(int)：カウント(画像を読み込む用)
- `height`(int)：画像の縦のピクセル数
- `width`(int)：画像の横のピクセル数

**返り値**
- `dir`(str)：進行方向( forward | right | left )を返す

**用法**
```py
dir = imgprocess(cnt = 0, height = 480, width = 640)
```
imgprocess内部で撮影した画像を読み込み，それに対し画像処理を行う．画像処理結果から，CanSatが進むべき方向を返す．

<h2 id = "#04"> logging.py </h2>
logging.pyはPythonの標準ライブラリloggingを使用し，また，各関数に組み込むため，記述しない．