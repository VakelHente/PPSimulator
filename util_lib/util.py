import sys

try:
    from colorama import Fore
    from colorama import Style
    import settings
except ImportError as error:
    print("{} {} {}".format(Fore.RED, error, Fore.RESET))
    sys.exit(settings.ErrorCode.ERROR_IMPORT.value)

def printBrightGreenRefresh(text):
    """
    Print provided text on bright green with flush last printed line.

    @param text : String to print
    @return     : None
    """
    print("\r{}{} {}{}".format(Fore.GREEN, Style.BRIGHT, text, Style.RESET_ALL), end='', flush=True)

def printRed(text):
    """
    Print provided string on red.

    @param text : String to print
    @return     : None
    """
    print("{} {}{}".format(Fore.RED, text, Fore.RESET))

def printYellow(text):
    """
    Print provided string on yellow.

    @param text : String to print
    @return     : None
    """
    print("{} {}{}".format(Fore.YELLOW, text, Fore.RESET))

def printBrightGreen(text):
    """
        Print provided string on red.

        @param text : String to print
        @return     : None
        """
    print("{}{} {}{}".format(Fore.GREEN, Style.BRIGHT, text, Fore.RESET))

if __name__ == "__main__":
    pass
