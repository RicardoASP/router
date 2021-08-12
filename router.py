'''
Design an application router
author: Ricardo Sanchez

requirements:
-Load config is called only once during the application start up. This function parses and loads the routing config file (example given below) into an internal data structure used by findRoute() function. Once loaded, the routes do not change. Routes are specified as one pattern per line (see the example below).
-findRoute takes a string as an input and returns a server name that is also a string. Input is a string like "<customer_id>.<country>.<state>.<city>". findRoute function returns the server that matches the input. The routes in config file could contain ‘*’ in them to accept any value. ‘*’ appears only in the trailing parts of the rule. Rules are not given in any specific order in the configuration file. When more than one rule matches, most specific match wins.

assumptions:
-key's patterns in config file are uniques
-wildcards in keys are always specified as *
-there is only one config file which rules are added to
-config file is at the same level as project ROOT
'''

import json
import fnmatch
import os

class router():
    def __init__(self):
        #load config file when initializing the object
        self.config_file_path = os.path.abspath(os.path.dirname(__file__)) + "/config.json"
        self.config_file = self.loadConfig(self.config_file_path)

    def loadConfig(self,config_file_path):
        open_config = open(config_file_path)
        config_file = json.load(open_config)

        return config_file

    def findRoute(self,input):
        selected_routes_dict = {}

        #loop through config file keys
        for key in self.config_file.keys():
            #find all matches and weight them based on the number of wildcards
            if fnmatch.fnmatch(input,key):
                weight = key.count('*')
                selected_routes_dict[weight] = self.config_file[key]

        #sort matches based on weights
        sorted_list = sorted(selected_routes_dict.keys())
        #pick the best match based on weights
        higher_match_server = selected_routes_dict[sorted_list[0]]


        return print(higher_match_server)

# script runtime test
if __name__=="__main__":
    import time

    test1 = ['customer1.us.ca.sfo']
    test2 = ['customer1.us.ca.sfo','customer1.us.ca.sjc','customer2.us.tx.dfw','customer2.cn.tw.tai','customer10.us.ny.nyc']

    # initialize class
    r = router()

    # basic runtime test
    print("""########### test 1 ###########
    test input 1=""" + str(test1))
    for address in test1:
        start_t = time.time()
        r.findRoute(address)
        print("--- %s sec ---" % (time.time() - start_t))

    print("""########### test 2 ###########
    test input 2=""" + str(test2))
    for address in test2:
        start_t = time.time()
        r.findRoute(address)
        print("--- %s sec ---" % (time.time() - start_t))

