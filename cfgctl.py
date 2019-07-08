import os
import re

from lawpack import Debug

def BuildDefault():
    """docstring for BuildDefault."""
    SCSD = BuildSCSD()
    print(str(SCSD))
    example = '''
    {
        \"DEBUG_MODE\" : 1,
        \"SHELL\" : \"%(SHELL)s\",
        \"LAWPACKDIR\" : \"%(LAWPACKDIR)s\",
        \"LAWDIR\" : \"%(LAWDIR)s\",
        \"LOG_FILE\" : \"%(LOG_FILE)s\",
        \"INS_FILE\" : \"%(INS_FILE)s\",
        \"CLANG\" : \"%(CLANG)s\",
        \"SCSD\" :  %(SCSD)s ,
        \"CTC\" : { %(CTC)s }
    }''' % {
            "SHELL": os.environ["SHELL"],
            "LAWPACKDIR": os.environ["LAWPACKDIR"],
            "LAWDIR": os.environ["LAWDIR"],
            "LOG_FILE": os.environ["LAWPACKDIR"]+"/lawpack.log",
            "INS_FILE": os.environ["LAWPACKDIR"]+"/input.json",
            "CLANG": "SCHLUM2",
            "SCSD": SCSD,
            "CTC": ""
            }
    file = open('config.json', 'w')
    file.write(example.replace('\r',  ''))
    # print(file.read())
    # print(example)
    file.close()
    ## DEBUG: Content
    file = open('config.json', 'r')
    Debug(file.read())
    file.close()
    # os.remove("config.json")

def BuildSCSD():
    """docstring for BuildSCSD."""
    try:
        WINTMP = 'C:\cygwin64\lawson\l9qa\law\qa91'
        # lawdir = (os.environ["LAWDIR"]+"/"+os.environ['XXPDL']+"/").replace('\r', '')
        lawdir = WINTMP
        lsdir = os.listdir(lawdir)
        print(lsdir)
        dir_dict = {}

        for dir in lsdir:
            if re.match("^[A-Za-z]{2}src$", dir):
                dir_dict[dir[:2].upper()] = dir

        return dir_dict

    except Exception as e:
            raise e
