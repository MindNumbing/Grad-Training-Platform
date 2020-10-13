class Converter:

    def convert_log(self, log):
        """loops through each line in file, removes whitespace and separators. Then translates all into dictionary"""
        l = []
        store = []

        with open(log) as f:
            for line in f.readlines():
<<<<<<< HEAD
                l.append(line.split('\x01'))
                del l[-1][-1]
                q = l[-1][0].split(' : ')
                del l[-1][0]
                l[-1][0:0] = q
=======
                l.append(line.split('\x01'))    # Removes separator characters
                del l[-1][-1]                   # Removes \n
                q = l[-1][0].split(' : ')       # Separates first two elements
                del l[-1][0]                    # Deletes first element
                l[-1][0:0] = q                  # Adds in two new elements

        open(log, 'w').close()  # Clears log file
>>>>>>> 05c7c901c9941b14d481dfe9622c36f03c4f5b89

        for c in l:
            tmp_dict = {}
            tmp_dict["Recieved Time"] = c[0]                 # Adds first element to dictionary manually
            for n in c[1:]:
                tmp_dict[n.split("=")[0]] = n.split("=")[1]  # Splits each element into key and value
            store.append(tmp_dict)                           # Adds completed dict to list

        return store  # Returns list of parsed messages


#con = Converter()

#con.convert_log('../../../../quickfix/client/log/FIXT.1.1-DBL-BME.messages.current.log')

