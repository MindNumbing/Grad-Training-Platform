class Converter:

    def convert_log(self, log):
        """loops through each line in file, removes whitespace and seperators. Then translates all into dictionary"""
        l = []
        store = []

        with open(log) as f:
            for line in f.readlines():
                l.append(line.split('\x01'))
                del l[-1][-1]
                q = l[-1][0].split(' : ')
                del l[-1][0]
                l[-1][0:0] = q

        for c in l:
            tmp_dict = {}
            tmp_dict["Recieved Time"] = c[0]
            for n in c[1:]:
                tmp_dict[n.split("=")[0]] = n.split("=")[1]
            store.append(tmp_dict)

        return store


#con = Converter()

#con.convert_log('../../../../quickfix/client/log/FIXT.1.1-DBL-BME.messages.current.log')

