def toStr(num,base):
    convertStr="0123456789ABCDEF"
    if num<base:
        return convertStr[num]
    else:
        return convertStr[num%base]+toStr(num//base,base)
print(toStr(65535,2)[::-1])