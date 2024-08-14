'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def fta_bar_plot(df):
    plt.figure(figsize=(12,8))
    sns.countplot(x="fta", data=df)
    plt.title("FTA")
    plt.savefig("data/part3_plots/fta_barplot.png", bbox_inches="tight")
    plt.close()
    
# 2. Hue the previous barplot by sex
def color_code_chart(df):
    plt.figure(figsize=(12,8))
    sns.countplot(x="fta",hue="sex", data=df)
    plt.title("FTA")
    plt.savefig("data/part3_plots/fta_barplot_by_sex.png", bbox_inches="tight")
    plt.close()

# 3. Plot a histogram of age_at_arrest
def plot_age_histogram(df):
    plt.figure(figsize=(12,8))
    sns.histplot(df["age_at_arrest"], bins=20)
    plt.title("Histogram of Age at Arrest")
    plt.savefig("data/part3_plots/age_at_arrest_histogram.png", bbox_inches="tight")
    plt.close()

# 4. Plot the same histogram, but create bins that represent the following age groups 
def age_histogram_with_bins(df):
    bins = [18,21,30,40,100]
    plt.figure(figsize=(12,8))
    sns.histplot(df["age_at_arrest"], bins=bins)
    plt.title("Histogram of Age at Arrest (Custom Bins)")
    plt.savefig("data/part3_plots/histogram_with_bins.png", bbox_inches="tight")
    plt.close()