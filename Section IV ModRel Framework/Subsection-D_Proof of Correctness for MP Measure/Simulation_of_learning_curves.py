"""
Simulation of 300 Learning Curves with 4 different vairants of decay function.

Input: X value [1,250]

Processing: Processed by 4 variant decay function and it's AD and ABC funciton
values are calculated, stored in the xlsx file and plots a learning curve

Output: 300 Learning curves along with all the parameters in xlsx file and AD ABC
funciton values for each curve.

"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pdb
import math as m

def generate_loss_curves(x):
    # Generate loss curves that stay within the 0.2 to 1 range and don't touch zero
    validation_loss = np.exp(-x / 100) * (np.random.uniform(0.8, 0.99)) #+ round(np.random.uniform(0.02, 0.6),3)  # Added offset to keep it above 0.2
    training_loss = np.exp(-x / 100) * (np.random.uniform(0.7, 0.99)) #+ round(np.random.uniform(0.02,0.5),3)
    #training_loss = validation_loss - (np.random.uniform(0.05, 0.1) + gap_factor)  # Adjust gap between training and validation
    validation_loss = np.clip(validation_loss, 0.02, 1)  # Ensure values stay above 0.2 and below 1
    training_loss = np.clip(training_loss, 0.02, 1)  # Ensure values stay above 0.2 and below 1
    validation_acc=1-validation_loss
    return validation_loss, training_loss,validation_acc

def generate_loss_curves1(x):
    # Generate loss curves that stay within the 0.2 to 1 range and don't touch zero
    validation_loss = np.exp(-x / 100) * (np.random.uniform(0.8, 0.99)) + round(np.random.uniform(0.02, 0.5),3)  # Added offset to keep it above 0.2
    training_loss = np.exp(-x / 100) * (np.random.uniform(0.7, 0.99)) + round(np.random.uniform(0.02,0.),3)
    #training_loss = validation_loss - (np.random.uniform(0.05, 0.1) + gap_factor)  # Adjust gap between training and validation
    validation_loss = np.clip(validation_loss, 0.02, 1)  # Ensure values stay above 0.2 and below 1
    training_loss = np.clip(training_loss, 0.02, 1)  # Ensure values stay above 0.2 and below 1
    validation_acc=1-validation_loss
    return validation_loss, training_loss,validation_acc

def generate_loss_curves2(x):
    # Generate loss curves that stay within the 0.2 to 1 range and don't touch zero
    validation_loss = np.exp(-x / 50) * (np.random.uniform(0.8, 0.99)) + round(np.random.uniform(0.02, 0.2),3)  # Added offset to keep it above 0.2
    training_loss = np.exp(-x / 25) * (np.random.uniform(0.7, 0.99)) + round(np.random.uniform(0.02,0.3),3)
    #training_loss = validation_loss - (np.random.uniform(0.05, 0.1) + gap_factor)  # Adjust gap between training and validation
    validation_loss = np.clip(validation_loss, 0.02, 1)  # Ensure values stay above 0.2 and below 1
    training_loss = np.clip(training_loss, 0.02, 1)  # Ensure values stay above 0.2 and below 1
    validation_acc=1-validation_loss
    return validation_loss, training_loss,validation_acc

def generate_loss_curves3(x):
    # Generate loss curves that stay within the 0.2 to 1 range and don't touch zero
    validation_loss = np.exp(-x / 50) * (np.random.uniform(0.8, 0.99)) + round(np.random.uniform(0.02, 0.2),3)  # Added offset to keep it above 0.2
    training_loss = np.exp(-x / 50) * (np.random.uniform(0.7, 0.99)) + round(np.random.uniform(0.02,0.3),3)
    #training_loss = validation_loss - (np.random.uniform(0.05, 0.1) + gap_factor)  # Adjust gap between training and validation
    validation_loss = np.clip(validation_loss, 0.02, 1)  # Ensure values stay above 0.2 and below 1
    training_loss = np.clip(training_loss, 0.02, 1)  # Ensure values stay above 0.2 and below 1
    validation_acc=1-validation_loss
    return validation_loss, training_loss,validation_acc

def generate_loss_curves4(x):
    # Generate loss curves that stay within the 0.2 to 1 range and don't touch zero
    validation_loss = np.exp(-x / 1000) * (np.random.uniform(0.8, 0.99)) + round(np.random.uniform(0.02, 0.2),3)  # Added offset to keep it above 0.2
    training_loss = np.exp(-x / 1000) * (np.random.uniform(0.7, 0.99)) + round(np.random.uniform(0.02,0.3),3)
    #training_loss = validation_loss - (np.random.uniform(0.05, 0.1) + gap_factor)  # Adjust gap between training and validation
    validation_loss = np.clip(validation_loss, 0.02, 1)  # Ensure values stay above 0.2 and below 1
    training_loss = np.clip(training_loss, 0.02, 1)  # Ensure values stay above 0.2 and below 1
    validation_acc=1-validation_loss
    return validation_loss, training_loss,validation_acc


def fnp1(x, y): #AD function
    return -np.log2(x+0.01)*(1-y+0.01)**-1 

def fnp2(x, y): #ABC function
    #return x**(-1)*y*np.exp(2*y)
    return -np.log2(x)*(y**-1)

if __name__=="__main__":

    k=250 # k number of epochs are considered so x axis values will be upto k
  
    column_names = ['SNo','Model_nu','X(Epochs)', 'R_i_tl', 'R_i_vl','R_i_vlf','|R_i_vl-R_i_tl|','R_i_va','R_i_ak','R_i_ak/k','Label','AD','ABC','R_i_mp']

    # Create an empty DataFrame with only column names
    Rdata = pd.DataFrame(columns=column_names) #allreviewersdata

    all_graph_data = []
    areas = []
    final_validation_losses = []
    final_training_losses = []
    final_validation_acc=[]


    for i in range(1,301):
        # X-axis values (250 units)
        x = np.arange(1, k+1)
        sel=np.random.randint(0, 6)
        if(sel==0):
            validation_loss, training_loss,validation_acc = generate_loss_curves(x)
        elif(sel==1):
            validation_loss, training_loss,validation_acc = generate_loss_curves1(x)
        elif(sel==2):
            validation_loss, training_loss,validation_acc = generate_loss_curves2(x)
        elif(sel==3):
            validation_loss, training_loss,validation_acc = generate_loss_curves3(x)
        else:
            validation_loss, training_loss,validation_acc = generate_loss_curves4(x)
        area = np.trapz(abs(validation_loss - training_loss), x)  # Area between the curves
        Narea = round(area/k,3)
    
        final_validation_losses.append(validation_loss[-1])
        final_training_losses.append(training_loss[-1])
        final_validation_acc.append(validation_acc[-1])


        #dataframe creation with data
        training_loss1=[abs(round(i,3)) for i in training_loss]
        validation_loss1=[abs(round(i,3)) for i in validation_loss]
        validation_acc1=[abs(round(i,3)) for i in validation_acc]

     
        diff=abs(validation_loss1[-1]-training_loss1[-1])
        va=validation_acc[-1]
        vsf=validation_loss1[-1]
        AD=fnp1(diff,va)
        ABC=fnp2(Narea,vsf)
        MP=AD+ABC
        sno=i
        row={
            'SNo': sno,
            'Model_nu':f"Simulated Learning Curves_{sno}",
            'X(Epochs)':[x],
            'R_i_tl':[training_loss1],
            'R_i_vl':[validation_loss1],
            'R_i_vlf':validation_loss1[-1],
            '|R_i_vl-R_i_tl|':abs(validation_loss1[-1]-training_loss1[-1]),
            'R_i_va':validation_acc[-1],
            'R_i_ak' : round(area,1),
            'R_i_ak/k':Narea, # You can store the same or different arrays in each cell
            'AD':AD,
            'ABC':ABC,
            'R_i_mp':MP,
            }
        # Create a DataFrame with one column that contains the NumPy array in each row
        df = pd.DataFrame(row)
        Rdata = pd.concat([Rdata, df], ignore_index=False)


        plt.figure(figsize=(10, 6))
        plt.plot(x, validation_loss, label=f'Validation Loss\nR_i_vl={validation_loss1[-1]}\n', color='blue', marker='o', markersize=2)
        plt.plot(x, training_loss, label=f'Training Loss\n|R_i_tl - R_i_vl|={round(abs(validation_loss1[-1]-training_loss1[-1]),3)}\nR_i_ak/k={Narea}\n', color='green', marker='o', markersize=2)
        plt.plot(x,validation_acc,label=f'validation accuracy\nR_i_va={round(validation_acc[-1],3)}\nR_i_mp={round(MP,3)}',color='red',marker='o',markersize=2)

        # Shade the area between the curves
        plt.fill_between(x, validation_loss, training_loss, color='gray', alpha=0.3)

        # Adding titles and labels
        plt.title(f'Simulated Learning Curves-{sno}')
        plt.xlabel(f'Epochs (X-axis, {k} units)')
        plt.ylabel('Loss (Y-axis between 0 and 1)')

        # Setting y-axis limits
        plt.ylim(0.01, 1)  # Ensure the curve doesn't touch zero and stays above 0.2

        # Displaying legend
        plt.legend()

        # Show grid
        plt.grid(True)

        # Show the plot
        plt.tight_layout()
        imagename = f"Path"+f"\\Simulated Learning Curve_{sno}.jpg"
        plt.savefig(imagename)
        plt.show()

    ExcelFileName =  f"path"+f"\\Learning Curvesv2.xlsx"
    Rdata.to_excel(ExcelFileName, index=False) 
