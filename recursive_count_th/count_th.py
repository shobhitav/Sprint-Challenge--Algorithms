'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Base case
    if 'th' not in word:
        return 0
    # Checking if substring 'th' matches in beginning of word
    elif  word[0:2] == 'th':
        return 1+count_th(word[2:])
    else:
        # otherwise recurse and  check for remaining index
        return count_th(word[1:])

print(count_th('theth')) 
