import matplotlib.pyplot as plt 
import seaborn as sns 

def pie_probe(datos_lista):
    fig, ax = plt.subplots(1,2,figsize=(4, 2))
    data = datos_lista
    wedgeprops = {'width':0.3, 'edgecolor':'black', 'lw':3}
    patches, _ = ax[0].pie(data, wedgeprops=wedgeprops, startangle=90, colors=['#5DADE2', 'white'])
    patches[1].set_zorder(0) 
    patches[1].set_edgecolor('black')
    #p lt.title('Worldwide Access to Electricity', fontsize=16, loc='left')
    ax[0].text(0, 0, "{0:.2f}%".format(data[0]), ha='center', va='center', fontsize=12)
    # plt.text(-1.2, -1.3, "", ha='left', va='top', fontsize=12)
    
    ax[1].axis("off")
    plt.show()
    

    return fig 
