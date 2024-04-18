import os, re
    
        
def getfiles(path):
        s = ''
        l = []

        # get all pgns to one string
        for x in os.listdir(path):
            s = s + open(path + r"\\" + x, 'r').read()
        
        # seperate each game to its own string
        pattern = re.compile(r"(\[Event[\s\S]*?\n\n[\s\S]*?\n\n)")
        l = re.findall(pattern, s)
        
        return l
    