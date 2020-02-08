# longest common subsequence

def lcs(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    output = [ [0 for i in range(0, len2+1)] for j in range(0, len1+1)]
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if str1[i-1] == str2[j-1]:
                output[i][j] = 1 + output[i-1][j-1]
            else:
                output[i][j] = max(output[i-1][j], output[i][j-1])
    return output[-1][-1]

# recursive program
def recursive_lcs(str1, len1, str2, len2):
    if len1 == -1 or len2 == -1:
        return 0
    if str1[len1] == str2[len2]:
        return 1 + recursive_lcs(str1, len1-1, str2, len2-1)
    else:
        return max(
            recursive_lcs(str1, len1-1, str2, len2),
            recursive_lcs(str1, len1, str2, len2-1)
        )


if __name__ == "__main__":
    str1 = "aaa"
    str2 = "aaa"
    val = recursive_lcs(str1, len(str1)-1, str2, len(str2)-1)
    print("LCS", val)
    print("LCS", lcs(str1, str2))
    print("LCS", lcs("AAAA", "BBBB"))
    print("LCS", lcs("ABCDE", "CDEBA"))
    