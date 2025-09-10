# INF601 - Advanced Programming in Python
# Jeff Johnson
# Mini Project 1

#Please submit a link to your GitHub project. Do not submit your project files here.
#This project will be using the packages NumPy and Matplotlib in order to create 5 graphs that output as PNG files.

# ✓(5/5 points) Initial comments with your name, class and project at the top of your .py file.
# ✓(5/5 points) Proper import of packages used.
# ✓(20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
# ✓(10/10 points) Store this information in a list that you will convert to an array in NumPy.
# ✓(10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# ✓(10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.
# pip install numpy
# pip install matplotlib
# pip install yfinance
# pip freeze
# pip freeze > requirements.txt
# https://ranaroussi.github.io/yfinance/

#Import needed packages
import yfinance as yf
import pprint
import numpy as np
import matplotlib.pyplot as plt
import copy
from pathlib import Path

#Initialize variables
stocktickers = {'MSFT','AAPL','TSLA','DKNG','RBRK'}
stocktickerdata = {}
#Initialize project root and charts output directory
project_root = Path().resolve()
output_directory = project_root / "charts"
output_directory.mkdir(parents=True, exist_ok=True)

#Loop through stocks in stocktickers array
for stock in stocktickers:
    #assign variable for stock name for graph titles
    stockname = stock
    #print(stockname)

    #Query stock ticker data
    #Get ticker data for each stock
    dat = yf.Ticker(stock)
    #Get last 10 days of data
    last10 = dat.history(period='10d')
    #Initialize stocktickerdata list
    stocktickerdata[stock] = []
    #Loop through last 10 days of closing stock prices
    for price in last10['Close']:
        #Add closing stock price to stocktickerdata list
        stocktickerdata[stock].append(price)

    #Initialize stockArray with current stock ticker data
    stockArray = np.array(stocktickerdata[stock])
    #print(stock)

    #Initialize listtosort list for gathering min and max
    listtosort = copy.copy(stockArray)
    listtosort.sort()
    #print(listtosort)

    #Plot data to a graph
    plt.plot(stockArray)
    plt.title(stockname)
    plt.axis((0, 10, listtosort.min()-5, listtosort.max()+5))
    plt.xticks(np.arange(0, 11, 1))
    plt.xlabel('Last 10 Days of Trading')
    plt.ylabel('Closing Price')
    plt.show()

    #Save chart
    outfile = output_directory / f"{stockname}.png"
    plt.savefig(outfile)