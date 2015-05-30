__author__ = 'nrot'

# -*- coding: utf-8 -*-

import time
import shutil
import FileClassPack
import ChoseModel


def main():

    Option = FileClassPack.OPtionsFileClass()
    Option.GetOptiions()
    if Option.Error != 'Done':
        OptionError = open('./OptionErrorLog.txt', 'w')
        OptionError.write(Option.Error)
        OptionError.close()
        return 'Option file error'
    PATH_TO_IMG_LIB = Option.PathToImage
    PathLog = Option.OptionPathLog
    #'~/.NewFonsLog'
    log = FileClassPack.DoubleLog(str(PathLog), 'log.txt')
    if log.Error == 'Open Error':
        return 'Open Error'

    while 1:
        print(log.path)
        img_internet = ChoseModel.Chose(log, Option)
        if img_internet == 'Error connect':
            time.sleep(Option.TimeToSleep)
            continue

        img_internet[0].raw.decode_content = True
        with open(PATH_TO_IMG_LIB + unicode(img_internet[1]), 'wb') as f:
            shutil.copyfileobj(img_internet[0].raw, f)
        # f.write(img_internet.content)
        f.close()

        log.write(text=str('All Done in this step! Wait ' + str(Option.TimeToSleep/60) + ' min.'))
        log.write(text='#====================================#\n')
        log.save()
        
        time.sleep(Option.TimeToSleep)

    del log

    return 0

if __name__ == "__main__":
    GLOBAL_ERROR = main()
    exit(GLOBAL_ERROR)
