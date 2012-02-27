import re


class Converter():
    def __init__(self, from_exp, to_exp):
        self.from_re = [re.compile(from_exp.replace("*", "(.*)"))]
        self.to_exp = []

        if self._is_formatter(to_exp):
            self.from_re.append(re.compile(to_exp.replace("*", "(.*)")))
            self.to_exp.append(self._pattern_to_formatter(to_exp))
            self.to_exp.append(self._pattern_to_formatter(from_exp))
        else:
            self.to_exp.append(to_exp)

    def convert(self, path):
        idx = 0
        while idx < len(self.from_re):
            match = self.from_re[idx].match(path)
            if match: return self.to_exp[idx].format(*match.groups())
            idx += 1

        return None

    def _pattern_to_formatter(self, pattern):
        counter = [-1]
        def increment(m):
            counter[0] += 1
            return "{" + str(counter[0]) + "}"

        return re.sub(r"\*", increment, pattern)

    def _is_formatter(self, exp):
        return exp.find("*") != -1
