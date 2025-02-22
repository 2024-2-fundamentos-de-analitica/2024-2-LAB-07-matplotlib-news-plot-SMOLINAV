"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import matplotlib.pyplot as plt
import pandas as pd
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

#  configuración de la figura
    plt.figure()
    colors = {
        'Television' : 'dimgray',
        'Newspaper' : 'grey',
        'Internet' : 'tab:blue',
        'Radio' : 'lightgrey',
    }

    zorder = {
        'Television' : 1,
        'Newspaper' : 1,
        'Internet' : 2,
        'Radio' : 1,
    }

    linewidth = {
        'Television' : 2,
        'Newspaper' : 2,
        'Internet' : 3,
        'Radio' : 2,
    }

# cargar los datos
    df = pd.read_csv('files/input/news.csv',index_col=0)  

    for colum in df.columns:
        plt.plot(
            df[colum],
            color = colors[colum],
            label=colum,
            zorder=zorder[colum],
            linewidth=linewidth[colum]
                )

# configuración de la figura
    plt.title('How people get their news', fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for colum in df.columns:
            first_year = df.index[0]
            plt.scatter(
                x=first_year, 
                y=df[colum][first_year], 
                color=colors[colum], 
                zorder=zorder[colum], 
                        )
            
            plt.text(
                first_year -0.2, 
                df[colum][first_year], 
                colum +' '+str(df[colum][first_year]) + '%', 
                ha ='right', 
                va ='center', 
                color = colors[colum]
                    )
            last_year = df.index[-1]
            plt.scatter(
                x=last_year, 
                y=df[colum][last_year], 
                color=colors[colum], 
                zorder=zorder[colum], 
                        )
            
            plt.text(
                last_year +0.2, 
                df[colum][last_year], 
                colum + ' ' + str(df[colum][last_year]) + '%', 
                ha = 'left', 
                va = 'center', 
                color = colors[colum]
                    )
            

# crear el gráfico
    os.makedirs('files/plots', exist_ok=True)
    
    plt.tight_layout()

    plt.savefig('files/plots/news.png')

pregunta_01()