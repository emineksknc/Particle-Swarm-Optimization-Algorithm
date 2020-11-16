# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 12:44:53 2020

@author: Emine
"""
import numpy as np
import random 
import matplotlib.pyplot as plt
#SPHERE FUNCTION
def  fitnes_fun(xx):
    
    num_rows, num_cols = xx.shape
    d = num_cols;# degisken sayisi
    y = []
    for k in range(num_rows): #parcacik sayisi 
        sum = 0
        for ii in range(d):
            xi = xx[k][ii]
            sum = sum + np.power(xi,2)  
        
        y.append(sum)

    return y

    
def PSO():    
    #Başlangıç değerleri
    iter = 100  # iterasyon sayısı
    swarm_size = 10 #Parçacık sayısı
    c1 = 2  #c1 ve  c2 ivme katsayıları
    c2 = 2
    w = 0.7  #Atalet ağırlık katsayısı
    LB = -5.12 # Konum alt sınırı
    UB = 5.12 # Konum üst sınırı
    D = 5   #Tasarım değişkeni sayısı


    vmax_coef = 0.1
    degiskenler = []
    degerler = []
    
    v_max = vmax_coef*(UB-LB)   #Maksimum hız
    v_min = -1 * v_max       #Mininmum hız

    #Parçacıkların ilk hızlarının random olarak hesaplanması
    rand_v = np.random.rand(swarm_size,D)
    particles_v = v_min + (rand_v   * (v_max - v_min))

    #Parçacıkların ilk konumlarının random olarak hesaplanması
    rand_x = np.random.rand(swarm_size,D)
    particles_x = LB + (rand_x * (UB - LB))

    #print(particles_v, particles_x)
    #ilk konuma göre fitness değerleri
    f_val = fitnes_fun(particles_x)

    #Başlangıç pbest'in atanması
    p_best = particles_x
    p_best_val = f_val
    min_particle = min(f_val)
    index = f_val.index(min_particle)

    #Başlangıç gbest'in atanması
    g_best = particles_x[index]
    g_best_val = f_val[index]



    for i in range(iter):

        for j in range(swarm_size):
    
            for k in range(D):
                #rand1 ve rand2 değerlerinin atanması
                r1 = np.random.rand();
                r2 = np.random.rand();
            
                #Parçacığın hızının güncellenmesi
                particles_v[j][k] = w*particles_v[j][k]+ c1*r1*(p_best[j][k]-particles_x[j][k])+ c2*r2*(g_best[k] - particles_x[j][k])

                #Parçacığın konumunun güncellenmesi
                particles_x[j][k] = particles_x[j][k] + particles_v[j][k]
                
                #Yeni konum Upper Boundary'den büyük değer alırsa UB değerine eşitlenir.
                if particles_x[j][k] > UB:
                    particles_x[j][k]= UB
            
                #Yeni konum Lower Boundary'den küçük değer alırsa LB değerine eşitlenir.
                if particles_x[j][k] < LB:
                    particles_x[j][k]= LB
            
                #Yeni hız maksimum hızdan büyük değer alırsa v_max değerine eşitlenir.
                if particles_v[j][k] > v_max:
                    particles_v[j][k]= v_max
                
                #Yeni hız minimum hızdan küçük değer alırsa v_min değerine eşitlenir.
                if particles_v[j][k] < v_min:
                    particles_v[j][k]= v_min
                
                #Değişkenlerin yeni değerlerine göre fitness değerleri hesaplanır.    
                f_val = fitnes_fun(particles_x)
        
        for j in range(swarm_size):
            #Parçacığın yeni fitness değeri personel best'ten küçükse, p_best olarak atanır. 
            if f_val[j] < p_best_val[j]:
                p_best[j][:] = particles_x[j][:].copy()
                p_best_val[j] = f_val[j]
        

            #Parçacığın yeni fitness değeri global best'ten küçükse, g_best olarak atanır.
            if f_val[j] < g_best_val:
                g_best = particles_x[j][:].copy()
                g_best_val = f_val[j]
                
    
        degiskenler.append(g_best)
        
        degerler.append(g_best_val)

    
        #print(i, '. iterasyon Gbest degeri:',g_best_val);

    #print('Fitness degeri:', g_best_val)

    #print('Tasarim değiskenleri:',g_best)

    return degerler,g_best_val,g_best
    
#def Main():
 #   PSO()
    
#if __name__ == "__main__":
 #   Main()