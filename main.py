def count_word(file_path,word):
    file = open(file_path,"r")
    #content = file.read()
    #word_count = content.count(word)

    return file.read().count(word)
print(count_word("file.txt","hello"))