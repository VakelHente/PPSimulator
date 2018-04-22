"""
File which contain all settings parameter used in application
"""
import os
import sys
from enum import IntEnum

try:
    from util_lib.utilityYml import getYmlDict
    from util_lib.utilityDict import dictToObj
    from util_lib.utilityDict import ObjectDict
except ImportError as error:
    print(error)
    # Indicate to Error code
    sys.exit(102)

# Global variables
_appDir = _protocolDir = _graphDir = _resultDir = None

class Settings(ObjectDict):
    pass

def init():
    global _appDir, _protocolDir, _graphDir, _resultDir
    _appDir = os.path.dirname(os.path.realpath(__file__))

    orderDict = getYmlDict("\\".join([_appDir, "settings.yml"]))

    settings = dictToObj(Settings, orderDict)
    try:
        _protocolDir = settings.directories.protocol
        _graphDir    = settings.directories.graph
        _resultDir   = settings.directories.result
    except AttributeError as e:
        print(e)

class ErrorCode(IntEnum):
    INVALID_PARAM               = 100
    UNSUPPORTED_REPOSITORY      = 101
    ERROR_IMPORT                = 102
    REPOSITORY_PATH_NOT_EXIST   = 103
    CALLED_PROCESS_ERROR        = 104
    INVALID_FILE                = 105

if __name__ == "__main__":
    init(False)