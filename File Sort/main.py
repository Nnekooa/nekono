#!/usr/bin/python3
import os
import os.path
import shutil

DirPath=input('Enter the directory to be organized:')
try:
    os.chdir(DirPath)
except (OSError,TypeError):
    print('WRONG PATH!')
    raise SystemExit(1)
Suffixes=[]
for root, dirs, files in os.walk("."):
    for name in files:
        if name.count('.'):        
            suffix=name.split('.')[-1]
            if not Suffixes.count(suffix):
                Suffixes.append(suffix)
                os.mkdir(str('_'+suffix.upper()+'_'))
                shutil.copy2(os.path.join(root,name),str('_'+suffix.upper()+'_'))
            else:
                shutil.copy2(os.path.join(root,name),str('_'+suffix.upper()+'_'))
        else:
            if not Suffixes.count('.'):
                Suffixes.append('.')
                os.mkdir('_UNKNOWN_')
                shutil.copy2(os.path.join(root,name),'_UNKNOWN_')
            else:
                shutil.copy2(os.path.join(root,name),'_UNKNOWN_')
        