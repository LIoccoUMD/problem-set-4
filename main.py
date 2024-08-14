'''
- You will run Problem Set 4 from this .py, so make sure to set things up to return outputs accordingly
- Go through each PART and write code / make updates as necessary to produce all required outputs
- Run main.py before you start
'''

import src.part1_etl as part1
import src.part2_plot_examples as part2
import src.part3_bar_hist as part3
import src.part4_catplot as part4
import src.part5_scatter as part5

def main():
    ##  PART 1: ETL  ##
    # ETL the datasets into dataframes
    pred_universe, arrest_events, charge_counts, charge_counts_by_offense = part1.extract_transform()
    felony_charge = part4.create_felony_df(arrest_events)
    merged_df = part4.merge_felony(pred_universe,felony_charge)
    
    ##  PART 2: PLOT EXAMPLES  ##
    # Apply plot theme
    part2.seaborn_settings()

    # Generate plots
    part2.barplots(charge_counts, charge_counts_by_offense)
    part2.cat_plots(charge_counts, pred_universe)
    part2.histograms(pred_universe)
    part2.scatterplot(pred_universe)

    # ##  PART 3: BAR PLOTS AND HISTOGRAMS  ##
    part3.fta_bar_plot(pred_universe)
    part3.color_code_chart(pred_universe)
    part3.plot_age_histogram(pred_universe)
    part3.age_histogram_with_bins(pred_universe)

    # ##  PART 4: CATEGORICAL PLOTS  ##
    part4.plot_charge_and_felony_prediction(merged_df)
    part4.plot_nonfelony_prediction(merged_df)
    part4.repeated_plot(merged_df)

    ##  PART 5: SCATTERPLOTS  ##
    part5.plot_scatter_predictions(merged_df)
    part5.plot_actual_vs_predicted_rearrest(merged_df)

if __name__ == "__main__":
    main()
