# Minecraft Mods Presets
# Version 0.11.1

# RUS
'''
Версия с исправлениями ошибок.

0.9: Вызов всех функций реализован через def.
0.9: Программа выполняется циклично. То есть за цикл её работы можно выполнять функции неограниченное количество раз.
0.10: Добавлена функция, записывающая данные о текущем пресете в файл.
0.11: Действия с пресетами записываются в лог.
0.11: Исправлен баг, из-за которого файл с информанией о пресете сохранялся в новый пресет, созданный функцией save.
0.11.1 Теперь программой предусмотрен неправильный ввод имён пресетов. Ошибки, приводящей к вылету программы, не происходит.
'''

# ENG
'''
Version with bug fixes.

0.9: Calling all functions is implemented via def.
0.9: The program is executed cyclically. That is, during the cycle of its operation, you can execute functions an unlimited number of times.
0.10: Added a function that writes data about the current preset to a file.
0.11: Actions with presets are recorded in the log.
0.11: Fixed a bug that caused the preset information file to be saved to a new preset created by the save function.
0.11.1 Now the program provides incorrect input of preset names. There is no error that causes the program to crash.
'''

import os
import shutil
import getpass
import time

user = getpass.getuser()
modsDir = 'C:\\Users\\{0}\\AppData\Roaming\\.minecraft\\mods'.format(user)
presetsDir = 'C:\\Users\\{0}\\AppData\Roaming\\.minecraft'.format(user) + os.sep + 'mods_presets'
presetInfo_file = modsDir + os.sep + 'preset_info.txt'
logFile = presetsDir + os.sep + 'Load_Log.txt'
dateTime = time.strftime('''%d.%m.%Y''') + ' ' + time.strftime('''%H:%M''')



def load(presetsDir, modsDir, current_modList, dateTime, logFile, presetInfo_file):

    try:
        print('-----------------------------------')
        target_preset = input('Select the preset: ')

        if not os.path.exists(presetsDir + os.sep + target_preset): 
            print('Incorrect name of preset')
            return
        print('-----------------------------------')


        print('Removing current mods...')
        for item in current_modList:

            if os.path.isfile(modsDir + os.sep + item):
                os.remove(modsDir + os.sep + item)
                print('Removed: ', item)
            
            elif os.path.isdir(modsDir + os.sep + item):
                shutil.rmtree(modsDir + os.sep + item)
                print('Removed: ', item)

        print('-----------------------------------')

        try:
            with open(presetInfo_file, 'w+') as infoFile:
                infoFile.write(f'Current preset: {target_preset} \n')
                infoFile.write('Date of load: ' + dateTime)
        except: print('Can`t create info file')

        current_preset = os.listdir(presetsDir + os.sep + target_preset)
        print('Loadig mods from presets\\{0}'.format(target_preset))

        for item in current_preset:

            if os.path.isfile(presetsDir + os.sep + target_preset + os.sep + item):
                shutil.copyfile(presetsDir + os.sep + target_preset + os.sep + item, modsDir + os.sep + item)

            elif os.path.isdir(presetsDir + os.sep + target_preset + os.sep + item):
                shutil.copytree(presetsDir + os.sep + target_preset + os.sep + item, modsDir + os.sep + item)

            print('Loaded: ', item)
    
    except:('Failed to load preset')

    try:
        with open(logFile, 'a') as lf:
            lf.write(f'[{dateTime}] Loaded: {target_preset} \n')
    except: print('Can`t save the log')

    input('Enter to continue...')



def save(presetsDir, modsDir, current_modList, dateTime, logFile):

    newPreset = input('Name of new preset: ')
    try:
        os.mkdir(presetsDir + os.sep + newPreset)
    except:
        print('Such a preset already exists')
        return

    print('Creating new preset...')
    for item in current_modList:

        if item == 'preset_info.txt': continue

        if os.path.isfile(modsDir + os.sep + item):
            shutil.copyfile(modsDir + os.sep + item, presetsDir + os.sep + newPreset + os.sep + item)

        elif os.path.isdir(modsDir + os.sep + item):
            shutil.copytree(modsDir + os.sep + item, presetsDir + os.sep + newPreset + os.sep + item)

        print('Saved: ', item)

    try:
        with open(logFile, 'a') as lf:
            lf.write(f'[{dateTime}] Saved: {newPreset} \n')
    except: print('Can`t save the log')
    
    input('Enter to continue...')



def delete(presetsDir, dateTime, logFile):

    run = True
    print('-----------------------------------')
    print('Removing presets')
    print('stop - exit')

    while run:
        
        delPreset = input('Preset to remove: ')

        if delPreset == 'stop':
            run = False
            continue
        
        if not os.path.exists(presetsDir + os.sep + delPreset):
            print('There is no such preset')
            continue

        shutil.rmtree(presetsDir + os.sep + delPreset)
        try:
            with open(logFile, 'a') as lf:
                lf.write(f'[{dateTime}] Deleted: {delPreset} \n')
        except: print('Can`t save the log')
        print(delPreset, 'removed')      



if __name__ == '__main__':

    while True:
        if not os.path.exists(presetsDir):

            os.mkdir(presetsDir)

            print('#########################')
            print('Presets directory created')
            print('#########################')
            print('')

        if not os.path.exists(logFile):
            f = open(logFile, 'w+')
            f.close() 


        current_modList = os.listdir(modsDir)
        print('Current mods:')

        for item in current_modList:
            print('>>>: ', item)


        presetsList = os.listdir(presetsDir)
        print('')
        print('Available presets:')

        for dirInList in presetsList:

            if os.path.isdir(presetsDir + os.sep + dirInList):
                print('>>>: ', dirInList)

        print()
        try:
            with open(presetInfo_file, 'r') as infoFile:
                for line in infoFile: 
                    print(line)
        except: print('Can`t read info about current preset')


        print('')
        print('Select any action:')
        print('load - load available preset')
        print('save - save current preset')
        print('del - remove any presets')
        print('stop - exit')

        action = input()
        if action   == 'load': load(presetsDir, modsDir, current_modList, dateTime, logFile, presetInfo_file)
        elif action == 'save': save(presetsDir, modsDir, current_modList, dateTime, logFile)
        elif action ==  'del': delete(presetsDir, dateTime, logFile)
        elif action == 'stop': break
        else: print('Incorrect command')