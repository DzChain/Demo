#  coding = utf-8
#! python3.6
# 2019.12.21

def duquguaci(gkey):
    f = open('guaci64.txt')
    flag = 0
    for each_line in f:
        if flag:
            if each_line[:10] == '==========':
                break
            print(each_line)
        if each_line[:6] == geky:
            flag = 1
            print("卦名：" + each_line[6:])
            print("卦辞：")
    f.close()
def getguaming(gkey):
    f = open('guaci64.txt')
    guaming = ""
    for each_line in f:
        if each_line[:6] == gkey:
            guaming = each_line[6:]
    f.close()
    return guaming
def getguaci(gkey):
    f = open('guaci64.txt')
    flag = 0
    guaci = ""
    for each_line in f:
        if flag:
            if each_line[:10] == '==========':
                break
            #print(each_line)
            guaci += each_line
        if each_line[:6] == gkey:
            flag = 1
    f.close()
    return guaci
def main():
    #duquguaci("000000")
    print(getguaci("111111"))
    print(getguaming("111111"))
if __name__ == '__main__':
    main()
