class Player:
    __chat_enabled: bool = False
    __round_number: int = int()
    __treatment: str = str()

    def __init__(self, line_list):
        """ Player object for each player in the centipede game.

        :param line_list: list of each line in the csv file parsed to python list
        :type line_list: list
        """
        try:
            if str(line_list[0]).lower() == 'chat':
                self.__chat_enabled = True
            else:
                if str(line_list[0]).lower():
                    self.__chat_enabled = False

            self.__round_number = int(line_list[1]) if line_list[1] else 1
            self.__treatment = line_list[2]
        except IndexError as e:
            print(e)

    @property
    def chat_enabled(self):
        return self.__chat_enabled

    @property
    def sample(self):
        return self.sample

    @property
    def round_number(self):
        return self.__round_number

    @property
    def treatment(self):
        return self.__treatment

    def to_json(self):
        pass
