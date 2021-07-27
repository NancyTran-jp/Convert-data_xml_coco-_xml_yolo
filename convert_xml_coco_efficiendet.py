import os
import glob
import xml.etree.ElementTree as ET
import xmltodict
import json
from xml.dom import minidom
from collections import OrderedDict
import argparse
import glob

# convert xml ->.json (efficientdet)

def generateVOC2Json(xmlFiles,output_file):
    attrDict = dict()
    attrDict["categories"]=[{"supercategory":"none","id":1,"name":"dust"},
                    {"supercategory":"none","id":2,"name":"hair"},
                    {"supercategory":"none","id":3,"name":"similar"},
                    {"supercategory":"none","id":4,"name":"b2"}
                  ]

    images = list()
    annotations = list()
    image_id = 0
    for file in xmlFiles:    
        image_id = image_id + 1      
        annotation_path=file
        image = dict()
        doc = xmltodict.parse(open(annotation_path).read(), force_list=('object'))
        image['file_name'] = str(doc['annotation']['filename'])
        image['height'] = int(doc['annotation']['size']['height'])
        image['width'] = int(doc['annotation']['size']['width'])
        image['id'] = image_id
        # print ("File Name: {} and image_id {}".format(file, image_id))
        images.append(image)
        id1 = 1
        if 'object' in doc['annotation']:
            for obj in doc['annotation']['object']:
                for value in attrDict["categories"]:
                    annotation = dict()          
                    if str(obj['name']) == value["name"]:
                        annotation["iscrowd"] = 0
                        annotation["image_id"] = image_id
                        x1 = int(obj["bndbox"]["xmin"])  - 1
                        y1 = int(obj["bndbox"]["ymin"]) - 1
                        x2 = int(obj["bndbox"]["xmax"]) - x1
                        y2 = int(obj["bndbox"]["ymax"]) - y1                         
                        annotation["bbox"] = [x1, y1, x2, y2]
                        annotation["area"] = float(x2 * y2)
                        annotation["category_id"] = value["id"]
                        annotation["ignore"] = 0
                        annotation["id"] = id1
                        annotation["segmentation"] = [[x1,y1,x1,(y1 + y2), (x1 + x2), (y1 + y2), (x1 + x2), y1]]
                        id1 +=1
                        annotations.append(annotation)

        else:
            print("File: {} doesn't have any object".format(file))

    attrDict["images"] = images    
    attrDict["annotations"] = annotations
    attrDict["type"] = "instances"

    jsonString = json.dumps(attrDict)
    with open(output_file, "w") as f:
        f.write(jsonString)

if __name__ =='__main__':
    parser = argparse.ArgumentParser(description='get_name')
    parser.add_argument('--rootDir', type=str, default="total/sample/ann_train", help='file')
    parser.add_argument('--output_file', type=str , default="total/sample/_annotations.coco_train.json", help='file')
    opt = parser.parse_args()
    xmlFiles = glob.glob(os.path.join(opt.rootDir,'*.xml'))
    generateVOC2Json(xmlFiles, opt.output_file)

