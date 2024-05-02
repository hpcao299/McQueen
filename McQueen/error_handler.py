from McQueen.colors import R, G, BOLD, RESET

def handle(error: str = None, label: str = None):
    print()
    print(f'{R}[{G}+{R}]{RESET} {label if label else "There Is A Problem"}{RESET}')

    print()
    print(f'{R}[{G}01{R}]{RESET} Check The Connection{RESET}')
    print(f'{R}[{G}02{R}]{RESET} Check If The Input Is Correct{RESET}')
    print(f'{R}[{G}03{R}]{RESET} Website May Be Unavailable{RESET}')

    if error: 
        print(f'\n{R}{BOLD}[error]{RESET} {error}')