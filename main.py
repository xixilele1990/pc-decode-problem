def decode(code):

    # get the length of the code
    length = len(code)

    # if the code is an empty string, there is nothing to decode
    # if the code starts with the 0, we cannot decode it
    if length == 0 or code[0] == "0":
        return 0

    # create a memo to store the number of ways each substring can be decoded
    # memo[i] = number of ways s[0:i] can be decoded
    # the extra element (memo[0]) will be used to solve edge cases 
    memo = [0 for i in range(length + 1)]

    # initialize base cases
    # memo[0] will be used to account for edge cases such as '30' where 
    # it may seem by looking at just the first element we can decode the
    # message, but it is actually impossible
    memo[0] = 1
    memo[1] = 1

    for i in range(2, length + 1):
        
        # check if previous digit can be translated to a letter
        if 1 <= int(code[i-1:i]) <= 9:
            # add number of ways we can decode s[0:i-1] to 
            # number of ways we can decode s[0:i]
            memo[i] += memo[i-1]

        # check if previous two digits can be translated to a letter
        if 10 <= int(code[i-2:i]) <= 26:
            # add number of ways we can decode s[0:i-2] to
            # number of ways we can decode s[0:i]
            memo[i] += memo[i-2]

    # return the number of ways we can decode entire string
    return memo[length]


assert (decode('12106')) == 2
assert (decode('339')) == 1
assert (decode('306')) == 0

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
