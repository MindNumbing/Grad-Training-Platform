
class FixConvert:

    def convert_fix(self):
        """Reads in from list of FIX tags, then stores the tags and explanations as key and value in dict"""

        file = open("FIX5.0-Tags.txt", "r")
        fix_tags = {}

        for l in file:
            fix_tags[l.split()[0]] = l.split()[1]  # Places the content of each line into a dictionary

        file.close()

        return fix_tags  # Returns a dictionary containing all FIX tags
