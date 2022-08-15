import os
import shutil
import getpass
import time

user = getpass.getuser()
modsDir = 'C:\\Users\\{0}\\AppData\Roaming\\.minecraft\\mods'.format(user)
presetsDir = 'C:\\Users\\{0}\\AppData\Roaming\\.minecraft'.format(user) + os.sep + 'mods_presets'
presetInfo_file = modsDir + os.sep + 'preset_info.txt'
logFile = presetsDir + os.sep + 'Load_Log.txt'

def dateTime(): 
    return time.strftime('''%d.%m.%Y''') + ' ' + time.strftime('''%H:%M''')



def load(target_preset, presetsDir, modsDir, current_modList, logFile, presetInfo_file):

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
    
    except:('Failed to load preset')

    try:
        with open(logFile, 'a') as lf:
            lf.write(f'[{dateTime()}] Loaded: {target_preset} \n')
    except: print('Can`t save the log')



def save(newPreset, presetsDir, modsDir, current_modList, logFile):

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
            lf.write(f'[{dateTime()}] Saved: {newPreset} \n')
    except: print('Can`t save the log')



def remove(delPreset, presetsDir, logFile):

    shutil.rmtree(presetsDir + os.sep + delPreset)
    try:
        with open(logFile, 'a') as lf:
            lf.write(f'[{dateTime()}] Deleted: {delPreset} \n')
    except: print('Can`t save the log')
    print(delPreset, 'removed') 

def delete(delPreset, presetsDir, logFile):

    print('Removing presets')
    print('stop - exit')

    if delPreset == 'stop':
        return False
    
    if not os.path.exists(presetsDir + os.sep + delPreset):
        print('There is no such preset')
        return True

    remove(delPreset, presetsDir, logFile)   

    return True   



def checkFiles(presetsDir, logFile):

    if not os.path.exists(presetsDir):

        os.mkdir(presetsDir)

        print('#########################')
        print('Presets directory created')
        print('#########################')
        print('')

    if not os.path.exists(logFile):
        f = open(logFile, 'w+')
        f.close() 



def get_modList(modsDir):

    current_modList = os.listdir(modsDir)
    print('Current mods:')

    for item in current_modList:
        print('>>>: ', item)

    return current_modList



def get_presetsList(presetsDir):

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
        
        checkFiles(presetsDir, logFile)
        current_modList = get_modList(modsDir)
        presetsList = get_presetsList(presetsDir)
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
            load(target_preset, presetsDir, modsDir, current_modList, logFile, presetInfo_file)

        elif action == 'save': 
            newPreset = input('Name of new preset: ')
            save(newPreset, presetsDir, modsDir, current_modList, logFile)

        elif action ==  'del':
            run = True
            while run:
                delPreset = input('Preset to remove: ')
                run = delete(delPreset, presetsDir, logFile)

        elif action == 'stop': break
        else: print('Incorrect command')