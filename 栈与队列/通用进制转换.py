from pythonds.basic.stack import Stack

def converter(deciaml,base):
    digits='0123456789ABCDEF'
    rem_stack = Stack()
    new_str = ""
    
    while deciaml>0:
        rem = deciaml%base
        rem_stack.push(rem)
        deciaml = deciaml//base
    while not rem_stack.isEmpty():
        new_str=new_str+digits[rem_stack.pop()]
    return new_str
print(converter(255,2))
print(converter(255,8))
print(converter(255,16))