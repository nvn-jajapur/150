def mini_window(s:str,t:str)->str:
    l=0
    r=len(t)-1
    count=0
    startIndex =-1
    minLen = 10000
    hmap={}
    for i in t:
        hmap[i] = hmap.get(i,0)+1
    while( r< len(s)):
        if(hmap.get(s[r],0) >0):
            count+=1
        hmap[s[r]] = hmap.get(s[r],0)-1
        if(count == len(t)):
            if((r-l+1) < minLen):
                minLen = (r-l+1)
                startIndex =l
            hmap[s[l]] = hmap.get(s[l],0)+1
            if(hmap[s[l]]>0):
                count-=1
            l+=1
        r+=1
    return  "" if startIndex ==-1 else s[startIndex:minLen]

if __name__ =="__main__":
    s = "ADOBECODEBANC"
    t="ABC"
    print(mini_window(s,t))