s = "sdkjf78934239ie!2#$%^*f"
l = ['0','1','2','3','4','5','6','7','8','9']

for i in range(len(s)):
    print(i,'print iiiiiiiiiiiiii')
    print(s[i],'s[i] **********')
    if s[i] in l:
        if int(s[i]) % 2 == 0:
            print(s[i], end=" ") 