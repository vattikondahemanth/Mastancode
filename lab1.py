############################  9.5  Start #############################
"""


'''
D R E X E L   U N I V E R S I T Y
ENGR 131 -- Introductory Programming for Engineers

Acronym generator with special morpheme support

Written by Your Name Here
Term:  Winter 2020-2021
'''

def generate_acronym(input_phrase, special_morphemes = {}):
    if not input_phrase or not input_phrase.split():
        return
    words = input_phrase.split()
    acronym = []
    for word in words:
        if special_morphemes and word in special_morphemes.keys():
            acronym.append(special_morphemes[word])
        else:
            acronym.append(word[0]) 
    acronym = ''.join(acronym)
    return acronym

if __name__ == '__main__':
    input_phrase = str(input('Please input the string \n'))
    example_special_morphemes = {'Chemical':'CH','Exchange':'EX','You':'U'}
    acronym = generate_acronym(input_phrase,special_morphemes=example_special_morphemes)
    print(acronym)



"""
##########################  9.5 End   ###################


#########################  10.29 Start ##################

"""

input_integers = input('Please enter the list of integers \n')
bound_values = input('Please enter the lower and upper bound seperated by Space\n')
input_integers = input_integers.split()
bound_values = bound_values.split()

for i in input_integers:
    if i >= bound_values[0]  and i <= bound_values[1]:
        print(i)


"""

#######################  10.29  End #####################



#######################  10.32 Start  ###################

"""

words = input('Enter the original word and replacement word \n').split()
sentence = input('Enter the Sentence to modify \n')
for i in range(0,len(words),2):
    new_sentence = sentence.replace(words[i], words[i+1])
    sentence = new_sentence
print(new_sentence)

"""

####################  10.32 End     #################