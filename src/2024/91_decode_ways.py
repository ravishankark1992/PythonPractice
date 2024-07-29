class Sol:
    def numDecodings(self, s: str) -> int:
        if not s and s[0]=='0':
            return 0
        memo = {len(s): 1}
        
        for i in range(len(s)-1, -1, -1):
            if s[i]=='0':
                memo[i] = 0
            else:
                memo[i] = memo[i+1]
                
                if i>0 and int(s[i-1])>0 and int(s[i-1:i+1])<27:
                    memo[i] += memo[i+2]
        print(memo)
        return memo[0]
x=Sol()
print(x.numDecodings('61207'))