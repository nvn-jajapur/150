
"""
Two Pointer - Sliding Window

to calculate how many chars are needed to be replaced in str 
Formula is = len - freq 
here len : length of the sub string ( r-l+1)
freq = the max number of times a char has appearred

"""


def longest_repeating_char_replace(s:str, k:int)->str:
    l=r=maxLen=freq=0
    mpp={}
    while( r< len(s)):
        mpp[s[r]] =mpp.get(s[r],0)+1
        freq = max(freq, mpp[s[r]])
        if((r-l+1) - freq <= k):
            maxLen = max(maxLen, (r-l+1))
        if((r-l+1) - freq > k):
            mpp[s[l]] = mpp.get(s[l],0)-1
            l+=1
        r+=1
    return maxLen



if __name__ =="__main__":
    s = "AABABBA"
    print(longest_repeating_char_replace(s,1))