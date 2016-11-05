'''
Created on Oct 19, 2016


@author: alamingo
@author: team_7
'''
from rfaUtils import getItemMessage, getMessage,getLogdir,getArgs,getLog,qaPrint,getTestCases,getLocalEnv

import sys
name_env_file = "local.properties"
# get dictionary environment variables                 
local_env = getLocalEnv(name_env_file)
<<<<<<< HEAD
# check for mistakes 
=======
>>>>>>> 5f1f43785bb38d10e0a62c86f2fc95166741c013
getItemMessage(local_env)
# get Log_dir from dictionary        
log_dir = getLogdir(local_env)
# check for mistakes
getItemMessage(log_dir)
# get arguments from command line
list_args = getArgs(sys.argv)
# check for mistakes 
getItemMessage(list_args)
<<<<<<< HEAD
# get log and list of arguments,list_args[2] is filename   
log = getLog(log_dir,list_args[2])
# check for mistakes
=======
  
log = getLog(log_dir,list_args[2])
>>>>>>> 5f1f43785bb38d10e0a62c86f2fc95166741c013
getItemMessage(log)
 # get test cases, trid in list_args[1]   
test_cases=getTestCases(list_args[1])
# check for mistakes   
getItemMessage(test_cases)     

qaPrint(log,'Starting ' + list_args[0] + list_args[1])
qaPrint(log,'Got test cases')
qaPrint(log, str(test_cases))

# close the log file if it open
if not log.closed:
    log.close()
         
