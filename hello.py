import sys
from termcolor import colored, cprint

text = colored ('Hello world', 'red', attrs=['reverse', 'blink'])
print (text)

#cprint('Hello, World', 'green', 'on_red')