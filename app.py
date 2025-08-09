from flask import Flask, render_template, request, send_file
from utilities import scrape_xrates_for_date, calculate_usd_exchange_difference, get_valid_date_input
import pandas as pd
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_csv():
    date_str = request.form['date']
    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        df = scrape_xrates_for_date(target_date)
        if df is not None:
            filename = f"xrates_data_{target_date}.csv"
            df.to_csv(filename, index=False)
            return send_file(filename, as_attachment=True)
        return "Failed to fetch data.", 400
    except Exception as e:
        return f"Error: {e}", 500

@app.route('/compare', methods=['POST'])
def compare_csvs():
    date1 = request.form['date1']
    date2 = request.form['date2']
    try:
        d1 = datetime.strptime(date1, "%Y-%m-%d").date()
        d2 = datetime.strptime(date2, "%Y-%m-%d").date()
        df1 = scrape_xrates_for_date(d1)
        df2 = scrape_xrates_for_date(d2)
        if df1 is None or df2 is None:
            return "Data for one or both dates is missing.", 400
        merged_df = pd.merge(df1, df2, on='Currency', suffixes=(f'_{d1}', f'_{d2}'))
        merged_df['Rate to USD Diff'] = merged_df[f'Rate to USD_{d2}'] - merged_df[f'Rate to USD_{d1}']
        merged_df['USD to Currency Diff'] = merged_df[f'USD to Currency_{d2}'] - merged_df[f'USD to Currency_{d1}']
        output_file = f"usd_exchange_difference_{d1}_vs_{d2}.csv"
        merged_df.to_csv(output_file, index=False)
        return send_file(output_file, as_attachment=True)
    except Exception as e:
        return f"Error comparing data: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
