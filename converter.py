import re


class Converter(object):
    def __init__(self, patterns):
        self.from_re = []
        self.to_exp = []

        for pattern in patterns:
            self.from_re.append(self._pattern_to_re(pattern))
            self.to_exp.append(self._pattern_to_formatter(pattern))

    def convert(self, path):
        results = []
        lenght = len(self.from_re)

        for i in range(lenght):
            match = self.from_re[i].match(path)
            if not match: continue

            j = (i + 1) % lenght
            while (j is not i):
                results.append(self.to_exp[j].format(*match.groups()))
                j = (j + 1) % lenght

            break

        return results

    def _pattern_to_re(self, pattern):
        return re.compile(re.escape(pattern).replace("\\*", "(.*)"))

    def _pattern_to_formatter(self, pattern):
        counter = [-1]
        def increment(m):
            counter[0] += 1
            return "{" + str(counter[0]) + "}"

        return re.sub(r"\*", increment, pattern)

    def _is_formatter(self, exp):
        return exp.find("*") != -1


class WindowsConverter(Converter):
    def __init__(self, patterns):
        super(WindowsConverter, self).__init__(list(map(self._normalize, patterns)))

    def _normalize(self, path):
        return path.replace("/", "\\")


def create(patterns, platform):
    if platform is "windows": return WindowsConverter(patterns)
    else:   return Converter(patterns)
