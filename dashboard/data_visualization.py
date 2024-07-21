import matplotlib.pyplot as plt

def visualize_data(data):
    fig, ax = plt.subplots()
    ax.plot(data)
    return fig
