import json
import os

MY_DATOS =  "data/"

def Newfile(*param):
    with open(MY_DATOS,"w") as wf:
        json.dump(param[0],wf,indent=4)

def updatefile(*param):
    with open(MY_DATOS,"w") as fw:
        json.dump(param[0],fw,indent=4)        
        
def addData(*param):
    data =list(param)
    with open(MY_DATOS,"r+") as rwf :
        data_file=json.load(rwf)
        if (len(param) > 1):
            data_file[data[0]].update({data[1]:data[2]})
        else:
            data_file.update({param[0]})
    
        rwf.seek(0)
        json.dump(data_file,rwf,indent=4 )
        
def readfile():
    with open(MY_DATOS,"r") as rf:
        return json.load(rf)            
            
def checkfile(*param):
    data = list(param)
    if(os.path.isfile(MY_DATOS)):
        if(len(param)): 
            data[0].update(readfile())        
    else:
        if(len(param)):
            Newfile(data[0])