import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            '''
            if xml_file.split('/')[-1].find('DOTA') != -1:
              value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[1][0].text),
                     int(member[1][1].text),
                     int(member[1][2].text),
                     int(member[1][3].text)
                     )
            elif xml_file.split('/')[-1].find('RSD') != -1:
              value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            else:
            '''
            value = (root.find('filename').text.split('.')[0]+'.jpg',
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member.find('name').text,
                     int(member.find('bndbox').find('xmin').text),
                     int(member.find('bndbox').find('ymin').text),
                     int(member.find('bndbox').find('xmax').text),
                     int(member.find('bndbox').find('ymax').text)
                     )

            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    #image_path = os.path.join(os.getcwd(), 'annotations')
    #image_path = '/home/fuxianya/data/DOTA_COCO_greyscale/test/annotations'
    image_path = '/home/fuxianya/py-faster-rcnn/data/VOCdevkit2007/VOC2007_no_suv/Annotations'
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv('train_labels_bit_no_suv.csv', index=None)
    print('Successfully converted xml to csv.')


main()
