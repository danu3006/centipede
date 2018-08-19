from __future__ import division

import matplotlib.pyplot as plt
import numpy as np

from src.centipede import Centipede
from src.player import Player

centipede = Centipede(csv_file_path='docs/Centipede Data.csv')
data = centipede.data

_data = dict(
    chat=dict(
        linear=[0 for _ in range(10)],
        baseline=[0 for _ in range(10)],
        zero=[0 for _ in range(10)]
    ),
    nochat=dict(
        linear=[0 for _ in range(10)],
        baseline=[0 for _ in range(10)],
        zero=[0 for _ in range(10)]
    )
)


#  calculate how many people played to each round
def values():
    for bool_chat in ['chat', 'nochat']:
        for treatment in ['linear', 'baseline', 'zero']:
            for played_round in range(10):
                total = 0
                for player in data[bool_chat][treatment]:
                    if type(player) is Player:
                        if player.round_number == played_round:
                            total += 1
                _data[bool_chat][treatment][played_round] += total


def plot_graph_one_s():
    labels = [str(index) for index in range(10)][1:]
    number_of_people = [0 for _ in range(10)][1:]

    for _type in ['chat', 'nochat']:
        for _round in range(9):
            rank = _round + 1
            for _treatment in ['linear', 'baseline', 'zero']:
                number_of_people[_round] += _data[_type][_treatment][rank]

        plt.bar(labels, number_of_people)
        plt.yticks(np.arange(0, max(number_of_people) + 1, 1.0))

        plt.xlabel('Round Number', fontsize=5)
        plt.ylabel('Number of Participants', fontsize=5)
        plt.title('Centipede Game Played with ' + _type.capitalize())
        plt.savefig(f'graphs/{_type}_totals.png')


def plot_graph_two():
    labels = ('Exponential', 'Linear', 'Zero')
    avgs = [float(0) for _ in range(3)]

    for _type in ['chat', 'nochat']:
        for _index, _treatment in enumerate(['baseline', 'linear', 'zero']):
            list_w = _data[_type][_treatment][1:]
            avgs[_index] = float(sum([(index * count) for index, count in enumerate(list_w)]) / sum(list_w))
        plt.bar(labels, avgs, label=_type)

    plt.xlabel('Treatment', fontsize=5)
    plt.ylabel('Avg Number of Rounds', fontsize=5)
    plt.title('Average Rounds Played')
    plt.legend(loc='best')
    plt.savefig('graphs/avg_totals.png')
    plt.show()


def get_averages():
    total = dict(
        chat=dict(
            baseline=float(),
            linear=float(),
            zero=float()
        ),
        nochat=dict(
            baseline=float(),
            linear=float(),
            zero=float()
        )
    )

    averages = dict(
        chat=dict(
            baseline=float(),
            linear=float(),
            zero=float()
        ),
        nochat=dict(
            baseline=float(),
            linear=float(),
            zero=float()
        )
    )

    # Get totals
    for _type in ['chat', 'nochat']:
        for _treatment in ['baseline', 'linear', 'zero']:
            total[_type][_treatment] += sum(_data[_type][_treatment])

    # averages
    for _type in ['chat', 'nochat']:
        for _treatment in ['baseline', 'linear', 'zero']:
            averages[_type][_treatment] = sum(_data[_type][_treatment]) / total[_type][_treatment]

    print(averages)


# Populate values
values()

# print averages
get_averages()
