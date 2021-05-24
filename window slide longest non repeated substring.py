#longest substring with non repeated char'''
#window slide method"
s = "abcabcbb"
maxL=0
window=set()
l=0
for r in range(len(s)):
    while s[r] in window:
        window.remove(s[l])
        l+=1
    window.add(s[r])
    maxL=max(maxL,len(window))       
print(maxL)
            
