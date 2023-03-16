# Minecraft Mods Presets
# Version 0.9

# RUS
'''
Обновлённая версия программы.

0.9: Вызов всех функций реализован через def.
0.9: Программа выполняется циклично. То есть за цикл её работы можно выполнять функции неограниченное количество раз.
'''

# ENG
'''
Updated version of the program.

0.9: Calling all functions is implemented via def.
0.9: The program is executed cyclically. That is, during the cycle of its operation, you can execute functions an unlimited number of times.
'''

import os
import shutil
import getpass

user = getpass.getuser()
modsDir = 'C:\\Users\\{0}\\AppData\Roaming\\.minecraft\\mods'.format(user)
presetsDir = 'C:\\Users\\{0}\\AppData\Roaming\\.minecraft'.format(user) + os.sep + 'mods_presets'
presetInfo_file = modsDir + os.sep + 'preset_info.txt'



def load(presetsDir, modsDir, current_modList):

    print('-----------------------------------')
    target_preset = input('Select the preset: ')
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


    current_preset = os.listdir(presetsDir + os.sep + target_preset)
    print('Loadig mods from presets\\{0}'.format(target_preset))

    for item in current_preset:

        if os.path.isfile(presetsDir + os.sep + target_preset + os.sep + item):
            shutil.copyfile(presetsDir + os.sep + target_preset + os.sep + item, modsDir + os.sep + item)

        elif os.path.isdir(presetsDir + os.sep + target_preset + os.sep + item):
            shutil.copytree(presetsDir + os.sep + target_preset + os.sep + item, modsDir + os.sep + item)

        print('Loaded: ', item)

    input('Enter to escape...')



def save(presetsDir, modsDir, current_modList):

    newPreset = input('Name of new preset: ')
    os.mkdir(presetsDir + os.sep + newPreset)

    print('Creating new preset...')
    for item in current_modList:

        if os.path.isfile(modsDir + os.sep + item):
            shutil.copyfile(modsDir + os.sep + item, presetsDir + os.sep + newPreset + os.sep + item)

        elif os.path.isdir(modsDir + os.sep + item):
            shutil.copytree(modsDir + os.sep + item, presetsDir + os.sep + newPreset + os.sep + item)

        print('Saved: ', item)
    
    input('Enter to escape...')



def delete(presetsDir):

    run = True
    print('-----------------------------------')
    print('Removing presets')
    print('stop - exit')

    while run:
        
        delPreset = input('Preset to remove: ')

        if delPreset == 'stop':
            run = False
            continue

        shutil.rmtree(presetsDir + os.sep + delPreset)
        print(delPreset, 'removed')      



if __name__ == '__main__':

    while True:
        if not os.path.exists(presetsDir):

            os.mkdir(presetsDir)

            print('#########################')
            print('Presets directory created')
            print('#########################')
            print('')


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


        print('')
        print('Select any action:')
        print('load - load available preset')
        print('save - save current preset')
        print('del - remove any presets')
        print('stop - exit')

        action = input()
        if action   == 'load': load(presetsDir, modsDir, current_modList)
        elif action == 'save': save(presetsDir, modsDir, current_modList)
        elif action ==  'del': delete(presetsDir)
        elif action == 'stop': break