import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from flask import Flask
from flask import send_file

app = Flask(__name__)

# prevent matplotlib from opening a gui
plt.ioff()
mpl.use('Agg')


@app.route('/')
def hello_world():
    data_source = np.random.randint(1, 6, 40).reshape(10, 4)
    tartalom = []
    with open("income.txt", "r") as fajl:
        fejlec = fajl.readline().split(',')

        sor = fajl.readlines()  #beolvassa az összes sort egy listába
        for adat in sor:
            adat = adat.strip().split(',')  #listák a listában
            tartalom.append(adat)

    for i in range(len(tartalom)):
        for j in range(len(tartalom[0])):
            tartalom[i][j] = int(tartalom[i][j].strip().replace(" ", ""))

    df = pd.DataFrame(tartalom)
    # df.columns = ['Class A', 'Class B', 'Class C', 'Class D']
    df.columns = fejlec
    sns_plot = sns.barplot(palette="ch:.25", data=df, ci=None)
    sns_plot.figure.savefig("output.png")
    plt.close()
    return send_file('output.png', mimetype='image/png')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)