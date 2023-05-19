

def calc_checket(target,num,*nums,operators='+'):
    result =num
    if operators=='+':
        for item in nums:
            result+=item
    elif operators=='-':
            for item in nums:
                result-=item
    else:
        print("Please chose minus or plus ")
    checker(target,result)
    return result


def checker(target,result):
     if(target<result):
          print("true target is greater than your selected target")
     elif target>result:
          print("true target is lower than your selected target")
     else:
          print("target and result is equal")

fina= calc_checket(1,2,3,4)
print("the final resutl %d is filnal "% fina)