import logging
from logging.handlers import BaseRotatingHandler
import re
import datetime
import os,json,sys,time
'''
按时间滚动日志

'''
class myhandler(BaseRotatingHandler):
    def __init__(self ,filename ,when ,encoding=None, delay=False):
        BaseRotatingHandler.__init__(self, filename, 'a', encoding, delay)
        self.when = when
        self.longtime = 0
        if self.when == 'S':
            self.suffix = "%Y-%m-%d_%H-%M-%S"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}(\.\w+)?$"

        elif self.when == 'M':
            self.suffix = "%Y-%m-%d_%H-%M"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}(\.\w+)?$"
            self.longtime = 60
        elif self.when == 'H':
            self.suffix = "%Y-%m-%d_%H"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}(\.\w+)?$"
            self.longtime = 60 * 60
        elif self.when == 'D' or self.when == 'MIDNIGHT':
            self.suffix = "%Y-%m-%d"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}(\.\w+)?$"
            self.longtime = 60 * 60 * 24
        else:
            raise ValueError("Invalid rollover interval specified: %s" % self.when)
        self.extMatch = re.compile(self.extMatch, re.ASCII)
        t = int(time.time())
        self.rolloverAt = self.computeRollover(t)
    def computeRollover(self, currentTime):
        datestruct = datetime.datetime.fromtimestamp(currentTime)
        datestruct1 = datestruct
        if self.when == 'S':
            datestruct1 = datestruct.replace(microsecond=0)
        elif self.when == 'M':
            datestruct1 = datestruct.replace(second=0, microsecond=0)
        elif self.when == 'H':
            datestruct1 = datestruct.replace(minute=0, second=0, microsecond=0)
        else:
            datestruct1 = datestruct.replace(hour=0, minute=0, second=0, microsecond=0)
        rollovertime = int(datestruct1.timestamp() ) +self.longtime
        return rollovertime
    def shouldRollover(self, record):
        """
        Determine if rollover should occur.
        record is not used, as we are just comparing times, but it is needed so
        the method signatures are the same
        """
        t = int(time.time())
        if t >= self.rolloverAt:
            return 1
        return 0
    def doRollover(self):
        """
        do a rollover; in this case, a date/time stamp is appended to the filename
        when the rollover happens.  However, you want the file to be named for the
        start of the interval, not the current time.  If there is a backup count,
        then we have to get a list of matching filenames, sort them and remove
        the one with the oldest suffix.
        """
        if self.stream:
            self.stream.close()
            self.stream = None
        # get the time that this sequence started at and make it a TimeTuple
        currentTime = int(time.time())
        dstNow = time.localtime(currentTime)[-1]
        # t = self.rolloverAt
        t = self.rolloverAt - self.longtime
        timeTuple = time.localtime(t)
        dstThen = timeTuple[-1]
        # if dstNow != dstThen:
        #    if dstNow:
        #        addend = 3600
        #    else:
        #        addend = -3600
        #    timeTuple = time.localtime(t + addend)


        dfn = self.rotation_filename(self.baseFilename + "." +
                                     time.strftime(self.suffix, timeTuple))
        if os.path.exists(dfn):
            os.remove(dfn)
        self.rotate(self.baseFilename, dfn)
        if not self.delay:
            self.stream = self._open()
        newRolloverAt = self.computeRollover(currentTime)
        self.rolloverAt = newRolloverAt
if __name__ == "__main__":
    myapp = logging.getLogger()
    myapp.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s: %(asctime)s %(filename)s %(message)s')
    filehandler = myhandler("lixiang.log", when='M')
    filehandler.setFormatter(formatter)
    myapp.addHandler(filehandler)
    import time
    while True:
        logging.info('info message')
        time.sleep(0.5)
