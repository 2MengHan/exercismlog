def is_armstrong_number(number):
    remain = abs(number)
    weishu=0
    weihe = []
    while remain > 0 :
        weihe.append(remain % 10)
        remain //= 10
        weishu += 1
    weihe_squ = [i**weishu for i in weihe]
    weihe_squ_sum = sum(weihe_squ)
    if weihe_squ_sum == number:
        return True
    else : 
        return False
