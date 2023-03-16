import os
import shutil
import getpass
import time

user = getpass.getuser()
modsDir = f'C:/Users/{user}/AppData\Roaming/.minecraft/mods'
presetsDir = f'C:/Users/{user}/AppData\Roaming/.minecraft/mods_presets'
presetInfo_file = modsDir + os.sep + 'preset_info.txt'
logFile = presetsDir + os.sep + 'Load_Log.txt'

def dateTime(): 
    return time.strftime('''%d.%m.%Y ''') + time.strftime('''%H:%M''')

def log(action, name):
    try:
        with open(logFile, 'a') as lf:

            if action == 'load': lf.write(f'[{dateTime()}] Loaded: {name} \n')
            elif action == 'save': lf.write(f'[{dateTime()}] Saved: {name} \n')
            elif action == 'rem': lf.write(f'[{dateTime()}] Removed: {name} \n')
            else: lf.write(f'[{dateTime()}] {action}: {name} \n')
            
    except: 
        print('Can`t save the log')
        return



def load(target_preset):

    try:

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
                infoFile.write('Date of load: ' + dateTime())
        except: print('Can`t create info file')

        current_preset = os.listdir(presetsDir + os.sep + target_preset)
        print('Loadig mods from presets\\{0}'.format(target_preset))

        for item in current_preset:

            if os.path.isfile(presetsDir + os.sep + target_preset + os.sep + item):
                shutil.copyfile(presetsDir + os.sep + target_preset + os.sep + item, modsDir + os.sep + item)

            elif os.path.isdir(presetsDir + os.sep + target_preset + os.sep + item):
                shutil.copytree(presetsDir + os.sep + target_preset + os.sep + item, modsDir + os.sep + item)

            print('Loaded: ', item)
    
    except:
        print('Failed to load preset')
        return

    log('load', target_preset)



def save(newPreset):

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

    log('save', newPreset)



def remove(delPreset):

    shutil.rmtree(presetsDir + os.sep + delPreset)
    log('rem', delPreset)
    print(delPreset, 'removed') 

def delete(delPreset):

    print('Removing presets')
    print('stop - exit')

    if delPreset == 'stop':
        return False
    
    if not os.path.exists(presetsDir + os.sep + delPreset):
        print('There is no such preset')
        return True

    remove(delPreset)   

    return True   



def checkFiles():

    if not os.path.exists(presetsDir):

        os.mkdir(presetsDir)

        print('#########################')
        print('Presets directory created')
        print('#########################')
        print('')

    if not os.path.exists(logFile):
        f = open(logFile, 'w+')
        f.close() 



def get_modList():

    current_modList = os.listdir(modsDir)
    print('Current mods:')

    for item in current_modList:
        print('>>>: ', item)

    return current_modList



def get_presetsList():

    presetsList = os.listdir(presetsDir)
    listToRemove = []
    print('')
    print('Available presets:')

    for item in presetsList:

        if os.path.isdir(presetsDir + os.sep + item):
            print('>>>: ', item)
        else: listToRemove.append(item)

    if len(listToRemove) > 0:
        for item in listToRemove:
            presetsList.remove(item)

    return presetsList



if __name__ == '__main__':

    while True:
        
        checkFiles()
        current_modList = get_modList()
        presetsList = get_presetsList()
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

        if action   == 'load': 
            print('-----------------------------------')
            target_preset = input('Select the preset: ')
            load(target_preset)

        elif action == 'save': 
            newPreset = input('Name of new preset: ')
            save(newPreset)

        elif action ==  'del':
            run = True
            while run:
                delPreset = input('Preset to remove: ')
                run = delete(delPreset)

        elif action == 'stop': break
        else: print('Incorrect command')