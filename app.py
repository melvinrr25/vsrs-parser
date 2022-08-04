import os
import pandas as pd
import csv
import re
import csv_cleaner
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

app.config['UPLOAD_PATH'] = '/tmp'

@app.route('/')
def home():
   return render_template('upload.html')

@app.route('/upload-csv', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        report_type = request.form['report_type']
        f = request.files['file']
        file_path = os.path.join(app.config['UPLOAD_PATH'], f.filename)
        f.save(file_path)
        cleaned_file_path = csv_cleaner.start_cleanup(file_path)

        data = pd.read_csv(cleaned_file_path)
        data.fillna('', inplace=True)
        data = data[data["ServiceName"] == 'Physician Advisor']
        if report_type == 'dynamodb_backend':
            data = data[data['Pricing'].apply(lambda p: 'per review all states' in p)]
        data.to_csv('out.csv', index=False)

        resp = make_response(data.to_csv(index=False))
        resp.headers["Content-Disposition"] = f'attachment; filename={report_type}.csv'
        resp.headers["Content-Type"] = "text/csv"
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(cleaned_file_path):
            os.remove(cleaned_file_path)
        return resp

with_debug = True if os.getenv('FLASK_DEBUG') else False
app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=with_debug)
