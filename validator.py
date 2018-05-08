import sys

try:
    from util_lib.utilityPrint import printRed
    import settings as st
    from exceptions import ProtocolItemError
    import re
except ImportError as error:
    printRed(error)
    sys.exit(st.ErrorCode.ERROR_IMPORT)


class SwitchPpG(object):
    def switchCase(self, attributeChecker):
        """
        Dispatch method to check correctness of Population protocol or graph obj.

        @param attributeChecker : Attribute to check of the population protocol obj
        @return                 : Method to check specific attribute
        """
        method = getattr(self, attributeChecker, lambda _: False)
        return method

    def name(self, obj):
        """
        Check if the name attribute is valid.

        @param obj       : Population protocol or graph obj
        @return          : True if the attribute is valid otherwise False
        """
        try:
            name = getattr(obj, "name")
            if name.strip() != "":
                return True
            else:
                printRed("Missing name's key.")
                return False
        except AttributeError as error:
            printRed(error)
            return False

    def protocolType(self, obj):
        """
        Check if the protocolType is valid.

        @param obj   : Population protocol or graph obj
        @return      : True if the attribute is valid otherwise False
        """
        try:
            protocolType = getattr(obj, "protocolType")
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

    def input(self, obj):
        """
        Check if the input is valid.

        @param obj   : Population protocol or graph obj
        @return      : True if the attribute is valid otherwise False
        """
        try:
            input = getattr(obj, "input")
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

    def states(self, obj):
        """
        Check if the states is valid.

        @param obj   : Population protocol or graph obj
        @return      : True if the attribute is valid otherwise False
        """
        try:
            states = getattr(obj, "states")
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

    def output(self, obj):
        """
        Check if the output is valid.

        @param obj   : Population protocol or graph obj
        @return      : True if the attribute is valid otherwise False
        """
        try:
            output = getattr(obj, "output")
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

    def inputFunction(self, obj):
        """
        Check if the input function is valid.

        @param obj   : Population protocol or graph obj
        @return      : True if the attribute is valid otherwise False
        """
        try:
            inputFunction = getattr(obj, "inputFunction")
            for function in inputFunction:
                firstElem, secondElem = self.findXYQBetween(function)
                input = getattr(obj, "input")
                states = getattr(obj, "states")
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

    def statesFunction(self, obj):
        """
        Check if the states function is valid.

        @param obj   : Population protocol or graph obj
        @return      : True if the attribute is valid otherwise False
        """
        try:
            inputFunction = getattr(obj, "statesFunction")
            for function in inputFunction:
                initiator, responder = self.findQQ_QQBetween(function)
                states = getattr(obj, "states")
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

    def outputFunction(self, obj):
        """
        Check if the output function is valid.

        @param obj   : Population protocol or graph obj
        @return      : True if the attribute is valid otherwise False
        """
        try:
            inputFunction = getattr(obj, "outputFunction")
            for function in inputFunction:
                firstElem, secondElem = self.findXYQBetween(function)
                states = getattr(obj, "states")
                output = getattr(obj, "output")
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

    def numberNodes(self, obj):
        """
        Check if the number nodes is valid.

        @param obj  : Population protocol or graph obj
        @return     : True if the attribute is valid otherwise False
        """
        try:
            numberNodes = getattr(obj, "numberNodes")
            if int(numberNodes.strip()) > 1:
                return True
            else:
                printRed("Number of nodes must be higher than 1.")
                return False
        except AttributeError as error:
            printRed(error)
            return False
        except ValueError as error:
            printRed(error)
            return False

    def agent(self, obj):
        """
        Check if the agent is valid.

        @param obj  : Population protocol or graph obj
        @return     : True if the attribute is valid otherwise False
        """
        try:
            name = getattr(obj, "agent")
            if isinstance(name, list):
                numberNodes = getattr(obj, "numberNodes")
                if len(name) == int(numberNodes.strip()):
                    return True
                else:
                    printRed("Number of nodes and agents must be equal.")
                    return False
            else:
                printRed("Number of agents must be higher than 1.")
                return False
        except AttributeError as error:
            printRed(error)
            return False
        except ValueError as error:
            printRed(error)
            return False

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
        if len(initiator) != 2 or len(responder) != 2:
            raise ProtocolItemError(string)
        return initiator, responder