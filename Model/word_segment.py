from dictionary import Dictionary

#query = "Máy bay nào đến thành phố Huế lúc 13:30HR ?"
query = "Máy bay nào bay từ TP. Hồ Chí Minh đến Hà Nội ?. "
dictionary = Dictionary().get_dict()


def word_segmenting(query):
    query = query.lower()
    query = query.replace(',','')
    word_tokens = query.split()
    word_segment = []
    token_buff = ""
    for token in word_tokens:
    
        token_buff += token
        print(token,token_buff)
        if (token_buff in  dictionary.keys()) :
            if (dictionary[token_buff]!="remove_word"):
                word_segment.append(token_buff)
            token_buff = ""
        elif (token in dictionary.keys()):
            if (dictionary[token]!="remove_word"):
                word_segment.append(token)
            token_buff = ""
        
        else:
            token_buff +=" "
        print(word_segment)
    return word_segment
#print(word_segmenting(query))

for i in range(10):
    file_path = f'/Users/hieudao/Desktop/nlo_assigmenp/Input/input_{i}.txt'
    file = open(file_path, 'r')
    
    query = file.readline()
    print(word_segmenting(query))
    new_f = open(f"/Users/hieudao/Desktop/nlo_assigmenp/word_segment/word_segment_{i}.txt", "w")
    new_f.write(str(word_segmenting(query)))
    new_f.close()
    file.close()
   # i+=1
