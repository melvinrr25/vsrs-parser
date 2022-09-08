import io
import csv
import re

def start_cleanup(path_to_file_to_clean):
    final_csv_path = path_to_file_to_clean + '.clean.csv'
    final_csv = open(final_csv_path, 'a')
    f = io.open(path_to_file_to_clean, mode="r", encoding="utf-8")
    csvdata = io.StringIO(f.read())
    reader = csv.DictReader(csvdata, dialect='excel')
    final_csv.write("ClientID,ClientName,EffectiveDate,ServiceName,Pricing,CustomPricing,PAReviewRecordsPricing,PAReviewRecordsCustomPricing,PAAppealPricing,PAAppealCustomPricing,Comments\n")

    for row in reader:
        client_id = row.get('ClientID', '')
        if len(client_id) == 0:
            client_id = row.get('\ufeffClientID', '')
        client_name = row.get('ClientName', '')
        effective_date = row.get('EffectiveDate', '')
        service_name = row.get('ServiceName', '')
        pricing = row.get('Pricing', '')
        custom_pricing = row.get('CustomPricing')
        comments = row.get('Comments')
        strRegex = "[a-zA-Z0-9\$\.\;\/-]+"
        custom_pricing = " ".join(re.findall(strRegex, custom_pricing))
        comments = " ".join(re.findall(strRegex, comments))
        pa_review_records_pricing = " ".join(re.findall(strRegex, row.get('PAReviewRecordsPricing', '')))
        pa_review_records_custom_pricing = " ".join(re.findall(strRegex, row.get('PAReviewRecordsCustomPricing', '')))
        pa_appeal_pricing = " ".join(re.findall(strRegex, row.get('PAAppealPricing', '')))
        pa_appeal_custom_pricing = " ".join(re.findall(strRegex, row.get('PAAppealCustomPricing', '')))
        line = f"{client_id},{client_name},{effective_date},{service_name},{pricing},{custom_pricing},{pa_review_records_pricing},{pa_review_records_custom_pricing},{pa_appeal_pricing},{pa_appeal_custom_pricing},{comments}\n"
        final_csv.write(line)
    final_csv.close()
    
    return final_csv_path
