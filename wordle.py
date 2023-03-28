import pathlib
import random
from string import ascii_letters, ascii_uppercase

from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
from rich.prompt import Prompt
console = Console(theme=Theme({"warning": "black on yellow"}))

def refresh(title,guesses,word):
    console.clear()
    console.rule(f"[bold] {title} [/]\n")
    print(word)  #Here for convinience when explaining or fixing bugs, not to be used in actual game
    check_guess(guesses, word)
    
def how_to():
    console.clear()
    console.rule("[bold blue on white] How to play Wordle:[/]") 
    console.print("[bold blue]Guess the word in 6 guesses![/]\n")
    console.print("->Each guess must be a valid 5-letter word.\n\n->The color of the tiles will change to show how close your guess was to the word.\n\n")

    console.print(Panel("[black]Example:[/]\n\n->[bold white on green]W[/][bold white on #666666]EA[bold white on yellow]R[/]Y[/]\n\n[bold green]W[/] is in the word and in [green]correct[/] spot\n[bold yellow]R[/] is in the word but in [yellow]wrong[/] spot\n[bold #666666]E, A and Y[/] are [bold black]NOT[/] in the word in any spot",width=50))

    console.print("[red]Press Enter to start the game[/]")
    if input():
        return

def select_theme():
    global WORDLIST
    global TOTAL_GUESSES
    global LETTER_LENGTH
    console.clear()
    console.print("[bold white]Select Theme:\n\n\n1.[yellow] Classic Wordle[/]\n\n2.[purple] Friends[/] Theme\n\n3.[red] Book [/]Theme\n\n[/]")
    ch=input("Enter choice: ")
    if ch=='1':
        WORDLIST=pathlib.Path("wordlist.txt")
        word=get_random_word(('c',5))
        TOTAL_GUESSES=6
    elif ch=='2':
        WORDLIST=pathlib.Path("friendschar.txt")
        word=get_random_word()
        TOTAL_GUESSES=4
    elif ch=='3':
        WORDLIST=pathlib.Path("words.txt")
        word=get_random_word()
        TOTAL_GUESSES=6
    else:
        console.print("Enter valid output\n")
        select_theme()
    LETTER_LENGTH=len(word)
    return word

def get_random_word(theme=('c',5)):
    if theme[0]=='c':
        word_len=theme[1]
        words = [word.upper() 
        for word in WORDLIST.read_text(encoding='utf-8').strip().split('\n') if len(word)==word_len]
    else:
        words = [word.upper() 
        for word in WORDLIST.read_text(encoding='utf-8').strip().split('\n')]
    return random.choice(words)
    
def check_guess(guesses,word):
    keyboard={'Q':'Q','W':'W','E':'E','R':'R','T':'T','Y':'Y','U':'U','I':'I','O':'O','P':'P\n','A':'A','S':'S','D':'D','F':'F','G':'G','H':'H','J':'J','K':'K','L':'L\n','Z':'Z','X':'X','C':'C','V':'V','B':'B','N':'N','M':'M'}
    for guess in guesses:
        styled_guess=[]
        word_set=set(word)
        for guess_letter,word_letter in zip(guess,word):
            if(guess_letter==word_letter):
                style="black on green"
            elif(guess_letter in word_set):
                style="black on yellow"
            elif(guess_letter in ascii_letters):
                style="white on #666666"
            else:
                style="dim"
            if guess_letter != "_":
                if (guess_letter == 'P') or (guess_letter=='L'):
                    keyboard[guess_letter.upper()] = f"[{style}]{guess_letter.upper()}\n[/]"
                else:
                    keyboard[guess_letter.upper()] = f"[{style}]{guess_letter.upper()}[/]"
            styled_guess.append(f"[{style}]{guess_letter}[/]")
        console.print("".join(styled_guess),justify="center")
    console.print("\n"+" ".join(keyboard.values()), justify="center")


def game_over(word,guesses,guessed_correctly):
    refresh(f"[red] Game over![/]",guesses,word)

    if guessed_correctly:
        console.print(Panel(f"[green]Correctly guessed!\nThe word was[/][red] {word}[/]"),justify='left')
    else:
        console.print(Panel(f"You've run out of guesses!\nThe word was[red] {word}[/]"),justify='left')


def main():
    guessed_correctly=False
    how_to()
    word=select_theme()
    guesses=["_"*LETTER_LENGTH+"\n"]*TOTAL_GUESSES
    refresh(f"[red]Guess the word![/]",guesses,word)
    for guess_count in range(0,TOTAL_GUESSES):
        guesses[guess_count]= guess_word(guess_count,prev_guess=guesses[:guess_count])
        refresh(f"[blue] Guess {guess_count+1}[/]",guesses,word)
        if guesses[guess_count]==word:
            guessed_correctly=True            
            break
    game_over(word,guesses,guessed_correctly)
        
def guess_word(guess_count,prev_guess):
    guess=Prompt.ask(f"\nGuess {guess_count+1} ").upper()

    if guess in prev_guess:
        console.print(f"You've already guessed [red]{guess}[/]",style="warning")
        return guess_word(guess_count, prev_guess)

    if len(guess)!=LETTER_LENGTH:
        console.print(f"Your guess must be {LETTER_LENGTH} letters",style="warning")
        return guess_word(guess_count, prev_guess)

    return guess
    
if __name__ == "__main__":
    main()