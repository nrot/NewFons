__author__ = 'nrot'

import random
import sys
import os
sys.path.insert(2, os.getcwd() + '\\Sites')
import Wall
import GoodFon
import BadFon
import Zastavki

def Chose(LogFile, Options):
        site = random.randint(1, 4)
        if site == 1:
            def_img = GoodFon.GoodFon(LogFile, Options)
            if def_img == 'Error connect':
                LogFile.write(aType='connect', text='wall.alphacoders.com', aTime=int(Options.TimeToSleep/60))
                return 'Error connect'
        elif site == 2:
            def_img = Wall.Wall(LogFile, Options)
            if def_img == 'Error connect':
                LogFile.write(aType='connect', text='www.goodfon.ru', aTime=int(Options.TimeToSleep/60))
                return 'Error connect'
        elif site == 3:
            def_img = BadFon.BadFon(LogFile, Options)
            if def_img == 'Error connect':
                LogFile.write(aType='connect', text='www.badfon.ru', aTime=int(Options.TimeToSleep/60))
                return 'Error connect'
        elif site == 4:
            def_img = Zastavki.Zastavki(LogFile, Options)
            if def_img == 'Error connect':
                LogFile.write(aType='connect', text='www.zastavki.com', aTime=int(Options.TimeToSleep/60))
                return 'Error connect'
        return def_img
