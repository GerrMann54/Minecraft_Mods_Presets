# Minecraft Mods Presets
# Version 0.7

# RUS
'''
Стандартная версия программы.

0.7: Вызов всех функций реализован через if / else.
0.7: Программа выполняется не циклично. То есть за весь цикл её работы выполняется только одна функция.
'''

# ENG
'''
The standard version of the program.

0.7: Calling all functions is implemented via if/else.
0.7: The program executed non-cyclically. That is, for the entire cycle of its operation, only one function is performed.
'''

import os
import shutil
import getpass

user = getpass.getuser()
modsDir = 'C:\\Users\\{0}\\AppData\Roaming\\.minecraft\\mods'.format(user)
presetsDir = 'C:\\Users\\{0}\\AppData\Roaming\\.minecraft'.format(user) + os.sep + 'mods_presets'


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
print('Enter - exit')

action = input()


if action == 'load':

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



elif action == 'save':

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



elif action == 'del':

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