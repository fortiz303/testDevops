input_upper = input('write the word hola: ')
print(input_upper.upper())

input_count = input('Input any word:')
print("the letter 'a' appears {} times".format(input_count.count('a')))

input_strip = input("input a word with 'est' as the suffix (eg. 'smallest', 'biggest'): ")
print(input_strip.strip('est'))

input_join = input("Type some words and watch 'em join! : ")
print(input_join.join(input_join))

