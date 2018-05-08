import sys

try:
    import settings as st
    from util_lib.utilityPrint import printRed
    from util_lib.utilityDict import ObjectDict
except ImportError as error:
    printRed(error)
    sys.exit(st.ErrorCode.ERROR_IMPORT)

class Protocol(ObjectDict):
    pass
