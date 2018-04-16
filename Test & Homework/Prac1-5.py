MoneyStr = input()
if MoneyStr[0] in ["R"]: #中括号，取字符串里某一个元素
    USD = eval(MoneyStr[3:]) / 6.78
    print("USD{:.2f}".format(USD))
elif MoneyStr[0] in ["U"]:
    RMB = 6.78 * eval(MoneyStr[3:]) 
    print("RMB{:.2f}".format(RMB))
