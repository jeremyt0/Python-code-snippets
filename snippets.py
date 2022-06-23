
# Singleton class

class ClassName:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(ClassName, cls).__new__(cls)
    return cls._instance
    
# Parse string of arguments to return dict
from shlex import split
def parseString2Dict(string:str="a=hello b=123"):
  args_list = list(filter(lambda k: '=' in k, split(args_str)))
  args_dict = dict(map(lambda x: x.split('='), args_list))
  return args_dict


