class creditcard:
    def salary(self):
        self.basepay=1000
        self.exp="04/2021"
    def reccard(self):
        print(self.basepay,self.exp)


caleb=creditcard()
caleb.salary()
caleb.reccard()


class creditcard:
    def salary(self,b,ex):
        self.basepay=b
        self.exp=ex
    def reccard(self):
        print(self.basepay,self.exp)


jv=creditcard()
jv.salary(1000,25)
jv.reccard()


class career:
    def __init__(self,ed,w):
        print("career")
        self.education=ed
        self.working=w
    def passion(self):
        pass

class movie(career):
    def __init__(self,w):
        print("movie")
        super().__init__("school",9)
        self.now=w

ab=movie(10)


class tune:
    def __init__(self,p,d):
        print("tune")
        self.progress=p
        self.dynamic=d
    def insturemnt(self):
        pass
    
class song(tune):
    def __init__(self,r):
        print("song")
        super().__init__("on progress","yes")
        self.relaese=r
        
newsong=song("done")



class joy:
    usa="happy"
    def __init__(self,n:str="caleb",a:int=20,d:str="ceo"):
        self.name=n
        self.age=a
        self.destination=d

obj1=joy()

obj2=joy("kingsley",19,"CEO")
    





