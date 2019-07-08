#! /usr/bin/python

# package


import json
import os
import sys
import cfgctl
# from cfgctl import Cfgctl

DEBUG_MODE = 1


# Terminal colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def Debug(message):
    """ Define type of messages """
    if DEBUG_MODE != 0:
        print(bcolors.OKGREEN + "[DEBUG]: %s" % message + bcolors.ENDC + "\n")


def Info(message):
    print(bcolors.OKBLUE+"[INFO]:%s \n" % message + bcolors.ENDC)


def Warn(message):
    print(bcolors.WARNING+"[WARN]: %s \n" % message+bcolors.ENDC)


def Error(message):
    print(bcolors.FAIL+"[ERROR]: %s \n " % message+bcolors.ENDC)


""" ReadInstruct -> open json file and load content to variable """


def ReadInstruct(path):

    try:
        fh = open(path, "r")
    except IOError:
        Error("Unable to open instruction file")
        sys.exit()

    Debug("Reading the instruction file")

    content = fh.read()

    fh.close()

    if content is None or content == "":
        Debug("Reading unsuccesfull")
        Warn("No instruction imported")

    Debug(content)

    return content


""" ParseJSON -> using json library decoding from JSON format to dict type """


def ParseJSON(to_decode):
    instructions = json.loads(to_decode)

    Debug(json.dumps(instructions, indent=4, sort_keys=True))

    return instructions


def CheckConfig():
    try:
        conf_file = open('config.json', 'r')

    except IOError:
        Warn("No config file in: "+os.getcwd() +'/')
        Info("Building config file")
        BuildConfig('default')


    # if conf_file is not None:
        #set varibles


def BuildConfig(type):
    cfgctl.BuildDefault()


def Main():

    # TODO: base env vars
    try:
        if os.environ['DEVENV'] in ['True', True, '1']:
            Debug("Running in DEV mode")
            os.system('/bin/bash . devenv.sh')
    except KeyError:
        Debug("Running in DEV mode")
        os.system('/bin/bash . devenv.sh')



    Debug("Reading the config file")

    CheckConfig()

    os.remove('config.json')

    # Debug("Opening the instruction file")
    #
    # content = ReadInstruct(INS_FILE)
    #
    # Debug("Parsing JSON")
    #
    # instructions = ParseJSON(content)
    #
    # for copy in instructions['appfiles']:
    #     # os.system('echo "./copy "+copy+ "./"+copy+"2"' )
    #     os.system(SHELL+" copy.sh " + copy + " " + copy + "2")


if __name__ == "__main__":
    Main()
