### INF601 - Advanced Programming in Python
### Jeff Johnson
### Mini Project 1
 
 
# Mini Project 1
 
Queries last 10 days of stock information for Apple, Draft King, Microsoft, Rubrik, and Tesla. It then creates graphs for each stock, plots the 10 stock prices over each day, and saves the charts to a folder called 'charts'.
 
## Description
 
The program pulls financial data from the yfinance API, processes arrays using NumPy, and plots charts with matplotlib. Each stock closing price for Apple, DraftKings, Microsoft, Rubrik, and Tesla are collected and scaled based on minimum and maximum values and plotted on a graph with X and Y axis labels and a title. The program ensures that a charts directory exists before saving the charts as .png files.
 
## Getting Started
 
### Dependencies
 
Python 3.13.7
Operating System: Windows, macOS, or Linux
Required libraries (install with pip):
    pip install numpy
    pip install matplotlib
    pip install yfinance
 
### Installing
 
1. Clone or download this project to your local machine.
2. Ensure you have the required dependencies listed above installed.
3. Running main.py will automatically create the charts folder if it doesn’t already exist.
 
### Executing program
 
1. Navigate to the project directory.
2. Run the Python script:
```
python main.py
```
 
## Help
 
If you encounter issues with missing modules, re-run pip installs:
    pip install -r requirements.txt

 
## Authors
 
Jeff Johnson
 
## Version History
 
* 0.1
    * Initial Release
 
## License
 
This project is licensed under the MIT License - see the LICENSE.md file for details
 
## Acknowledgments
 
Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)