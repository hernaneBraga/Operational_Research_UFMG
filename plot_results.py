import numpy as npimport matplotlib.pyplot as pltdef plot_tas_per_drink(data, items_TAS, TAS_MIN, TAS_MAX, plot_items, n, max_items):    labels = [label for label in data["item_bebida"]]    plt.title("Quantidade e tipo de itens por TAS em g/L")    gr = plt.gca()    # plot de restrições    plt.axhline(y=TAS_MIN, color='red')    plt.axhline(y=TAS_MAX, color='red')    points_to_plot = items_TAS    m = np.zeros((max_items, n))    for i in range(max_items):        for j in range(n):            m[i][j] = points_to_plot[j] * (i + 1)    for i in range(max_items):        for j in range(n):            plt.plot([j*10], [m[i][j]], 'ro', color='black')            plt.text((j*10+1), m[i][j], r'{}'.format(i+1))    for i in plot_items:        plt.plot([i["id"]*10],[m[int(i["value"])-1][i["id"]]], 'ro', color="cyan")    xticks = np.arange(0, 110, 10)    yticks = np.arange(0, 4.0, 0.5)    gr.set_xticks(xticks)    gr.set_yticks(yticks)    gr.set_xticklabels(labels, rotation=60)    gr.grid(which='major', alpha=0.5)    gr.set_xlabel('Bebida')    gr.set_ylabel('TAS (g/L)')    plt.show()def plot_price_per_drink(data, items_preco, preco_min, preco_max, plot_itens, n, max_items):    labels = [label for label in data["item_bebida"]]    gr = plt.gca()    plt.title("Quantidade e tipo de itens por preço em R$")    # plot de restrições    plt.axhline(y=preco_min, color='red')    # plt.axhline(y=preco_max, color='red')    points_to_plot = items_preco    m = np.zeros((max_items, n))    for i in range(max_items):        for j in range(len(points_to_plot)):            m[i][j] = points_to_plot[j] * (i + 1)    for i in range(max_items):        for j in range(len(points_to_plot)):            plt.plot([j * 10], [m[i][j]], 'ro', color='black')            plt.text((j*10+1), m[i][j], r'{}'.format(i+1))    i_to_plt = plot_itens    for i in i_to_plt:        plt.plot([i["id"] * 10], [m[int(i["value"])-1][i["id"]]], 'ro', color="cyan")    xticks = np.arange(0, 110, 10)    yticks = np.arange(preco_min, sorted(items_preco)[len(items_preco)-1]*5, 30)    gr.set_xticks(xticks)    gr.set_yticks(yticks)    gr.set_xticklabels(labels, rotation=60)    gr.grid(which='major', alpha=0.5)    gr.set_xlabel('Bebida')    gr.set_ylabel('Preço (R$)')    plt.show()