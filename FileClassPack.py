﻿__author__ = 'nrot'

# -*- coding: utf-8 -*-

import os
import time
import shutil
import xml.etree.ElementTree as XMLElementTree
import glob
from lxml import etree


class DoubleLog(object):
    def __init__(self, inpath, namefile):
        self.path = os.path.expanduser(inpath)
        try:
            if (os.path.getsize(self.path + namefile) > 10240):
                os.remove(self.path + namefile)
        except:
            if not os.path.exists(self.path):
                os.makedirs(self.path)
        try:
            self.objlogfile = open(str(self.path + '\\' + namefile), 'a')
            self.objlogfile.write(time.ctime(time.time()))
            self.objlogfile.write('\n')
            self.Error = 'Done'
        except:
            print('Can`t open ', self.path, namefile)
            #self.CommandToKdeError = 'kdialog --error \'Can`t open file ' + self.path + namefile + ' \n Program will close. \' --title \'New Fons\''
            #print(self.CommandToKdeError)
            #os.system(self.CommandToKdeError)
            self.Error = 'Open Error'

    def __del__(self):
        self.objlogfile.close()

    def write(self, aType='simple', text='nothing', aTime=10):
        if aType == 'connect':
            print(str('Can`t connect to ' + str(text) + "\n wait " + str(aTime) + ' min and i try connect again.\n'))
            self.objlogfile.write('Can`t connect to ' + str(text) + '\n' + 'wait ' + str(aTime) + ' min and i try connect again.\n')
            self.objlogfile.write(
                '#######################################################################################################\n')
            self.objlogfile.write('\n')
        elif aType == 'simple':
            print(text)
            self.objlogfile.write(text)
            self.objlogfile.write('\n')
        return 'Done'
    
    def save(self):
        self.objlogfile.flush()


class OptionsFileClass(object):
    def __init__(self):
        self.path = os.path.realpath('./') + '\\'
        self.namefile = 'Option.xml'
        self.originpath = os.path.realpath("./OriginFile.xml")
        if os.path.exists(self.path) == 0:
            os.makedirs(self.path)
        try:
            self.originfile = open(self.originpath, 'r')
        except:
            print(str('Can`t open ' + self.path + self.namefile))
            #self.CommandToKdeError = 'kdialog --error \'Can`t open file ' + self.originpath + '\nProgram will close. \' --title \'New Fons\''
            #print(self.CommandToKdeError)
            #os.system(self.CommandToKdeError)
            self.Error = 'Open Error'
        try:
            if os.path.exists(self.path + self.namefile):
                self.optionsfile = open(str(self.path + self.namefile), 'r')
            else:
                shutil.copy(self.originpath, self.path + self.namefile)
            self.Error = 'Done'
        except:
            print(str('Can`t open ' + self.path + self.namefile))
            #self.CommandToKdeError = 'kdialog --error \'Can`t open file ' + self.path + self.namefile + '\nProgram will close. \' --title \'New Fons\''
            #print(self.CommandToKdeError)
            #os.system(self.CommandToKdeError)
            self.Error = 'Open Error'
        print(self.path + self.namefile)
        self.parser = etree.XMLParser(recover=True)
        try:
            self.parsedoption = XMLElementTree.parse(self.namefile, parser=self.parser)
        except:
            self.parsedoption = XMLElementTree.parse(self.path + self.namefile, parser=self.parser)
        self.parsedorigin = XMLElementTree.parse(self.originpath, parser=self.parser)

        self.OriginVersion = self.parsedorigin.findall('Version')[0].text
        self.OptionVersion = self.parsedoption.findall('Version')[0].text
        if self.OriginVersion != self.OptionVersion:
            self.Warning = 'Different version'

    def __del__(self):
        try:
            self.optionsfile.close()
            self.originfile.close()
        except:
            self.Error = 'Bag close'

    def GetOptiions(self):
        try:
            self.PathToImage = os.path.realpath(os.path.expanduser(self.parsedoption.findall('PathToImage')[0].text)) + '\\'
            #self.PathToImage = unicodedata.normalize('NFKD', self.PathToImage).encode('ascii', 'ignore')
            if os.path.exists(self.PathToImage) != True:
                os.makedirs(self.PathToImage)
            if self.OriginVersion != self.OptionVersion:
                self.Version = 'Different version.'
            else:
                self.Version = self.OptionVersion
            self.OptionPathLog = os.path.realpath(os.path.expanduser(self.parsedoption.findall('PathLog')[0].text))
            self.OriginPathLog = os.path.realpath(os.path.expanduser(self.parsedorigin.findall('PathLog')[0].text))
            self.TimeToSleep = int(self.parsedoption.findall('time')[0].text)
            self.AmountImageSave = int(self.parsedoption.findall('amountImageSave')[0].text)
            self.ImageAmount = int(self.parsedoption.findall('amountImage')[0].text)
            self.MaxAmountImage = int(self.parsedoption.findall('maxImage')[0].text)
        except:
            self.Error = 'second parsed error'
    def EditOptions(self, Setting, NewValue):
        if self.parsedoption.findall(str(Setting)) == []:
          return 'Not Have this Setting'
        else:
            #self.cachestr = unicodedata.normalize('NFKD', str(self.AmountImageSave)).encode('ascii', 'ignore')
            cachestr = self.parsedoption.findall(str(Setting))[0]
            cachestr.text = str(NewValue)
            self.GetOptiions()
            return True
    def FindImage(self):
        os.chdir(self.PathToImage)
        jpgAmount = len(glob.glob('*.jpg'))
        jpgAmount += len(glob.glob('*.jpeg'))
        pngAmount = len(glob.glob('*.png'))
        self.EditOptions('amountImage', jpgAmount + pngAmount)
        return jpgAmount + pngAmount

    def OldestImageDelete(self, amount=1):
        os.chdir(self.PathToImage)
        imageFiles = glob.glob('*.jpg')
        imageFiles += glob.glob('*.jpeg')
        imageFiles += glob.glob('*.png')
        imageCreateTime = []
        DeleteName = []
        for i in imageFiles:
            imageCreateTime.append(os.path.getctime(i))
        for i in range(0, amount):
            IndexDel = imageCreateTime.index(min(imageCreateTime))
            DeleteName.append(imageFiles[IndexDel])
            os.remove(imageFiles[IndexDel])
        return DeleteName