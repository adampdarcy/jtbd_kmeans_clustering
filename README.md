## Getting Started
This code lets you take the results of a product survey using JTBD and find hidden clusters in the data to help you build better more focused products

## Prerequisites
You just need Python and a few libraries to run plus your survey results

### Check Python Installation

1. Python comes preinstalled on most computers ([download](https://www.python.org/downloads/) if not). On Windows open [console/terminal](https://www.howtogeek.com/235101/10-ways-to-open-the-command-prompt-in-windows-10) and on Mac open [terminal](https://www.howtogeek.com/682770/how-to-open-the-terminal-on-a-mac/) and type:
   ```python
   python --version
   ```

2. Write a test program to output some text by creating a text file called test.py and entering below text and saving (ensuring [no formatting](https://superuser.com/questions/415958/how-do-i-change-the-file-extension-with-textedit-on-osx)):
   ```python
   print("Hello, World!")
   ```

3. Run your test file to see result (ensure it is in same folder as your console/terminal)
   ```python
   python test.py
   ```

### Install libraries

Install [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html), [matplotlib](https://matplotlib.org/stable/users/installing.html) and [sklearn](https://scikit-learn.org/stable/install.html) by following instructions in links 

### Run with test survey 'jtbd_survey.csv' included 

1. Download both [jtbd_kmeans_clustering.py](https://github.com/adampdarcy/jtbd_kmeans_clustering/blob/main/jtbd_kmeans_clustering.py) and [jtbd_survey.csv](https://github.com/adampdarcy/jtbd_kmeans_clustering/blob/main/jtbd_survey.csv) to a folder of your choice

2. Run the program by typing the following into your console/terminal:
   ```python
   python jtbd_kmeans_clustering.py
   ```

3. Observe if a new file was created called 'clustered_survey.csv' which contained a new column called Cluster

### Run with your own survey data 

1. Copy paste your own survey responses into 'jtbd_survey.csv' 

2. Edit the program using any text editor to specify the [column](https://www.shanelynn.ie/pandas-iloc-loc-select-rows-and-columns-dataframe/) indexes for the responses you want to cluster around (you can put range of column numbes e.g. 49:96 or a list e.g. 1,4,6,9)
   ```python
   jtbd_needs_only = training.iloc[:,49:96]
   ```
   
3. Save and run the program by typing the following into your console/terminal:
   ```python
   python jtbd_kmeans_clustering.py
   ```
   
4. Open the new 'clustered_survey.csv' file to see your new Cluster column added
