
# no space only number for 0-9 , no constrain how many digits  < 10^9
# map to store relation bt number to char  key : number -- value char
# the number should <=26 and also larger than 1 
# # dp[i] until the current digit how many ways to decode  (check if this digit is valid)
# cornercase  startingwith 0 --c an not decode 
# dp[0] = 1 dp[1]= (if previous number betwen larger than > or =0 3,   dp[i] = dp[i-1]; if previous numebr is  1, dp[i] = dp[i-1]+1    )
#else curerent between (0-6)   dp[i] = dp[i-1] +1 


def decode(code):
    if code.startswith("0"):
        return 0 
    
    dp = [0] * (len(code)+1)
    dp[0] = 1 
    
    for i in range(1,len(code)):
        
        if int(code[i]) >= 3 or int(code[i])==0:  # > 30 or exclude 09
            dp[i] = dp[i-1]
        
        elif int(code[i]) ==1:   # 10-19
            dp[i] = dp[i-1] + 1
        
        elif 6 >= int(code[i+1]) >=0:   # 20- 26
            dp[i] = dp[i-1] + 1
        
        else:
            dp[i]= dp[i-1] 
    print(dp)        
    return dp[len(code)]
            
        
        
        
    
    
    
1,2,1
12,1
    

print(decode('12106'),"AAA")
assert (decode('12106')) == 2
assert (decode('339')) == 1
assert (decode('306')) == 0

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
