first_word_list = list(input("Enter the 1st string: "))
second_word_list = list(input("Enter the 2nd string: "))

print("\nIs an anagram.") if first_word_list.sort() == second_word_list.sort() else print("\nNot an anagram.")