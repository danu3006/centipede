import csv

from .player import Player


class Centipede:
    __data = dict(
        chat=dict(
            zero=list(),
            baseline=list(),
            linear=list()
        ),
        nochat=dict(
            zero=list(),
            baseline=list(),
            linear=list()
        )
    )

    def __init__(self, *, csv_file_path):
        self.__csv_file_path = csv_file_path

        self._parse_csv()

    def _parse_csv(self):
        try:
            with open(self.__csv_file_path) as csv_file:
                # Parse the data into a CSV reader delimited by a comma
                csv_reader = csv.reader(csv_file, delimiter=',')
                # For through each line of the file
                for line in csv_reader:
                    # Check if the line actually has data
                    if line[0] and line[1] and line[2]:
                        # Create player object from the line (ease of access)
                        player = Player(line_list=line)
                        # Check if it is a chat enabled centipede or not
                        if player.chat_enabled:
                            if 'Zero' in line[2]:
                                self.__data['chat']['zero'].append(player)
                            if 'Baseline' in line[2]:
                                self.__data['chat']['baseline'].append(player)
                            if 'Linear' in line[2]:
                                self.__data['chat']['linear'].append(player)
                        else:
                            if 'Zero' in line[2]:
                                self.__data['nochat']['zero'].append(player)
                            if 'Baseline' in line[2]:
                                self.__data['nochat']['baseline'].append(player)
                            if 'Linear' in line[2]:
                                self.__data['nochat']['linear'].append(player)

        except FileNotFoundError as e:
            print(e)

    @property
    def data(self):
        return self.__data
