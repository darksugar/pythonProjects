#Authon Ivor

class Flight(object):
    def __init__(self,name):
        self.flight_name = name


    def checking_status(self):
        print("checking flight %s status " % self.flight_name)
        return  1

    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 0 :
            print("flight got canceled...")
        elif status == 1 :
            print("flight is arrived...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...,please check later")

    @flight_status.setter
    def flight_status(self,status):
        status = status
        print("666")

    @flight_status.deleter
    def flight_status(self):
        print("it's delete")

f = Flight("CA980")
f.flight_status
f.flight_status = 2  #调用@flight_status.setter
del f.flight_status  #调用@flight_status.deleter
