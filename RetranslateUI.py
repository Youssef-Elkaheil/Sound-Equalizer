from PyQt5 import QtCore
def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "Equalizer"))
    for i in range(10):
        self.label[i].setText(_translate("MainWindow", "{}/10".format(i+1)))
        
    self.tabWidget.setTabText(self.tabWidget.indexOf(
        self.tab), _translate("MainWindow", "Tab 1"))
    self.menuFile.setTitle(_translate("MainWindow", "File"))
    self.menuNavigation.setTitle(_translate("MainWindow", "Navigation"))
    self.menuScroll.setTitle(_translate("MainWindow", "Scroll"))
    self.menuZoom.setTitle(_translate("MainWindow", "Zoom"))
    self.menuSpeed.setTitle(_translate("MainWindow", "Speed"))
    self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
    self.menuTheme.setTitle(_translate("MainWindow", "Theme"))
    self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
    self.actionOpen.setText(_translate("MainWindow", "Open"))
    self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
    self.actionSave.setText(_translate("MainWindow", "Save"))
    self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
    self.actionTab.setText(_translate("MainWindow", "Tab"))
    self.actionTab.setToolTip(_translate("MainWindow", "Tab"))
    self.actionZoom_in.setText(_translate("MainWindow", "Zoom in"))
    self.actionZoom_in.setShortcut(_translate("MainWindow", "Ctrl+Up"))
    self.actionZoom_out.setText(_translate("MainWindow", "Zoom out"))
    self.actionZoom_out.setShortcut(_translate("MainWindow", "Ctrl+Down"))
    self.actionLeft.setText(_translate("MainWindow", "Left"))
    self.actionLeft.setShortcut(_translate("MainWindow", "Ctrl+Left"))
    self.actionRight.setText(_translate("MainWindow", "Right"))
    self.actionRight.setShortcut(_translate("MainWindow", "Ctrl+Right"))
    self.actionFaster.setText(_translate("MainWindow", "Faster"))
    self.actionFaster.setShortcut(
        _translate("MainWindow", "Ctrl+Shift+Right"))
    self.actionSlower.setText(_translate("MainWindow", "Slower"))
    self.actionSlower.setShortcut(
        _translate("MainWindow", "Ctrl+Shift+Left"))
    self.actionPlay.setText(_translate("MainWindow", "Play"))
    self.actionPlay.setShortcut(_translate("MainWindow", "Space"))
    self.actionSound.setText(_translate("MainWindow", "Sound"))
    self.actionSound.setShortcut(_translate("MainWindow", "Ctrl+S"))
    self.actionSpectrogram.setText(_translate("MainWindow", "Spectrogram"))
    self.actionSpectrogram.setShortcut(_translate("MainWindow", "Ctrl+F"))
    self.actionEqualizer.setText(_translate("MainWindow", "Equalizer"))
    self.actionEqualizer.setShortcut(_translate("MainWindow", "Ctrl+E"))
    self.actionExit.setText(_translate("MainWindow", "Exit"))
    self.actionClose_Tab.setText(_translate("MainWindow", "Close Tab"))
    self.actionClose_Tab.setShortcut(_translate("MainWindow", "Ctrl+F4"))
    self.actionGraph_theme.setText(_translate("MainWindow", "Graph"))
    self.actionSpectrogram_theme.setText(
        _translate("MainWindow", "Spectrogram"))
    # self.push