class Player:
    __id_in_session: int = int()
    __code: int = int()
    __chat_enabled: bool = False
    __sample: int = int()
    __id_in_group: int = int()
    __pairing: int = int()
    __decision: str = str()
    __round_number: int = int()
    __treatment: str = str()
    __strategy: str = str()

    def __init__(self, line_list):
        """ Player object for each player in the centipede game.

        :param line_list: list of each line in the csv file parsed to python list
        :type line_list: list
        """
        try:
            self.__id_in_session = line_list[0]
            self.__code = line_list[1]

            if str(line_list[2]).lower() == 'Chat':
                self.__chat_enabled = True
            else:
                self.__chat_enabled = False

            self.__sample = line_list[3]
            self.__id_in_group = line_list[4]
            self.__pairing = line_list[5]
            self.__decision = line_list[6]
            self.__round_number = line_list[7]
            self.__treatment = line_list[8]
            self.__strategy = line_list[9]
        except IndexError as e:
            print(e)

    @property
    def id_in_session(self):
        return self.__id_in_session

    @property
    def code(self):
        return self.__code

    @property
    def chat_enabled(self):
        return self.__chat_enabled

    @property
    def sample(self):
        return self.sample

    @property
    def id_in_group(self):
        return self.__id_in_group

    @property
    def pairing(self):
        return self.__pairing

    @property
    def decision(self):
        return self.__decision

    @property
    def round_number(self):
        return self.__round_number

    @property
    def treatment(self):
        return self.__treatment

    @property
    def strategy(self):
        return self.__strategy

    def to_json(self):
        pass
