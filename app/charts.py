import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def generate_bar_chart(labels, values ):

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    
    return fig
    
def generate_pie_chart(labels, values ):

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    
    return fig
    

def show_chart(labels, values, tipo):
    root = tk.Tk()
    root.title("Mi gráfico")
    
    labels = labels
    values = values

    if tipo == 'bar':
        fig = generate_bar_chart(labels, values)

    elif tipo == 'pie':
        fig = generate_pie_chart(labels, values )
    
    else: 
        print('escoje un tipo de grafica')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    root.protocol("WM_DELETE_WINDOW", root.quit)
    root.mainloop()


if __name__ == "__main__":
    show_chart()
