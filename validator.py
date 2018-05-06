import sys

try:
    from util_lib.utilityPrint import printRed
    import settings as st
    from exceptions import ProtocolItemError
    import re
except ImportError as error:
    printRed(error)
    sys.exit(st.ErrorCode.ERROR_IMPORT)


class SwitchPP(object):
    def switchCase(self, attributeChecker):
        """
        Dispatch method to check correctness of Population protocol obj.

        @param attributeChecker : Attribute to check of the population protocol obj
        @return                 : Method to check specific attribute
        """
        method = getattr(self, attributeChecker, lambda _: False)
        return method

    def name(self, ppObj):
        """
        Check if the name attribute is valid.

        @param ppObj     : Population protocol obj
        @param attribute : Attribute of the population protocol obj
        @return          : True if the attribute is valid otherwise False
        """
        try:
            name = getattr(ppObj, "name")
            if name.strip() != "":
                return True
            else:
                printRed("Missing name's key.")
                return False
        except AttributeError as error:
            printRed(error)
            return False

    def protocolType(self, ppObj):
        """
        Check if the protocolType is valid.

        @param ppObj : Population protocol obj
        @return      : True if the attribute is valid otherwise False
        """
        try:
            protocolType = getattr(ppObj, "protocolType")
            strippedProtocolType = protocolType.strip()
            if strippedProtocolType == "Leader Election":
                return True
            elif strippedProtocolType == "Leader Election":
                return True
            elif strippedProtocolType == "":
                printRed("Missing protocolType's key.")
                return False
            else:
                printRed("Unsupported protocol Type.")
                return False
        except AttributeError as error:
            printRed(error)
            return False

    def input(self, ppObj):
        """
        Check if the input is valid.

        @param ppObj : Population protocol obj
        @return      : True if the attribute is valid otherwise False
        """
        try:
            input = getattr(ppObj, "input")
            if isinstance(input, list):
                if not len(input) > 0:
                    printRed("List of inputs does not contain single input.")
            else:
                printRed("Input does not contain list of inputs")
                return False
        except AttributeError as error:
            printRed(error)
            return False
        return True

    def states(self, ppObj):
        """
        Check if the states is valid.

        @param ppObj : Population protocol obj
        @return      : True if the attribute is valid otherwise False
        """
        try:
            states = getattr(ppObj, "states")
            if isinstance(states, list):
                if not len(states) > 0:
                    printRed("List of states does not contain single state.")
            else:
                printRed("States does not contain list of states")
                return False
        except AttributeError as error:
            printRed(error)
            return False
        return True

    def output(self, ppObj):
        """
        Check if the output is valid.

        @param ppObj : Population protocol obj
        @return      : True if the attribute is valid otherwise False
        """
        try:
            output = getattr(ppObj, "output")
            if isinstance(output, list):
                if not len(output) > 0:
                    printRed("List of outputs does not contain single output.")
            else:
                printRed("Outputs does not contain list of outputs")
                return False
        except AttributeError as error:
            printRed(error)
            return False
        return True

    def inputFunction(self, ppObj):
        """
        Check if the input function is valid.

        @param ppObj : Population protocol obj
        @return      : True if the attribute is valid otherwise False
        """
        try:
            inputFunction = getattr(ppObj, "inputFunction")
            for function in inputFunction:
                firstElem, secondElem = self.findXYQBetween(function)
                input = getattr(ppObj, "input")
                states = getattr(ppObj, "states")
                if firstElem not in input:
                    raise ProtocolItemError(function, "inputFunction")
                if secondElem not in states:
                    raise ProtocolItemError(function, "inputFunction")
        except AttributeError as error:
            printRed(error)
            return False
        except ProtocolItemError as error:
            printRed(error)
            return False
        return True

    def statesFunction(self, ppObj):
        """
        Check if the states function is valid.

        @param ppObj : Population protocol obj
        @return      : True if the attribute is valid otherwise False
        """
        try:
            inputFunction = getattr(ppObj, "statesFunction")
            for function in inputFunction:
                initiator, responder = self.findQQ_QQBetween(function)
                states = getattr(ppObj, "states")
                # TODO different finding.
                for i in range(2):
                    if initiator[i] and responder[i] not in states:
                        raise ProtocolItemError(function, "statesFunction")
        except AttributeError as error:
            printRed(error)
            return False
        except ProtocolItemError as error:
            printRed(error)
            return False
        return True

    def outputFunction(self, ppObj):
        """
        Check if the output function is valid.

        @param ppObj : Population protocol obj
        @return      : True if the attribute is valid otherwise False
        """
        try:
            inputFunction = getattr(ppObj, "outputFunction")
            for function in inputFunction:
                firstElem, secondElem = self.findXYQBetween(function)
                states = getattr(ppObj, "states")
                output = getattr(ppObj, "output")
                if firstElem not in states:
                    raise ProtocolItemError(function, "outputFunction")
                if secondElem not in output:
                    raise ProtocolItemError(function, "outputFunction")
        except AttributeError as error:
            printRed(error)
            return False
        except ProtocolItemError as error:
            printRed(error)
            return False
        return True

    def findXYQBetween(self, string):
        """
        Find elements of the set.

        @param string   : Function
        @return         : Two element of the set if correct otherwise False
        """
        elemSet = re.findall("{}([a-zA-Z0-9]+){}".format(re.escape('('), re.escape(')')), string)
        if len(elemSet) != 2:
            raise ProtocolItemError(string)
        return elemSet[0], elemSet[1]

    def findQQ_QQBetween(self, string):
        """
        Find double states of the set.

        @param string   : Function
        @return         : Two element of the set if correct otherwise False
        """
        initiator = re.findall("{}([a-zA-Z0-9]+){}".format(re.escape('('), re.escape(',')), string)
        responder = re.findall("{}([a-zA-Z0-9]+){}".format(re.escape(','), re.escape(')')), string)
        if len(initiator) != 2 or len(responder) != 2 :
            raise ProtocolItemError(string)
        return initiator, responder