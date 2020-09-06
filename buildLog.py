# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 09:36:21 2020

@author: agrabdur7137
"""
import logging

class Log:
    """Class for create Log Process (Global Running)
    
    Use:
        from buildlog import Log
        
        logger = Log().createLog() 
    
    parameter use:
        name_logger     name process of log
        file_logger     name file of log
    """
    
    def __init__(self, name_logger, file_logger, PATH_LOG):
        self.name_logger = name_logger
        self.file_logger = file_logger
        self.path_log = PATH_LOG
        
    def createLog(self):
        logger = logging.getLogger("{}".format(self.name_logger))
        logging.basicConfig(level=logging.INFO)
        f_handler = logging.FileHandler("{}/{}.log".format(self.path_log, self.file_logger))
        f_handler.setLevel(logging.DEBUG)
        f_format = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        
        return logger
