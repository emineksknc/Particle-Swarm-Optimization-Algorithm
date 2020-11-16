# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 23:07:34 2020

@author: Emine
"""

#Kütüphanelerin import edilmesi
from ParticleSwarmOptimization import *
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import pyplot as plt
from celluloid import Camera

#Rastgele renk üretmek için fonksiyon
def productColor():
    color = "#"
    for i in range(6):
        color = color + random.choice("ABCDEF0123456789")
    return  color

#Arayüzdeki,sonuçların gösterildiği plot ve tablonun oluşturulması için fonksiyon
def create_charts():
    
    global x1 #kullanıcıdan alınan çalıştırma sayısı
    x1 = int(entry1.get())
    global plot1
    global table1
    global table2
   

    temp_degerler = []
    temp_g_best_val = []
    temp_color = []  
    #Çalıştırma sayısına göre plot oluşturulması
    for i in range(x1):
      
        figure1 = Figure(figsize=(4, 3), dpi=100)
        plot1 = figure1.add_subplot(111)
        degerler,g_best_val,g_best = PSO()
        temp_degerler.append(degerler)
        temp_g_best_val.append(g_best_val)
    
    for j in temp_degerler:
        color = productColor()
        temp_color.append(color)
        plot1.plot(j, color = color , linestyle="solid")
      
    

    #Çalıştırma sayısına göre sonuç tablosunun oluşturulması
    val1 = ["Global Best Fitness Değeri(g_best_val)"] 
    val2 = ["{}".format(i+1) for i in range(x1)] 
    val3 = [["{}".format(r) for c in range(1)] for r in temp_g_best_val] 
  
    fig, ax = plt.subplots() 
    ax.set_axis_off() 
    table1 = ax.table( 
    cellText = val3,  
    rowLabels = val2,  
    colLabels = val1, 
    rowColours =  [j for j in temp_color],  
    colColours =["white"] ,
    cellLoc ='center',  
    loc ='upper left')         
  
    
    ax.set_title('Results of runnning ' + str(x1) + ' times', fontweight ="bold") 
  

    
    row_name = ['iteration','Particles', 'c1','c2','w','LB','UB','Dimension']
    col_value =['100', '10', '2',' 2', '0.7','-5.12','5.12','5']
    val11 = ["Başlangıç Değerleri"] 
    val22 = ["" + i for i in row_name] 
    val33 = [[""+ r for c in range(1)] for r in col_value] 
  

    
    fig2, ax2 = plt.subplots() 
    ax2.set_axis_off() 
    table2 = ax2.table( 
        cellText = val33, 
        rowLabels = val22,  

        cellLoc ='center',  
        rowLoc = 'left',
        loc ='upper left'
        )   
    
    ax2.set_title('Initial Values ', fontweight ="bold")
    table2 = FigureCanvasTkAgg(fig2, root)
    table2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
    
    table1 = FigureCanvasTkAgg(fig, root)
    table1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
    
    plot1 = FigureCanvasTkAgg(figure1, root)
    plot1.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH, expand=1) 
    
 

#Oluşturulan plot ve tablonun silinmesi için fonksiyon  
def clear_charts():
    plot1.get_tk_widget().pack_forget()
    table1.get_tk_widget().pack_forget()
    table2.get_tk_widget().pack_forget()
            
    
root= tk.Tk()
root.title('Particle Swarm Optimization')
  
canvas1 = tk.Canvas(root, width = 800, height = 300)
canvas1.pack()

label1 = tk.Label(root, text='Particle Swarm Optimization Algorithm')
label1.config(font=('Arial', 20))
canvas1.create_window(400, 50, window=label1)



label3 = tk.Label(root, text='Number of run:')  
label3.config(font=('Arial', 10))
canvas1.create_window(240, 100, window=label3)

#Butonların oluşturulması
entry1 = tk.Entry (root)
canvas1.create_window(360, 100, window=entry1) 
button1 = tk.Button (root, text='Create Charts',command=create_charts, bg='palegreen2', font=('Arial', 11, 'bold')) 
canvas1.create_window(360, 180, window=button1)

button2 = tk.Button (root, text='  Clear Charts  ', command=clear_charts, bg='lightskyblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(360, 220, window=button2)

button3 = tk.Button (root, text='Exit Application', command=root.destroy, bg='lightsteelblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(360, 260, window=button3)
 
root.mainloop()