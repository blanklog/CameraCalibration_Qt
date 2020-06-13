Camera calibration program base on OpenCV.   A tool. It can calibrate fisheye Lens with charUco chess board and normal chess board.

## Manual

1. First, in createBoard  page create the board which you used in practice.
2. And, in Calib page select the class of board and lens.
3. Then, click calib to  calibrate the Camera.
4. click “save” to save Parameter of Camera.
5. Finally, click outPut  to write Parameters to file.

# Specification

### Calibration

- class of chess board

  - ChessBoard：Normal chess board

  - CharUco：CharUco chess board

  - CharUco+：CharUco chess board, but more strict detection

- class of Lens

  - isFisheLens:  Whether to perform fisheye calibration

### ChessBoard Creation

- Number_X: Number of horizontal grids
- Number_Y: Number of vertical grids
- squareSize：The physical size of a grid
- dpi：dpi of Printer
- print_width: The width of the printing paper
- print_height: The height of the printing paper
- Dict：Class of tag dictionary. The chessBoard means normal chess board.


## Project Introduction

- mainwindow.ui： The Qt designer file
- mianwindow.py:  The code  transformed by mainwindow.u
- mian.py :  Main file
- CharucoBoard.py: CharUco chess board module
- chessBord.py: Nomal chess board module
- CameraGroup.py:  The class of camera group
- Calib.py: Calibration module
- tools：There are scripts of linux and windows
  - call pyside2-uic to transform ui file，and deal erro of defualt transforming.

# Dependence

use pip3 to install

- pyside2 : UI based on Qt

- opencv-python：Function calibration

- opencv-contrib-python：Function of charuco

- numpy

- matplotlib： Plot curve of geometric relationship of fish Lens.	



