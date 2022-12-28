def longest_common_prefix(strs: str):
    if len(strs) == 0:
        return ""
    elif len(strs) == 1:
        return strs[0]
    common = strs[0]
    common_length = len(common)
    for s in strs[1:]:
        while common != s[0:]:
            pass
    return common
