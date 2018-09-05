dictionary = {"mobile", "samsung", "sam", "sung", "man", "mango",
              "icecream", "and", "go", "i", "like", "ice", "cream"}

dp = {}

def matches(word):
    if word is None or len(word) == 0:
        return True

    if word in dp:
        return dp[word]

    for i in range(len(word)):
        substr = word[0:i + 1]

        if substr in dictionary and matches(word[i + 1:]):
            dp[word] = True
            return True

    dp[word] = False
    return False

print(matches("ilikesamsung"))
print(matches(""))
print(matches("ilikelikeimangoiii"))
print(matches("samsungandmango"))
print(matches("samsungandmangok"))
