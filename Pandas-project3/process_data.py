from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def analyze_data():
    # Read the CSV file
    try:
        df = pd.read_csv('resume_data.csv')  # Replace with your CSV file path
        
        # Get basic information
        total_rows = len(df)
        total_columns = len(df.columns)
        
        # Count null values in each column
        null_counts = df.isnull().sum().to_dict()
        
        # Count duplicate rows
        duplicate_count = df.duplicated().sum()
        
        # Analyze skills (assuming there's a 'skills' column)
        try:
            # Split skills if they're in a comma-separated format
            skills_series = df['skills'].str.split(',').explode()
            # Get top 5 most common skills
            top_skills = skills_series.value_counts().head(5).to_dict()
        except:
            top_skills = {"Error": "Skills column not found or could not be processed"}
        
        # Prepare data for template
        analysis = {
            'total_rows': total_rows,
            'total_columns': total_columns,
            'null_values': null_counts,
            'duplicate_rows': duplicate_count,
            'top_skills': top_skills
        }
        
        return render_template('data_analysis.html',analysis=analysis)
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)


