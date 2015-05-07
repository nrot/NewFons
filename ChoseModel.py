__author__ = 'nrot'

import random
import Sites.BadFon
import Sites.Wall
import Sites.Zastavki
import Sites.GoodFon


def Chose(LogFile, Options):
        site = random.randint(1, 4)
        if site == 1:
            def_img = Sites.GoodFon.GoodFon(LogFile, Options)
            if def_img == 'Error connect':
                LogFile.write(aType='connect', text='wall.alphacoders.com', time=int(Options.TimeToSleep/60))
                return 'Error connect'
        elif site == 2:
            def_img = Sites.Wall.Wall(LogFile, Options)
            if def_img == 'Error connect':
                LogFile.write(aType='connect', text='www.goodfon.ru', time=int(Options.TimeToSleep/60))
                return 'Error connect'
        elif site == 3:
            def_img = Sites.BadFon.BadFon(LogFile, Options)
            if def_img == 'Error connect':
                LogFile.write(aType='connect', text='www.badfon.ru', time=int(Options.TimeToSleep/60))
                return 'Error connect'
        elif site == 4:
            def_img = Sites.Zastavki.Zastavki(LogFile, Options)
            if def_img == 'Error connect':
                LogFile.write(aType='connect', text='www.zastavki.com', time=int(Options.TimeToSleep/60))
                return 'Error connect'
        return def_img
