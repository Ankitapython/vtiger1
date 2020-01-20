import inspect
import logging #generates log reports

def customLogger(logLevel=logging.DEBUG):
    loggerName= inspect.stack()[1][3]
    logger=logging.getLogger(loggerName)#by default, log all messages
    logger.setLevel(logging.DEBUG)

    filehandler= logging.FileHandler("C:\\Users\\ankita\\PycharmProjects\\vtiger1\\resources\\reports\\log_reports\\auotmation.log",mode='a')
    filehandler.setLevel(logLevel)

    formatter=logging.Formatter('%(asctime)s -%(name)s -%(levelname)s: %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p')

    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    return logger