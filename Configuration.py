"""
    This module will read a file that ends with .conf and construct a dictionary of its contents.
"""

import Log

class Configuration:
    def __init__(self, path: str):
        self.__path = path
        Log.LogEvent(f"Opening configuration file \"{path}\"")
        try:
            self.__file = open(path, 'r')        
        except FileNotFoundError as e:
            Log.LogEvent(f"The file was not found.", Log.Error)

        Log.LogEvent("Opened file, now reading...")
        self.ReadFile()
    
    def ReadFile(self) -> None:
        self.__configurations = {}
        line = None
        while True:
            line = self.__file.readline()
            if (line == None): # No more lines
                break
            
            # Split the string by '='
            Splits = line.split("=")
            if (len(Splits) < 2): # No = was found, not proper format
                Log.LogEvent(f"The line \"{line}\" is not in proper format, to be ignored....", Log.Warning)
                continue

            Name = Splits[0]
            Value = Splits[1]
            if (len(Splits) > 2): # There was another = after the first one, and string re-combination must occur.
                for i in range(2, len(Splits)-1): # Go through each other element and add it back together.
                    Value += "=" + Splits[i]
            
            Name = Name.strip().lower() # For best searches.
            Value = Value.strip() # For most accurate results.
            if (self.__configurations.get(Name) != None):
                Log.LogEvent(f"The configuration with name \"{Name}\" is a duplicate, only the first item is kept.", Log.Warning)
                continue

            self.__configurations.update({Name: Value})
            Log.LogEvent(f"Configuration file property \"{Name}\" was added sucessfully.", Log.Debug)
        
        Log.LogEvent(f"Configuration file read, {len(self.__configurations)} configuration(s) were found.")


    def RetriveConfiguration(self, name: str) -> str:
        name = name.strip()
        Value = self.__configurations.get(name)
        if (Value == None):
            Log.LogEvent(f"A configuration of name \"{name}\" was not found.", Log.Warning)
            return None

        return Value

    def SetConfiguration(self, name: str, value: str) -> None:
        name = name.strip()
        Value = self.__configurations.get(name)
        if (Value == None):
            Log.LogEvent(f"A configuration of name \"{name}\" was not found.", Log.Warning)
            raise NameError("The name could not be found.")

        self.__configurations[name] = value
        

if __name__ == "__main__":
    Log.InitLog("configuration_run.log", Log.Debug)
    conf = Configuration("test_conf.conf")
    print(conf.RetriveConfiguration("name"))
    print(conf.RetriveConfiguration("your friend"))