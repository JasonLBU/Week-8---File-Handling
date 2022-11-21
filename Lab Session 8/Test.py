def DataStream():
    import statistics
    Data =  input("")
    RunnerID = Data.split('::')[0]
    Time = Data.split('::',1)[0]
    print(RunnerID)
    print(Time)





print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!")
DataStream()