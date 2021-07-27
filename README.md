****voc2coco.py****
<!-- change your folder -->
!python voc2coco.py --ann_dir [total/sample/ann_train] --ann_ids [total/sample/data_ids/train.txt] --labels [total/sample/labels.txt] --output [total/sample/output_train.json] --ext xml
<!-- change your folder -->
!python voc2coco.py --ann_dir [total/sample/ann_valid]  --ann_ids [total/sample/data_ids/valid.txt] --labels [total/sample/labels.txt] --output [total/sample/output_valid.json] --ext xml

****convert_xml_yolo.py****
<!-- change your folder , your classes-->
dirs = ['total/train', 'total/valid']
classes = ['dust', 'hair', 'similar', 'b2']

****convert_xml_coco_efficiendet.py****
<!-- change your folder-->
!python convert_xml_coco_efficiendet.py --rootDir ["total/sample/ann_train"] --output_file ["total/sample/_annotations.coco_train.json"]
