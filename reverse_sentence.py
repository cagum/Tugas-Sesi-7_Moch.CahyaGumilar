# Mochammad Cahya Gumilar
# 20220040116
# TI22B

# sentence = input("Balikkan Kalimat : ")

def reverse_sentence(sentence):
    reversed_sentence = ""
    for i in range(len(sentence)-1,-1,-1):
        reversed_sentence += sentence[i]

    return reversed_sentence

while True:
    sentence = input('Balikkan Kata : ')
    if sentence == 'exit':
        break
    
    hasil = reverse_sentence(sentence)
    print(hasil)


