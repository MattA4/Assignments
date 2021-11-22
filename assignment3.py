print('You will be asked for an adjective, a noun, an animal, and a place. These will be used to fill in a story template, which will then be printed with your inputs at the end')

with open('mltemp.txt','r') as file:
  for line in file: #Creates loop to run through all lines of the txt doc
    line = line.split(" ")
    adj = input('Enter an adjective: ')
    noun = input('Enter a noun: ')
    animal = input('Enter an animal: ')
    place = input('Enter a place: ')
    print(line[0], line[1], adj, line[2], line[3], noun, line[4], line[5], animal, line[6], line[7], line [8], line[9], line[10], place)
    break #exits the loop once done