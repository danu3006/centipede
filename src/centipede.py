import csv
import json
from typing import List, Dict

from .player import Player


class Centipede:
    __data: List[Dict] = list()

    def __init__(self, *, csv_file_paths):
        """ Data analysis of centipede game with different payoffs. E.g. Zero, Linear and Baseline

        :param csv_file_paths: list of all the absolute or relative file path of the relevant csv files
        :type csv_file_paths: list
        """
        self.__csv_file_paths = csv_file_paths

        self._parse_csv()

    def _parse_csv(self):
        """ Parse the CSV and read data into a dictionary to be analysed later. """
        try:
            for path in self.__csv_file_paths:

                # Create temporary dictionary
                temp_dict = dict()

                # Outer two filters
                temp_dict['chat'] = dict()
                temp_dict['nochat'] = dict()

                # Inner filters based on type of Centipede with chat functionality
                temp_dict['chat']['zero']: List = list()
                temp_dict['chat']['baseline'] = list()
                temp_dict['chat']['linear'] = list()

                # Inner filters based on type of Centipede with no chat functionality
                temp_dict['nochat']['zero']: List = list()
                temp_dict['nochat']['baseline'] = list()
                temp_dict['nochat']['linear'] = list()

                with open(path) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    for line in csv_reader:

                        # Check if the line actually has data
                        if line[0]:

                            # Create player object from the line (ease of access)
                            player = Player(line_list=line)

                            # Check if it is a chat enabled centipede or not
                            if player.chat_enabled:
                                if 'Zero' in line[8]:
                                    temp_dict['chat']['zero'].append(player)
                                if 'Baseline' in line[8]:
                                    temp_dict['chat']['baseline'].append(player)
                                if 'Linear' in line[8]:
                                    temp_dict['chat']['linear'].append(player)
                            else:
                                if 'Zero' in line[8]:
                                    temp_dict['nochat']['zero'].append(player)
                                if 'Baseline' in line[8]:
                                    temp_dict['nochat']['baseline'].append(player)
                                if 'Linear' in line[8]:
                                    temp_dict['nochat']['linear'].append(player)

                # Append the temporary dictionary to the global data variable
                self.__data.append(temp_dict)

        except FileNotFoundError as e:
            print(e)

    @property
    def data(self):
        return json.dumps(self.__data)
