def anagram1(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)


def anagram2(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for i in s1:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i in s2:
        if i in count:
            count[i] -= 1;
        else:
            count[i] = 1;

    for i in count:
        if count[i] != 0:
            return False

    return True


print(anagram1("clint eastwood", "old west action"))
print(anagram2("clint eastwood", "old west action"))
print(anagram1("clint eastwood", "olsd west action"))
print(anagram2("clint eastwood", "olsd west action"))