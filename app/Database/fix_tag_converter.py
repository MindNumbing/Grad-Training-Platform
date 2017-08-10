
class FixConvert:

    def convert_fix(self):
        file = open("FIX5.0-Tags.txt", "r")
        fix_tags = {}

        for l in file:
            fix_tags[l.split()[0]] = l.split()[1]

        file.close()

        return fix_tags
