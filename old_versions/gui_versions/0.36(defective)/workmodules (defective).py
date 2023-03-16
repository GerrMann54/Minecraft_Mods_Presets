import os
import shutil
import getpass
import time

user = getpass.getuser()
mods_dir = f'C:/Users/{user}/AppData\Roaming/.minecraft/mods'
presets_dir = f'C:/Users/{user}/AppData/Roaming/.minecraft/mods_presets'
presetInfo_file = mods_dir + os.sep + 'preset_info.txt'
logFile = presets_dir + os.sep + 'Load_Log.txt'

def dateTime(): 
    return time.strftime('''%d.%m.%Y''') + ' ' + time.strftime('''%H:%M''')


class Preset:

    def __init__(self, name):
        self.name = name

    def load(self):
        pass


