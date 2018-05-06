import os
import yaml
from collections import OrderedDict

currentFilePath = os.path.dirname(os.path.realpath(__file__))

class IndentDumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)

def orderedLoad(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    """

    @param stream            :
    @param Loader            :
    @param object_pairs_hook :
    @return                  :
    """
    class OrderedLoader(Loader):
        pass
    def construct_mapping(loader, node):
        """

        @param loader   :
        @param node     :
        @return         :
        """
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)

def orderedDump(data, stream=None, Dumper=yaml.Dumper, **kwds):
    """
    Extended yaml dump to make dump for ordered dict and with increased indent.

    @param data     : Ordered dict
    @param stream   : Stream
    @param Dumper   : Dumper class
    @param kwds     : rest arguments
    @return         : YAML stream or string if stream is None.
    """
    def _dictRepresenter(dumper, data):
        """
        Extended Dumper for processing OrderedDict obj.
        """
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            data.items())
    IndentDumper.add_representer(OrderedDict, _dictRepresenter)
    return yaml.dump(data, stream, IndentDumper, **kwds)

def createYmlFile(name, data, path=currentFilePath, ext="yml"):
    """
    Create yml file from provided data.

    @param name     : Name of file where data will be saved
    @param data     : Ordered dict or simple dict data
    @param path     : Path where to save yml file (Default path of utilityYml.py file)
    @param ext      : Extension of file (Default "yml")
    @return         : None
    """
    # TODO: add path to create file

    with open("{}\\{}.{}".format(path, name, ext), 'w') as file:
        orderedDump(data, file, Dumper=yaml.SafeDumper, default_flow_style=False, explicit_start=True)

def getYmlDict(ymlFile):
    """
    Get dictionary from provided file.

    @ymlFile    : File in yml format
    @return     : Parsed Dict
    """
    with open(ymlFile, 'r') as file:
        data = file.readlines()
        return orderedLoad("".join(data))

def getYmlString(data):
    """
    Get yml string from provided data

    @param data : Ordered dict or simple dict data
    @return     : Yml string
    """
    return orderedDump(data, Dumper=yaml.SafeDumper, default_flow_style=False, explicit_start=True)

if __name__ == "__main__":
    aaa = {"name": "configuration", "check": 1, "dupa": ["safdsafsda", 1, 2, "dfasasd"]}
    aaOrder = OrderedDict([("name", "configuration"), ("check", 1), ("dupa", ["safdsafsda", 1, 2, "dfasasd"])])
    od = OrderedDict(
        [
            (u'name', u'Alice'),
            (u'ID', OrderedDict(
                [
                    (u'type', u'card'),
                    (u'nr', u'123')
                ]
            )),
            (u'name', u'Bob'),
            (u'ID', OrderedDict(
                [
                    (u'type', u'passport'),
                    (u'nr', u'567')
                ]
            ))
        ]
    )
    aa = [
            (u'name', u'Alice'),
            (u'ID', OrderedDict(
                [
                    (u'type', u'card'),
                    (u'nr', u'123')
                ]
            )),
            (u'name', u'Bob'),
            (u'ID', OrderedDict(
                [
                    (u'type', u'passport'),
                    (u'nr', u'567')
                ]
            )),
        ]
    order = OrderedDict(aa)
    # print(yaml.dump(range(5), default_flow_style=False))
    createYmlFile("xyz", od)