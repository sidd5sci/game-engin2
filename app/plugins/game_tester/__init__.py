
### meta data

author      = "siddhartha"
name        = 'level designer'
version     = '1.0.1'
main        = 'main.py'

load_sequence =[]

class Plugin:
    def __init__(self,*args,**kwargs):
        print('Level designer :',args,kwargs)
    def run(self):
        print("run")
    def meta(self):
        return load_sequence

