def sort(s1):
    s1 = s1.lower()
    s1 = s1.replace(' ','')
    le = len(s1)
    s2 = []
    for i in range(0,le):
        s2.append(s1[i])
    for i in range(0,le):
        for j in range(i+1,le):
            if (s2[i]>s2[j]):
                temp = s2[i]
                s2[i] = s2[j]
                s2[j] = temp
    return s2
            
def check_anagram(st1,st2):
    s1 = sort(st1)
    s2 = sort(st2)
    l1 = len(s1)
    l2 = len(s2)
    if l1 != l2:
        return 'Not an Anagram'
    for i in range(l1):
        if s1[i] != s2[i]:
            return 'Not an Anagram'
    return "It's an Anagram !"
