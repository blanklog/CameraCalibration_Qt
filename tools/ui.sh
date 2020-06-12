#!/bin/bash
#conda activate cv-py
pyside2-uic mainwindow.ui -o mainwindow.py
sed -i "s/string()/""/g" mainwindow.py
