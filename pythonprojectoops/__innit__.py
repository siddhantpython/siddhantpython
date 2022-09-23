class computer:
    def __init__(self,cpu,battery,ram):
        self.cpu=cpu
        self.battery=battery
        self.ram=ram


    def config(self):
        print('config is',self.cpu,self.battery,self.ram)
comp1=computer('i5','3000mah','8gb')
comp2=computer('ryzen3','4000mah','16gb')

comp1.config()
comp2.config()