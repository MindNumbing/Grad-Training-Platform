
def convert_log(log):
    with open(log) as f:
        for line in f.readlines():
            list = line.split('\^A')
            print list


convert_log('FIXT.1.1-DBL-BME.messages.current.log')
