def ch():                                               #closure concept
    print("i am a super coder")
    def hg():
        print("yes i am")
    return hg
ret= ch()
ret()







def running(**args):                                   #getting n number of arguements
    for i in args:
        print(i)


def joy(happy):                                        #generator cocept
    if happy =="positive":
        print("smiling face")
    elif happy=="worried":
        print("unhappy face")
    yield"disys"
    print("long life")





def smile(worries):                                  #decorator concept
    print("stand strong!")
    worries("tough","quite easy to handle")



def problem(difficult,easy):
    print(difficult,easy)


smile(problem)
    
