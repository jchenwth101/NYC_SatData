#Joel Chenoweth
#Date: 04-26-20
#Description:  This reads data from a JSON file from NYC SAT results and writes it to a csv file

import json

class SatData:
    """class SatData with an init method and save_as_csv method"""

    def __init__(self):  #this initializes the class allowing to open file w/attributes

        """ method opens json file, reads file and iterates through indexes(specifically 8-13) and
        pulling title/data from imported json file"""

        with open('sat.json', 'r') as infile:
            self.restored_list = json.load(infile)  # reads SAT/NYC json file

            self.data = self.restored_list["data"]

            self.header = []  # sets header to index list for DBN
        for i in range(8, 14):  # iterates a search through index 8 -13
            self.header.append(self.restored_list['meta']['view']['columns'][i]['name'])  # pulls title
            # from index

    def save_as_csv(self, dbns):

        """this will output to csv file, sorting DBN list, comparing user input
        to DBN's in json file. It will next input the data into the
        the csv file"""
                                                                #needs a list_of_DBNs
        csvFile = open("output.csv", 'w')  # opens Csv file for output
        csvFile.write(','.join(self.header))  #this will write (headers) in csv file
        csvFile.write('\n')

        dbns.sort()  # sorts list

        for dbn in dbns:  # for loop iterates through list
            for row in self.data:
                if dbn == row[8]:  # if DBN is equal to list of DBNs in json file
                    csvFile.write(','.join(row[8:14]))  # write info from indices 8-13
                    csvFile.write('\n')  # line break
                    break

        csvFile.close()
#sd = SatData()
#dbns = ["02M303", "02M294", "01M450", "02M418"]
#print(sd.save_as_csv(dbns))