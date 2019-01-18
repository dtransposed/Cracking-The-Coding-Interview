import time

def join_words(list_words):
    sentence = ""
    for word in list_words:
        sentence = sentence + word

    return sentence

def join_words_v2(list_words):
    sentence = []
    for word in list_words:
        sentence.append(word)

    return sentence


def generate_list_words(no_words, string):
    list_words = []
    for _ in range(no_words):
        list_words.append(string)
    return list_words

list_words = generate_list_words(100000, 'WuTangClan')

start = time.time()
join_words(list_words)
end = time.time()
print('Naive implementation runtime: {}'.format(end-start))
start = end
join_words_v2(list_words)
end = time.time()
print('Smarter implementation runtime: {}'.format(end-start))

