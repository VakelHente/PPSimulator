import subprocess
import shlex
import sys

try:
    import settings
    from util_lib.utilityPrint import printRed
except ImportError as error:
    printRed(error)
    sys.exit(settings.ErrorCode.ERROR_IMPORT)

def processCommand(command, cwd):
    """
    Function to process provided command in case of fail print appropriate message.

    @param command  : command with concatenated arguments in single string
    @cwd            : current working directory
    @return         : output of executed command
    """
    try:
        subprocess.check_output(shlex.split(command), stderr=subprocess.STDOUT, cwd=cwd, shell=True)
        return True
    except subprocess.CalledProcessError as error:
        printRed(error.output.decode("utf-8"))
        printRed(error)
        return False


if __name__ == "__main__":
    pass