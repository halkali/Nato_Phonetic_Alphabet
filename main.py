import pandas

p = pandas.read_csv('nato_phonetic_alphabet.csv')
df = pandas.DataFrame(p)


dict2 = {value.letter:value.code for (index,value) in df.iterrows()}


word = input("the word:").upper()

the_list = [dict2.get(i) for i in word if i in dict2.keys()]

print(the_list)




