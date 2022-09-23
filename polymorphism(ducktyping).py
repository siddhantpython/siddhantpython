class pycharm:
    def execute(self):
        print("compiling")
        print('running')

class myeditor:
    def execute(self):
        print('conventional')
        print('spell check')
        print("compiling")
        print('running')

class laptop:
    def code(self,ide):#ide:integerated development environment
        ide.execute()  #in duck typing we can access various methods or fuction of different classes#
                       #but it should have same function as execute()

ide1=pycharm()
ide2=myeditor()
lap=laptop()
lap.code(ide1)
lap.code(ide2)