from src.centipede import Centipede


data = [
    'docs/centipede1.csv',
    'docs/centipede2.csv',
    'docs/centipede3.csv',
    'docs/centipede4.csv',
    'docs/centipede5.csv',
    'docs/centipede6.csv',
]

centipede = Centipede(csv_file_paths=data)
print(centipede.data)
