 # Levenshtein distance(Edit distance) between two words is the minimum number of single-character edits
 # (insertions, deletions or substitutions) required to change one word into the other.

def ascii_deletion_distance(s1, s2):
    list1 = compareLetters(s1, s2)
    list2 = compareLetters(s2, s1)
    return sum(list1+list2)


def stillLetters(s):
    return len(s) > 0


def compareLetters(s1, s2):
    count = 0
    list = []
    while stillLetters(s1) and stillLetters(s2):
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[0] == s2[j]:
                    s1 = s1[1:]
                    s2 = s2[:j] + s2[j + 1:]
                    count += 1
                    break

        if not s1[:1] == "": list.append(ord(s1[:1]))
        s1 = s1[:0] + s1[1:]
    return list

print(ascii_deletion_distance("at", "cat"))
print(ascii_deletion_distance("boat", "got"))
print(ascii_deletion_distance("thought", "sloughs"))
