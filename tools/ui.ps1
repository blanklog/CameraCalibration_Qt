conda activate qt
pyside2-uic mainwindow.ui -o mainwindow.py
$file = Get-Content ./mainwindow.py
$reg = "QString\(\)"
$out= $file -replace $reg, "`"`""  
Set-Content ./mainwindow.py $out
   
