# -*- coding: utf-8 -*-
"""
#   -------------------------------------------------   #
#
#   -------- Description --------
#   	read config.cfg and save variables
#
#   -------- Run --------
#
#
#
#   Created on Sat Mar 10 16:58:50 2018 by   O.Keller
#   -------------------------------------------------   #
"""
import os, re

cfg = "config.cfg"
key_words = ['meshed', 'new', 'error']

def main():
    var, allKeyWords = read_config(cfg, key_words)
    globals().update(allKeyWords)
    globals().update(var)

    new.remove('test2.CATPart')
    meshed.append('test2.CATPart')

    update_config(cfg, var, key_words)

def update_config(cfg, var, key_words):
    f = open(cfg,'w')
    for varName, varValue in var.items():
        f.write("{:<15}={:>20}\n".format(varName, varValue))

    # --- word1 = [test1, test2, ...]   word1: i=0 test1:j=0
    for i in key_words:
        for j in globals().get(i):
           f.write("{:<15}{:>20}\n".format(i, j))


    f.close()

def read_config(cfg, key_words):
    allVariabel = {}
    allKeyWords = {}

    if os.path.isfile(cfg):
        f = open(cfg,'r')
        for line in f:
            # --- key-elements
            comment = re.match(r'^#.*', line)
            empty   = re.match(r'^\s*$', line)

            # --- save Variable, syntax inlcude = name.inc
            #      include --> Variable name
            #      name.inc --> varibale value
            variable = re.match(r'(\S+)\W*=\W*(\S+)', line)

            # --- search for all keywords, if line begins with <actoword>
            #   store in dict matchWords
            # bsp:   meshed     test1.CATPart
            #   keyWord : meshed
            #   allKeyWords -->  {'meshed': ['test1.CATPart']}
            matchWords = {}
            for actword in key_words:
                temp = re.match(r'{}\W*(\S+)'.format(actword),line)
                if temp:
                    matchWords.update({actword: temp.group(1) })


            # --- check key-elements
            if comment or empty: continue
            if variable:
                allVariabel.update({variable.group(1):variable.group(2)})
            for name, value in matchWords.items():
                try:
                    allKeyWords[name].append(value)
                except KeyError:
                    allKeyWords.update({name:[value]})
        f.close()

    else:
        f = open(cfg, 'w')
        f.write(txt_cfg)
        f.close()

    return allVariabel, allKeyWords


txt_cfg = """workingDir =             c:/temp
meshed            test.CATPart
meshed            test1.CATPart
new               test2.CATPart
new               test2.CATPart
"""

if __name__ == "__main__":
    main()

