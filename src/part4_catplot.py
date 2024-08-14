'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

def create_felony_df(arrest_events):
    felony_charge = arrest_events.groupby("arrest_id").apply(lambda group: pd.Series({
        "has_felony_charge": (group["charge_degree"] == "felony").any()
    })).reset_index()
    return felony_charge


# 2. Merge `felony_charge` with `pre_universe` into a new dataframe
def merge_felony(pred_universe, felony_charges):
    merged_df = pd.merge(pred_universe, felony_charges, on="arrest_id")
    return merged_df

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes


##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.

def plot_charge_and_felony_prediction(merged_df):
    sns.catplot(x="has_felony_charge", y="prediction_felony", kind="bar", data=merged_df)
    plt.savefig("data/part4_plots/felony_prediction.png")
    plt.close()

# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest

def plot_nonfelony_prediction(merged_df):
    sns.catplot(x="has_felony_charge", y="prediction_nonfelony", kind="bar", data=merged_df)
    plt.savefig("data/part4_plots/nonfelony_prediction.png")
    plt.close()

# In a print statement, answer the following question: What might explain the difference between the plots?

print("The plots show that individuals with a felony charge are predicted to have a higher likelihood of being rearrested, \nboth for felony and nonfelony crimes. However, the overall probability of nonfelony rearrest is higher, \nsuggesting that nonfelony crimes might be more frequent.\n")

# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
def repeated_plot(merged_df):
    sns.catplot(x="has_felony_charge", y="prediction_felony", hue="y_felony", kind="bar", data=merged_df)
    plt.savefig("data/part4_plots/felony_prediction_with_color.png")
    plt.close()
    
# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?
print("This suggests that people with felony charges are seen as more likely to reoffend, even if they don't.\nOn the other hand, those with misdemeanor charges might sometimes reoffend more seriously than expected.\nIt highlights how serious charges like felonies often lead to higher expectations of future crimes, while less serious charges might sometimes escalate in unexpected ways.")