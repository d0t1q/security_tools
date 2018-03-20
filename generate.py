#!/usr/bin/python
import sys, pip, git, os, csv, fnmatch, subprocess
from git import Repo
from os import path

urls_file="urls_git.csv"
urls_git = list(csv.reader(open(urls_file)))

def menu_command(request_generate):
    #request_generate=int(request_generate)
    if request_generate==1:
        wordlists()
    if request_generate==2:
        dir_scan()
    if request_generate==3:
        exploit_tools()
    if request_generate==4:
        wordlists()
        dir_scan()
        exploit_tools()
    if request_generate==5:
        precompiled()
    if request_generate==6:
        wordlists()
        dir_scan()
        exploit_tools()
        precomplied()
    if request_generate==7:
        add_repos()
    if request_generate==8:
        update_gits()
    if request_generate==9:
        inst_req()
    if request_generate==98:
        repo_list()
    raw_input( "\nLoop complete press Enter to conitnue")
    main()

def pip_inst(package):
    pip.main(['install', package])

def update_gits():
    subprocess.call("./updateGit.sh")

def inst_req():
    matches = []
    for root, dirnames, filenames in os.walk('./'):
        for filename in fnmatch.filter(filenames, 'requirements*'):
            matches.append(os.path.join(root, filename))
    req_lib=[]
    for i in xrange(0, len(matches)):
        with open(matches[i]) as f:
            req_lib.extend( f.read().splitlines())
            f.close()
    print "\n[- INSTALLING THE FOLLOWING LIBRARIES -]"
    for i in xrange(0, len(req_lib)):
        print req_lib[i]
    for i in xrange(0, len(req_lib)):
        pip_inst(req_lib[i])

def repo_list():
    print "\n[- CURRENT REPO LIST -]"
    print "\n SECTION +|+ SHORT NAME +|+ URL\n"
    for i in xrange(0, len(urls_git)):
        print urls_git[i][0]+"\n\t +|+ "+urls_git[i][1]+"\n\t\t\t +|+ "+urls_git[i][2]

def add_repos():
    f=open("urls_git.csv","a")
    print """
    Lets add a repo, what section do you want to add it to?
    wordlists(w) - directory scanners(d) - exploit tools(e) - precompiled repos(p)

    """
    selection = raw_input("Your selection: ")
    if selection.lower() =="w" or selection.lower() =="d" or selection.lower()\
    =="e" or selection.lower() =="p":
        repo_url = raw_input("The url of the repo: ")
        repo_short = raw_input\
        ("enter a short form name of the repo(what the folder will be called): ")
        if selection.lower() =="w":
            f.write("wordlist,"+repo_short+","+repo_url)
        if selection.lower() =="d":
            f.write("dirscan,"+repo_short+","+repo_url)
        if selection.lower() =="e":
            f.write("tools,"+repo_short+","+repo_url)
        if selection.lower() =="p":
            f.write("precomplied,"+repo_short+","+repo_url)
    else:
        add_repos()
    f.close()

def wordlists():
    print "\n[- WORD LIST GENERATION -]"
    word_list = [i for i in urls_git if i[0] == "wordlist"]
    if path.isdir(word_list[0][0]):
        pass
    else:
        os.mkdir(word_list[0][0])
    for i in xrange(0, len(word_list)):
        print "Generating "+word_list[i][1]
        try:
            Repo.clone_from(word_list[i][2],word_list[0][0]+"/"+word_list[i][1])
        except:
            print "already exists, passing"

def dir_scan():
    print "\n[- DIR SCANNING TOOLS GENERATION -]"
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
        print "Generating "+dir_scan[i][1]
        try:
            Repo.clone_from(dir_scan[i][2],"tools/"+dir_scan[0][0]+"/"+dir_scan[i][1])
        except:
            print "already exists, passing"

def exploit_tools():
    print "\n[- EXPLOIT TOOLS GENERATION -]"
    exp_tools = [i for i in urls_git if i[0] == "tools"]
    if path.isdir(exp_tools[0][0]):
        pass
    else:
        os.mkdir(exp_tools[0][0])
    for i in xrange(0, len(exp_tools)):
        print "Generating "+exp_tools[i][1]
        try:
            Repo.clone_from(exp_tools[i][2],exp_tools[0][0]+"/"+exp_tools[i][1])
        except:
            print "already exists, passing"
def precomplied():
    print "\n[- PRECOMPILED REPO GENERATION -]"
    pre_comp = [i for i in urls_git if i[0] == "precomplied"]
    if path.isdir(pre_comp[0][0]):
        pass
    else:
        os.mkdir(pre_comp[0][0])
    for i in xrange(0, len(pre_comp)):
        print "Generating "+pre_comp[i][1]
        try:
            Repo.clone_from(pre_comp[i][2],pre_comp[0][0]+"/"+pre_comp[i][1])
        except:
            print "already exists, passing"
def help():
    print """
        Generates a security tools folder
          """
    sys.exit()

try:
    def main():
        os.system('clear')
        args = sys.argv[1:]
        if not args:
            print """

        This script will generate a few folders and scripts based on predefined
        github repos.

        Select which Tasks you would like to preform

    1)  Generate only Wordlsits+FuzzDB              7)  Add New repo to list
    2)  Generate only web directory scanners        8)  update all repos
    3)  Generate only exploit tools                 9)  install all dependancies
    4)  Generate WordList+tools                     98) print out all repos
    5)  Generate the precomplied git repos          99) exit
    6)  Generate all
        """
            request_generate = raw_input("\n Make your selection: ")
            request_generate=int(request_generate)
            if request_generate<=98:
                menu_command(request_generate)
            else:
                exit()
        #if sys.argv[1].lower() == "-h" or sys.argv[1].lower() == "--help":
        #    help()
        else:
            help()
            sys.exit()

#check for ^C
except KeyboardInterrupt:
    print '\n'" Bye!"
    sys.exit()

#Call the main function
if __name__=='__main__':
    main()
    sys.exit()
