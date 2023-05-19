

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
    return result


def checker(target,result):
     if(target<result):
          print("true target")
     elif target>result:
          pass
     else:
          print("target and result is equal")

fina= calc_checket(1,2,3,4)
print(fina , ' this sfile ')