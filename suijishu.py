#  coding = utf-8
#! python3.6
# 2019.12.21

import random
import sys
import duquguaci

gkey = ''
def qigua():
    gkey = ''
    for i in range(6):
        num = random.randint(0,1)
        gkey = gkey+str(num)
        """if num == 1:
            print("___")
        else:
            print("_ _")"""
    return gkey
#print("\n")
#duquguaci.duquguaci(gkey)
gkey = qigua()
guaming = duquguaci.getguaming(gkey)
guaci = duquguaci.getguaci(gkey)
