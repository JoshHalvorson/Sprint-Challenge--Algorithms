'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if 'th' not in word:
        return 0
    # finds the index of the first th in the word, and adds 2 for the next recursive call 
    # so that its only searching from after the last th found to the rest of the word
    # ex: 'thhelthloth' would be  'helthloth' then 'loth'
    return 1 + count_th(word[word.find('th') + 2:])

if __name__ == '__main__':
    # to run from console, enter 'python count_th.py' and enter a word when it prompts
    word = input('Enter a word: ')
    print(count_th(word))