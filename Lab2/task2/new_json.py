import inspect
import re


class JSONEncoder(object):
    def to_json(self, obj):
        if type(obj) in (int, float, long):
            return str(obj)
        elif type(obj) in (list, set, frozenset, tuple):
            return self.__iterable_to_json(obj)
        elif type(obj) == dict:
            return self.__dict_to_json(obj)
        elif type(obj) in (str, unicode, basestring):
            return self.__string_to_json(obj)
        elif type(obj) == bool:
            return self.__bool_to_json(obj)
        elif obj is None:
            return "null"
        else:
            return self.__object_to_json(obj)

    def __object_to_json(self, source_object):
        def attributes_filter(attribute):
            attribute_name = attribute[0]
            attribute_value = attribute[1]
            is_func = hasattr(attribute_value, "__call__")
            is_builtin = attribute_name[:2] == "__"
            return not (is_func or is_builtin)

        attributes = filter(attributes_filter, inspect.getmembers(source_object))
        object_dict = dict(attributes)
        return self.__dict_to_json(object_dict)

    def __dict_to_json(self, source_dict):
        result = "{"
        for key, value in source_dict.items():
            result += self.__quotes_wrap(key) + ":"
            result += self.to_json(value) + ","
        result = result[:-1] + "}"
        return result

    def __iterable_to_json(self, source_iterable):
        result = "["
        for item in source_iterable:
            result += self.to_json(item) + ","
        result = result[:-1] + "]"
        return result

    def __bool_to_json(self, value):
        return "true" if value else "false"

    def __string_to_json(self, string):
        return self.__quotes_wrap(string)

    def __quotes_wrap(self, string):
        return '"{}"'.format(string)


class JSONDecoder(object):
    def from_json(self, txt):
        string = txt.strip()

        if string == "null":
            return None

        if string in ["true", "false"]:
            return string == "true"

        if string[0] == '{' and string[-1] == '}':
            return self.__dict_from_json(string)

        if string[0] == '[' and string[-1] == ']':
            return self.__list_from_json(string)

        if string[0] == "'" and string[-1] == "'":
            return string[1:-1]

        try:
            number = float(string)
            try:
                number = int(string)
                return number
            except ValueError:
                return number
        except ValueError:
            print('Value error: {}'.format(string))

    def __dict_from_json(self, string):
        content = string[1:-1] + ","
        result_dict = dict()
        if content == ",":
            return result_dict
        last = first = counter = 0
        for item in content:
            if item in ["{", "["]:
                counter += 1
            elif item in ["}", "]"]:
                counter -= 1
            elif item == ",":
                if counter:
                    return
                element = content[first:last]
                first = last + 1
                attrs = element.split(":", 1)
                attr_in = attrs[0].strip()
                if not (attr_in[0] == "'" and attr_in[-1] == "'"):
                    raise ValueError('Invalid Key name: {}'.format(attrs[0]))
                result_dict[self.from_json(attrs[0])] = self.from_json(attrs[1])
            last += 1
        return result_dict

    def __list_from_json(self, string):
        content = string[1:-1] + ","
        result_list = list()
        if content == ",":
            return result_list
        last = first = counter = 0
        for item in content:
            if item in ["{", "["]:
                counter += 1
            elif item in ["}", "]"]:
                counter -= 1
            elif item == ",":
                if counter:
                    return
                element = content[first:last]
                first = last + 1
                result_list.append(self.from_json(element))
            last += 1
        return result_list
