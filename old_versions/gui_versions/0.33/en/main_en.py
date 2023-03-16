# Minecraft Mods Presets
# Version 1.0

# RUS
'''
Версия с графическим интерфейсом.

0.9: Вызов всех функций реализован через def.
0.9: Программа выполняется циклично. То есть за цикл её работы можно выполнять функции неограниченное количество раз.
0.10: Добавлена функция, записывающая данные о текущем пресете в файл.
0.11: Действия с пресетами записываются в лог.
0.11: Исправлен баг, из-за которого файл с информанией о пресете сохранялся в новый пресет, созданный функцией save.
0.11.1 Теперь программой предусмотрен неправильный ввод имён пресетов. Ошибки, приводящей к вылету программы, не происходит.
0.33 Выведение списков реализовано через def
0.33 Добавлен графический интерфейс.
'''

# ENG
'''
Version with GUI.

0.9: Calling all functions is implemented via def.
0.9: The program is executed cyclically. That is, during the cycle of its operation, you can execute functions an unlimited number of times.
0.10: Added a function that writes data about the current preset to a file.
0.11: Actions with presets are recorded in the log.
0.11: Fixed a bug that caused the preset information file to be saved to a new preset created by the save function.
0.11.1 Now the program provides incorrect input of preset names. There is no error that causes the program to crash.
0.33 Added GUI.
'''

import os
import sys 
from PyQt6 import QtWidgets

import mmp_en
import main_functions as mf     # mf значит мишк фреде

mf.checkFiles(mf.presetsDir, mf.logFile)

class App(QtWidgets.QMainWindow, mmp_en.Ui_MainWindow):

    def get_presetsList(self):
        self.listWidget.clear()
        presetsList = mf.get_presetsList(mf.presetsDir)

        for item in presetsList:
            self.listWidget.addItem(item)
        return presetsList

    def get_modList(self):
        self.listWidget_3.clear()
        current_modList = mf.get_modList(mf.modsDir)
        
        for item in current_modList:
            self.listWidget_3.addItem(item)
        return current_modList

    def show_preset(self, i):
        global selected_preset
        try:
            selected_preset = i.text()
            str(selected_preset)

            self.listWidget_2.clear()
            modsInPreset_list = os.listdir(mf.presetsDir + os.sep + i.text())

            for item in modsInPreset_list:
                self.listWidget_2.addItem(item)
            return modsInPreset_list
        except: return
    
    def load(self):
        try:
            mf.load(selected_preset, mf.presetsDir, mf.modsDir, mf.get_modList(mf.modsDir), mf.logFile, mf.presetInfo_file)
            self.get_modList()
        except: return

    def remove(self):
        if self.checkBox.isChecked():
            try:
                mf.remove(selected_preset, mf.presetsDir, mf.logFile)
                self.listWidget_2.clear()
            except: return
        self.get_presetsList()

    def save(self):
        newPreset = self.lineEdit.text()
        try:
            mf.save(newPreset, mf.presetsDir, mf.modsDir, mf.get_modList(mf.modsDir), mf.logFile)
        except: return
        self.get_presetsList()
 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.get_presetsList()
        self.get_modList()
        self.pushButton.clicked.connect(self.load)
        self.pushButton_2.clicked.connect(self.remove)
        self.pushButton_3.clicked.connect(self.save)
        self.listWidget.currentItemChanged.connect(self.show_preset)
        self.checkBox.setChecked(False)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App() 
    window.show()  
    app.exec() 

if __name__ == '__main__': main()