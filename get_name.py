# import os
# base = os.path.basename('data\good\DJI_0115.JPG')
# name = os.path.splitext(base)[0]
# print(name)

from pathlib import Path
import glob
import os
import cv2
import argparse

# get name ->file .txt
def get_name(folder_train_labels,folder_valid_labels):
    name_path1 = []
    name_path2 = []
    path1 = glob.glob(folder_train_labels + '*.xml')
    path2 = glob.glob(folder_valid_labels + '*.xml')
    for i in path1:
        name = Path(i).stem
        name_path1.append(name)
    f = open(r"total/sample/data_ids/train.txt", "w+")
    for i in name_path1:
        f.writelines(i+"\n")
    f.close()

    for i in path2:
        name = Path(i).stem
        name_path2.append(name)
    g = open(r"total/sample/data_ids/valid.txt", "w+")
    for i in name_path2:
        g.writelines(i+"\n")
    g.close()    
if __name__ =='__main__':
    parser = argparse.ArgumentParser(description='get_name')
    parser.add_argument('--folder_train_labels', type=str, default='total/sample/train/labels/'  , help='file')
    parser.add_argument('--folder_valid_labels', type=str , default= 'total/sample/valid/labels/', help='file')
    opt = parser.parse_args()
    get_name(opt.folder_train_labels , opt.folder_valid_labels)
  
