with open('words.txt','r') as file:
    content = file.read()

letter_count =sum(1 for char in content if char.sisalpha())

print("total number = ",letter_count)
