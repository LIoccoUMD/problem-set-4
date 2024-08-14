'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
def plot_scatter_predictions(merged_df):
    sns.lmplot(x="prediction_felony", y="prediction_nonfelony", hue="has_felony_charge", data=merged_df)
    plt.savefig("data/part5_plots/scatter_predictions.png")
    plt.close()
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
print("\nThe group of dots on the right side of the plot likely represents individuals with high predicted probabilities of felony rearrest.")
# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
def plot_actual_vs_predicted_rearrest(merged_df):
    sns.scatterplot(x="prediction_felony", y="y_felony", data=merged_df)
    plt.savefig("data/part5_plots/real_vs_predicted_rearrest.png")
    plt.close()
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
print("\nThis plot shows that the predictions do not align with the actual outcomes. This suggests that the model is not calibrated as there is not a strong correlation between high predicted probabilities and actual rearrests.")