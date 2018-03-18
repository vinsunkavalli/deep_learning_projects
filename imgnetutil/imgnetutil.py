#!/usr/bin/env python

"""
Uses ImageNet urls provided on download page to download images
Created by Vineet Sunkavalli
"""

from urllib import urlretrieve

class ImageNetInfo(object):
"""This class is aimed to simplify the process of downloading images from ImageNet.

    This class is used to store and download Image Net Information derived from two sources: text files and JSON. 
    It is expected that these files follow the general format used. See the README for more detail.

    Attributes:
        wnids: A dictionary containing the Word Net Indexes and their corresponding image numbers
        classes: A dictionary containing the Word Net Indexes and their corresponding classes
        urls: A dictionary containing the Image titles and their corresponding urls
"""
    def __init__(self):
        """Initializes ImageNetInfo object.
        """
        self.wnids = {}
        self.classes = {}
        self.urls = {}

    def load_txt(self, file_name, num_classes=10, num_images=10):
        txt = open(file_name, 'r')
        txt_lines = txt.readlines()

        class_num = 0
        i = 0

        for line in txt_lines:
            line_info = line.split()
            wnid, image_num = line_info[0].split('_')

            if wnid not in self.wnids.keys():
                class_num += 1
                if class_num > num_classes:
                    break
                i=0

            if i < num_images:
                i+=1
                if wnid not in self.wnids.keys():
                    self.wnids[wnid] = [image_num]
                else:
                    self.wnids[wnid].append(image_num)             
                self.urls[line_info[0]] = line_info[1]

    def getWnids(self):
        return self.wnids

    def getUrls(self):
        return self.urls

    def mapWnids_txt(self, file_name):
        txt = open(file_name, 'r')
        txt_lines = txt.readlines()

        for line in txt_lines:
            line_info = line.split()
            wnid = line_info[1]
            classid = line_info[0]

            if wnid in self.wnids.keys():
                self.classes[wnid] = classid

    def getClasses(self):
        return self.classes

    def downloadImages_txt(self):
        for wnid in self.wnids.keys():
            for i in range(len(self.wnids[wnid])):
                try:
                    classid = self.classes[wnid]
                except KeyError:
                    classid = wnid
                try:
                    urlretrieve(self.urls[wnid+"_"+self.wnids[wnid][i]], wnid+"_"+str(i+1)+'.jpg')
                except:
                    print ':('
