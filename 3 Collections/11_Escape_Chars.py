print("Vignesh is working \n  hard to live life")

print("Vignesh is Learning \"Python\" to learn programming")      ### backward \ used to escape the special meanings
print("Vignesh is Learning \"Python\" to learn programming\\")    ### To print \ if it's confuse with escape then we need to use double \\ slash

""""
- the char has special functionality called escape chars
\n --> New Line
\k --> Horizontal tab
\r --> Carrige return (come back to Beginning of line )
\b --> backspace to delete one char
\f --> form feed    go to next page
\' --> To Print  single quote
\" -->  To Print double quote
\\ --> To Print Back slash

"""
from shlex import quote

print("VigneshLearning")
print(20*"#")
print("Vignesh\tLearning")
print(20*"#")
print("Vignesh\nLearning")
print(20*"#")
print('This is \' single quote symbol' )
print(20*"#")
print('This is \"  double  quote symbol' )
print(20*"#")
print('This is \\  back slash symbol' )

                                                                                                             