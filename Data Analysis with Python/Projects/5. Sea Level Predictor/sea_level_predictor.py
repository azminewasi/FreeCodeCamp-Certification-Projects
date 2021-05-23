import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"],s=2)
    plt.xlim([1850, 2075])
    


    # Create first line of best fit

    best_fit=linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x1 = np.arange(1880,2051,1)
    print(len(x1))
    y1 = x1*best_fit.slope + best_fit.intercept

    plt.plot(x1,y1)
    

    # Create second line of best fit

    df2=df.loc[df['Year']>=2000]
    best_fit2=linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
    x2 = np.arange(2000,2051,1)
    y2 = x2*best_fit2.slope + best_fit2.intercept

    plt.plot(x2,y2)



    # Add labels and title
    
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

print(draw_plot())