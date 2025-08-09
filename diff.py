import pandas as pd

def calculate_usd_exchange_difference(file1, file2, output_file):
    
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    
    date1 = file1.split('_')[-1].split('.')[0]
    date2 = file2.split('_')[-1].split('.')[0]

    merged_df = pd.merge(df1, df2, on='US Dollar', suffixes=(f'_{date1}', f'_{date2}'))


    merged_df['1.00 USD Diff'] = merged_df[f'1.00 USD_{date2}'] - merged_df[f'1.00 USD_{date1}']
    merged_df['inv. 1.00 USD Diff'] = merged_df[f'inv. 1.00 USD_{date2}'] - merged_df[f'inv. 1.00 USD_{date1}']

    merged_df.to_csv(output_file, index=False)
    print(f"Exchange rate difference saved to: {output_file}")


calculate_usd_exchange_difference(
    "xrates_data_2025-07-15.csv",
    "xrates_data_2025-07-16.csv",
    "usd_exchange_difference_2025-07-15_vs_2025-07-16.csv"
)
