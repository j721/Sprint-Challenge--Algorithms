'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


# U
#takes in word as parameter, must return a count (need a counter that will increment at +1)
#look for words that contain the "th" string
#going to assume word is similar to an array that has indices to be able to search for "th" within it

#use recursion to call the function within itself



# P

#for count, see if it could be passed in as a parameter and set to default of 0. To initialize the counter
#def count_th(word, count =0):
#conditions to consider
#word needs at least the two letters "th"
#if the word contains less than or equal to 1 letter then just return back the empty count of 0

#if the word contains at least two letters, with th in its index then 
#return the count back incremented by count +1

#lastly, we need to call our recursion in our last return statement that will return our parameters of word and count

# E
#how to make sure word array contains the string "th" in it?
# "th" has to exist in the index of the word array, use slicing method?

# R#


# def count_th(word, count = 0):
#     #if length of word has 1 or 0 letters then return count 0 value
#     if len(word) <= 1:
#         return count
#     #if the first two letters is found in the word array then add count +1
#     if word[:2] =="th":
#         count +=1
#     #call function recursively to return the first index, and the count as well
#     return count_th(word[1:], count)


#2nd method
def count_th(word):
    #if length of word has less than 2 letters then return 0
    if len(word) < 2:
      return 0
    #else if the first two letters has th in its index 
    #then return +1 for the count_th function and count that as the first index 
    elif word[0:2] == 'th':
        return 1 + count_th(word[1:])
    #else no 'th' letters found, then just return the count_th function 
    else:
        return count_th(word[1:])
