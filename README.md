# router
Run ```router.py```

 requirements:</br>
-Load config is called only once during the application start up. This function parses and loads the routing config file (example given below) into an internal data structure used by findRoute() function. Once loaded, the routes do not change. Routes are specified as one pattern per line (see the example below).</br>
-findRoute takes a string as an input and returns a server name that is also a string. Input is a string like "<customer_id>.<country>.<state>.<city>". findRoute function returns the server that matches the input. The routes in config file could contain ‘*’ in them to accept any value. ‘*’ appears only in the trailing parts of the rule. Rules are not given in any specific order in the configuration file. When more than one rule matches, most specific match wins.

 assumptions:</br>
-key's patterns in config file are uniques</br>
-wildcards in keys are always specified as *</br>
-there is only one config file which rules are added to</br>
-config file is at the same level as project ROOT</br>
