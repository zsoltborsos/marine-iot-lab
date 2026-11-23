from infrarcv import infraGetCMD

rec = infraGetCMD(14)
while True:
    try:
        irValue = rec.ir_read()
        if irValue:
            print(irValue)
    except:
        print("IR error, resetting")
        rec.reset()
        pass
    
