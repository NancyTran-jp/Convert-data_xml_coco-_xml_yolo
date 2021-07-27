from pathlib import Path
import glob
import os
import cv2
import shutil
import argparse
# deleted images not have file .xml, .txt
def secede(file,file_save)
    name_path1 = []
    path1 = glob.glob(file +'*.xml')
    path2 = glob.glob(file +'*.jpeg')
    for i in path1:
        name = Path(i).stem
        name_path1.append(name)
        shutil.copy(i, file_save)
    for i in path2:  
        name = Path(i).stem  
        if name in name_path1:
            shutil.copy(i,file_save)
if __name__ =='__main__':
    parser = argparse.ArgumentParser(description='get_name')
    parser.add_argument('--file', type=str, default='dust/', help='file')
    parser.add_argument('--file_save', type=str , default='dust_secede', help='file')
    opt = parser.parse_args()
    secede(opt.file, opt.file_save)
