class MetaClass(type):
    def __new__(mcs, name, bases, attrs):
        if "file_name" in attrs:
            with open(attrs["file_name"], "r") as file_input:
                for attr in file_input.read().split(','):
                    splited_attr = attr.split('=')
                    attrs[splited_attr[0]] = splited_attr[1]
        return super(MetaClass, mcs).__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        super(MetaClass, cls).__init__(name, bases, attrs)
