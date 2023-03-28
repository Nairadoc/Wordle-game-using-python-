# Wordle-game-using-python-
Making the classic wordle game in python with help of Rich library (with custom themes and a spalsh screen!)

Libaraies used:

Rich library- To add color for wordle feedback and make a pretty display 
Pathlib- For linking the path to wordlists
Random- To select random word from wordlist
String- For getting ascii_letters

Structure of code:

1. Splash screen (How to play wordle-Instructions):
Wordle is word guessing game. Player gets six attempts to guess a secret five-letter word.
After each guess, player will get feedback about which letters are correctly placed (colored green), which are misplaced (colored yellow), and which are wrong (colored gray).

2. Theme Selection(Classic or custom themes): 
I decided to add a few custom wordlists apart from the classic wordle list. The friends theme has all the words related to the tv show friends, the main difference here is that now the words can be more than 5 letters (eg: Chadler) or less than 5 letters too (eg: Ross). You can add your own custom themes as well! I have added space for a third custom theme (named book theme), you can add your own flare to a wordlist and use that space!

3. Actual game:
Then comes the actual game, formated using rich. 
