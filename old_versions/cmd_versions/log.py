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


while True:
    
    try:
        with open(logFile, 'w+') as lf:

            lf.write(f'[{dateTime}] Loaded: 228 \n')
    except: print('Can`t save the log')

    input('Next time...')