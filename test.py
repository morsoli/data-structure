def longestPalindrome(s):
    demo={}
    if not s:
        return s
    for i in range(len(s)):
        for j in range(len(s)-i):
            demo_str=s[i:j+i+1]
            if demo_str[::-1]==demo_str:
                demo[len(demo_str)]=demo_str
            else:
                continue
    return demo[max([i for i in demo])]
print(longestPalindrome("asdfghjkkjhgfasd"))