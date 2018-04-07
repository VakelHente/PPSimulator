import sys
import os

try:
    from colorama import Fore
    from colorama import Style
    import settings
except ImportError as error:
    print("{} {} {}".format(Fore.RED, error, Fore.RESET))
    sys.exit(settings.ErrorCode.ERROR_IMPORT.value)

def getBrightGreenString(text):
    """
    Color provided string on bright green.

    @param text : String to color
    @return     : Colored string
    """
    return "{}{} {}{}".format(Fore.GREEN, Style.BRIGHT, text, Fore.RESET)

def getRedString(text):
    """
    Color provided string on red.

    @param text : String to color
    @return     : Colored string
    """
    return "{} {}{}".format(Fore.RED, text, Fore.RESET)

def getYellowString(text):
    """
    Color provided string on yellow.

    @param text : String to color
    @return     : Colored string
    """
    return "{} {}{}".format(Fore.YELLOW, text, Fore.RESET)

def printBrightGreen(text):
    """
    Print provided string on bright green.

    @param text : String to print
    @return     : None
    """
    print(getBrightGreenString(text))

def printBrightGreenRefresh(text):
    """
    Print provided text on bright green with flush last printed line.

    @param text : String to print
    @return     : None
    """
    print(getBrightGreenString(text), end='', flush=True)

def printRed(text):
    """
    Print provided string on red.

    @param text : String to print
    @return     : None
    """
    print(getRedString(text))

def printYellow(text):
    """
    Print provided string on yellow.

    @param text : String to print
    @return     : None
    """
    print(getYellowString(text))

def disableEnablePrint(isDebug=False):
    """
    Depends on bool argument (isDebug) disable or enable print to output.

    @param debug : Bool to disable or enable print.
    @return      : None
    """
    if isDebug:
        sys.stdout = sys.__stdout__
    else:
        sys.stdout = open(os.devnull, 'w')

if __name__ == "__main__":
    pass
