import configparser,os,sys


curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "config/user.ini")
conf = configparser.ConfigParser()
conf.read(cfgpath, encoding="utf-8")

def config(a,b):
    return conf.get(a, b)
