def sort_sentence(sentence):
    sentence=sentence.split()
    count = 0
    for i in sentence[0]:
        if i.isupper() and count < 1:
            count += 1
            u = i.lower()
            sentence[0] = sentence[0].replace(i, u)
    p = len(sentence)
    for i in range(p):
        for f in range(i+1,p):
            if len(sentence[i]) > len(sentence[f]):
                temp = sentence[i]
                sentence[i] = sentence[f]
                sentence[f] = temp
    count=0
    for i in sentence[0]:
        if i.islower() and count<1:
            count+=1
            u = i.upper()
            sentence[0] = sentence[0].replace(i, u)
    neeeew_sentence=' '.join(sentence)
    return neeeew_sentence
print (sort_sentence(sentence))
