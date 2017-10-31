def outerFunction ():
    global var
    var = 12
    def innerFunctin():
        global var
        var = 31
        print ('var',var)
var=11
innerFunction()
print('var=',var)
