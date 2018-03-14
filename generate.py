#!/usr/bin/python
import sys
import pip
from git import Repo
import os
from os import path

urls_git=[
        ["wordlist","seclist","https://github.com/danielmiessler/SecLists"],
        ["wordlist","fuzzdb","https://github.com/hannestrunde/fuzzdb.git"],
        ["dirscan","inspathx","https://github.com/emilyanncr/inspathx.git"],
        ["dirscan","dirsearch","https://github.com/maurosoria/dirsearch.git"],
        ["dirscan","dir-Xcan","https://github.com/NoobieDog/Dir-Xcan.git"],
        ["dirscan","pyfuzz","https://github.com/AyoobAli/pyfuzz.git"],
        ["tools","crlf","https://github.com/d0t1q/CRLF-Injection-Scanner.git"],
        ["tools","autoSploit","https://github.com/NullArray/AutoSploit.git"],
        ["tools","ipScan","https://github.com/d0t1q/ipScan.git"],
        ["tools","jexboss","https://github.com/joaomatosf/jexboss.git"],
        ["tools","javaUnserialize","https://github.com/d0t1q/JavaUnserializeExploits.git"],
        ["tools","dorkbot","https://github.com/utiso/dorkbot.git"],
        ["precomplied","rhinoLabs","https://github.com/RhinoSecurityLabs/Security-Research.git"],
        ["precomplied","arsenalTools","https://github.com/toolswatch/blackhat-arsenal-tools.git"],
        ["precomplied","tactical-explotation","https://github.com/0xdea/tactical-exploitation.git"],
        ]

def menu_command(request_generate):
    print request_generate
    request_generate=int(request_generate)
    if request_generate==1:
        wordlists()
    if request_generate==2:
        dir_scan()
    if request_generate==3:
        exploit_tools()
    if request_generate==4:
        dir_scan()
        exploit_tools()
    if request_generate==5:
        precompiled()
    if request_generate==6:
        wordlists()
        dir_scan()
        exploit_tools()
    if request_generate==7:
        wordlists()
        precomplied()
    if request_generate==8:
        dir_scan()
        exploit_tools()
        precomplied()
    if request_generate==9:
        wordlists()
        dir_scan()
        exploit_tools()
        precomplied()


def wordlists():
    print "word list generation"
    word_list = [i for i in urls_git if i[0] == "wordlist"]
    if path.isdir(word_list[0][0]):
        pass
    else:
        os.mkdir(word_list[0][0])
    for i in xrange(0, len(word_list)):
        Repo.clone_from(word_list[i][2],word_list[0][0]+"/"+word_list[i][1])

def dir_scan():
    print "Generating DirScanning tools"
    dir_scan = [i for i in urls_git if i[0] == "dirscan"]
    if path.isdir("tools"):
        pass
    else:
        os.mkdir("tools")
    if path.isdir("tools/"+dir_scan[0][0]):
        pass
    else:
        os.mkdir("tools/"+dir_scan[0][0])
    for i in xrange(0, len(dir_scan)):
        Repo.clone_from(dir_scan[i][2],"tools/"+dir_scan[0][0]+"/"+dir_scan[i][1])


def exploit_tools():
    print "Generating exploit tools"
    exp_tools = [i for i in urls_git if i[0] == "tools"]
    if path.isdir(exp_tools[0][0]):
        pass
    else:
        os.mkdir(exp_tools[0][0])
    for i in xrange(0, len(exp_tools)):
        Repo.clone_from(exp_tools[i][2],exp_tools[0][0]+"/"+exp_tools[i][1])

def precomplied():
    print "Generating precomplied repos"
    pre_comp = [i for i in urls_git if i[0] == "precomplied"]
    if path.isdir(pre_comp[0][0]):
        pass
    else:
        os.mkdir(pre_comp[0][0])
    for i in xrange(0, len(pre_comp)):
        Repo.clone_from(pre_comp[i][2],pre_comp[0][0]+"/"+pre_comp[i][1])

def help():
    print """
        Generates a security tools folder
          """
    sys.exit()

try:
    def main():
        args = sys.argv[1:]
        if not args:
            print """
        This script will generate a few folders and scripts based on predefined github repos
        Select which Tasks you would like to preform

        1) Generate only Wordlsits+FuzzDB
        2) Generate only web directory scanners(inspathx, Dir-Xcan, dirsearch, pyfuzz)
        3) Generate only exploit tools(CRLF, AutoSploit, JexBoss, JavaUnserialize, dorkbot)
        4) Generate all tools(Options 2-3 and includes IPscanner and SiteServices.sh)
        5) Generate the precomplied git repos(Rhino-Labs, Arsenal-Tools)
        6) Generate options 1-4
        7) Generate options 1 and 5
        8) Generate options 4 and 5
        9) Generate all
        """
            request_generate = raw_input("\n Make your selection: ")
            menu_command(request_generate)

        #if sys.argv[1].lower() == "-h" or sys.argv[1].lower() == "--help":
        #    help()
        else:
            print "Invlaid formatting"
            sys.exit()

#check for ^C
except KeyboardInterrupt:
    print '\n'" Bye!"
    sys.exit()

#Call the main function
if __name__=='__main__':
    main()
