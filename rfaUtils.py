'''
Created on Oct 19, 2016

@author: alamingo
@author: team_7
'''
from datetime import datetime
import os, sys
name_dir = 'log_dir'

def getItemMessage(message_item):
    
    return {
        '-1': lambda message_item: getMessage("Unable to read local.properties file"),
        '-2': lambda message_item: getMessage("Unable to create dictionary"),
        '-3': lambda message_item: getMessage("Unable to find proporties for log_dir"),
        '-4': lambda message_item: getMessage("Can not read arguments"),
        '-5': lambda message_item: getMessage("Unable to create log file"),
        '-6': lambda message_item: getMessage("Cannot open 42.txt file for reading"),
        '-7': lambda message_item: getMessage("Cannot create dictionary"),        
           } 
            
def getMessage(message):
    
    print(message)
    sys.exit() 

def getLogdir(local_dict): 
    
    log_dir = local_dict.get('log_dir')
    if log_dir == None:
        return -3
    else:
        return log_dir      

def getLog(log_dir, name_script):
    """
    Creates 'logs' directory, if it doesn't exist,
    creates or opens a log file in 'logs' directory.
    """
    # assign a current working directory + '/logs' to log_dir variable (platform independent)
    #log_dir = os.path.join(os.getcwd(), "logs")
    # or --> script directory: log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    # or --> user directory: log_dir = os.path.join(os.path.expanduser("~"), "logs")

    try:
        # if logs directory(!) doesn't exist, create it
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        # open log file with prefix and timestamp (platform independent) in Append mode
        log = open(os.path.join(log_dir, name_script + '_' + getCurTime("%Y%m%d_%H-%M") + ".log"), "a")
        return log
    except (OSError, IOError):
        # return -1 in case of exception
        return -5


def qaPrint(log, message):
    """
    Prints 'timestamp + message' to console and writes it to the log file
    """
    # current date and time as string + message. example: [Oct 25 01:52:33.000001] TC1 - Passed
    log_message = getCurTime("[%b %d %H:%M:%S.%f]") + " " + message
    # prints log_message
    print log_message
    # writes message to a log file
    log.write(log_message + "\n")

def getArgs(list_comandstring):
    
    if len(list_comandstring)<2:
       getMessage('invalid parameters. Need more parameters. (rfarunner.py --testrun=42)')
    if len(list_comandstring)>3:
       getMessage('invalid parameters. Too many parameters. (rfarunner.py --testrun=42)')        
    try:
        param_name = list_comandstring[0]
        param_value = list_comandstring[1]
        list_args = list_comandstring[1].lower().split('=')                
        if len(list_args) == 2:
            if list_args[0] == "--testrun" :
                list_args[0]=list_args[0].replace('--','') 
                trid = int(list_args[1])
                if 0 <= trid <= 10000: 
                    return list_args                           
                else : getMessage('invalid parameters. Out of range.(--testrun=[0-10000] )')
        else: getMessage('invalid parameters.(rfarunner.py --testrun=42 )')       
    except IOError:
            return -4        
  
def getCurTime(date_time_format):
    """
    Returns current date_time as a string formatted according to date_time_format
    """
    date_time = datetime.now().strftime(date_time_format)
    return date_time

def getTestCases(test_id):
    
    list_keys = ['tcid','rest_URL','HTTP_method','HTTP_RC_desired','param_list']
    
    try:
        file_lines = getLinesFile(test_id+".txt")        
        if file_lines == -2:
            return -6
        else:
            id_dict = {}            
            len_keys = len(list_keys)
            for line in file_lines:
                list_values = line.strip().split('|')
                index_paramlist = list_keys.index('param_list')
                params = list_values[index_paramlist]                                                
                list_values[index_paramlist] = params.split(',')
                index_keys = 1
                dict_value = {}
                while index_keys  < len_keys:
                    dict_value[list_keys[index_keys]] = list_values[index_keys]
                    index_keys += 1                   
                id_dict.update({list_values[0]:dict_value})
            return id_dict        
    except IOError:             
        return -7                  
    

def getLinesFile(file_name):
    
    try:
        file_opened = open(file_name,"r")
        file_opened.seek(0)
        file_list = file_opened.read().splitlines() 
        file_opened.close()
        return file_list
    except IOError:
        return -2        


def getLocalEnv(file_name):
    
    try:
        properties_list=getLinesFile(file_name)
        if properties_list == -2:
            return -2
        else:    
            properties_dict = {}
            for line_file in properties_list:
                list_param = line_file.split('=')
                properties_dict.update({list_param[0]:list_param[1]})
            return properties_dict 
    except IOError:
        return -1                                    
       
        
      
