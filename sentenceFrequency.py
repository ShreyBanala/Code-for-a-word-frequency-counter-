
import string 

def main():
    enter_sentence= input("Type sentence here : " )
    list_of_words=enter_sentence.split()
    clean_words=[]
    frequency_counter= dict()
    unique_words=set()
    for index in range(len (list_of_words)):
        local_s=list_of_words[index]
        translator = str.maketrans('', '', string.punctuation)
        clean_text = local_s.translate(translator)
        clean_words.append(clean_text)
    for index in range(len(clean_words)):
        frequency_counter[clean_words[index]]=clean_words.count(clean_words[index])
        unique_words.add(clean_words[index])
	
    for word in frequency_counter:
        print("Word is: ", word, " and it appears: ", frequency_counter[word] , " times")

    print("All unique words: ")
    for unique in unique_words:
        print(unique)

if __name__ == "__main__":
    main()
	