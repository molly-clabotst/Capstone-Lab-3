def camel_case(sentence):
    
    sentence = sentence.strip()        
    words = sentence.split(" ")

    if set(words).issubset("U+"):
        smush = join(words)
        return smush
    
    # specific solution in credit to: https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension#4260304
    changedWords = [word.title() if words.index(word)!=0 else word.lower() for word in words]
    changedWords

    camelCat = join(changedWords)
    
    return camelCat

def join(changedWords):
    camelCat = ''

    for word in changedWords:
        camelCat+=word

    return camelCat

def main():
    sentence = input('Please write a sentence ')
    print(camel_case(sentence))

if __name__ == '__main__':
    main()