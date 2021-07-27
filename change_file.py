import os
import glob
import shutil
import argparse

# copy file image and .xml,.txt ->foldel
def change_file_train(folder_train):
    source_train=glob.glob(folder_train + '*.jpeg')
    source_train_1=glob.glob(folder_train + '*.xml')
    for filename in source_train:
        shutil.copy(filename, 'total/sample/new_data/train')
        # folder_main
        shutil.copy(filename, 'total/sample/train/images') 
    for filename in source_train_1:
        # folder_main
        shutil.copy(filename, 'total/sample/train/labels')

        shutil.copy(filename, 'total/sample/ann_train')
        
def change_file_valid(folder_valid):
    source_train=glob.glob(folder_valid + '*.jpeg')
    source_train_1=glob.glob(folder_valid + '*.xml')
    for filename in source_train:
        shutil.copy(filename, 'total/sample/new_data/valid')
        # folder_main
        shutil.copy(filename, 'total/sample/valid/images')
    for filename in source_train_1:
        # folder_main
        shutil.copy(filename, 'total/sample/valid/labels')

        shutil.copy(filename, 'total/sample/ann_valid')        

if __name__ =='__main__':
    parser = argparse.ArgumentParser(description='get_name')
    parser.add_argument('--folder_train', type=str, default='total/train/', help='file')
    parser.add_argument('--folder_valid', type=str , default='total/valid/', help='file')
    opt = parser.parse_args()
    change_file_train(opt.folder_train)
    change_file_valid(opt.folder_valid)