from collections import Counter
from re import split
from matplotlib import pyplot as plt
import os

WIDGETS = ['Text', 'Container', 'Padding', 'Column', 'Icon',
           'Row', 'SizedBox', 'Center', 'Expanded', 'Scaffold']

if __name__ == '__main__':
    counter = Counter()
    for (folder, _, files) in os.walk(r'/Users/zhu.mei1/tomo/consumer-app/lib/view'):
        for file in files:
            if file.endswith('.dart'):
                with open(os.path.join(folder, file)) as dart_file:
                    words = split(r'[,.;\'"(){}\s+]', dart_file.read())
                    counter.update(words)

    output = {}
    for widget in WIDGETS:
        print(f'{widget}: {counter[widget]}')
        output[widget] = counter[widget]

    plt.figure(figsize=(9, 4))
    plt.bar(range(len(output)), list(output.values()), align='center')
    plt.xticks(range(len(output)), list(output.keys()))
    plt.show()
