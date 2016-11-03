'''
Created on Oct 19, 2016


@author: alamingo
@author: team_7
'''
from rfaUtils import getItemMessage, getMessage,getLogdir,getArgs,getLog,qaPrint,getTestCases,getLocalEnv

import sys
name_env_file = "local.properties"
                 
local_env = getLocalEnv(name_env_file)

getItemMessage(local_env)
        
log_dir = getLogdir(local_env)
getItemMessage(log_dir)

list_args = getArgs(sys.argv) 
getItemMessage(list_args)
  
log = getLog(log_dir,list_args[0])
getItemMessage(log)
    
test_cases=getTestCases(list_args[1])   
getItemMessage(test_cases)     

qaPrint(log,'Starting ' + list_args[0] + list_args[1])
qaPrint(log,'Got test cases')
print(test_cases)

# close the log file if it open
if not log.closed:
    log.close()
         
