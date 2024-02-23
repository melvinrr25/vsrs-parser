import io
import csv
import re

def start_cleanup(path_to_file_to_clean):
    final_csv_path = path_to_file_to_clean + '.clean.csv'
    final_csv = open(final_csv_path, 'a')
    f = io.open(path_to_file_to_clean, mode="r", encoding="utf-8")
    csvdata = io.StringIO(f.read())
    reader = csv.DictReader(csvdata, dialect='excel')
    columns = [
        'ClientID',
        'ClientName',
        'EffectiveDate',
        'ServiceName',
        'Pricing',
        'CustomPricing',
        'PAReviewRecordsPricing',
        'PAReviewRecordsCustomPricing',
        'PAAppealPricing',
        'PAAppealCustomPricing',
        'Comments',
        'EscalatorPricingItem_ServiceName', # Escalator Attributes
        'ServiceSubSectionName',
        'StateCode',
        'EscalatorPricingItem_Pricing',
        'EscalatorPricingItem_CustomPricing',
        'EscalatorPricingYear1BeginDate',
        'EscalatorPricingYear1EndDate',
        'EscalatorPricingYear1Price',
        'EscalatorPricingYear2BeginDate',
        'EscalatorPricingYear2EndDate',
        'EscalatorPricingYear2Price',
        'EscalatorPricingYear3BeginDate',
        'EscalatorPricingYear3EndDate',
        'EscalatorPricingYear3Price',
        'EscalatorPricingYear4BeginDate',
        'EscalatorPricingYear4EndDate',
        'EscalatorPricingYear4Price',
        'EscalatorPricingYear5BeginDate',
        'EscalatorPricingYear5EndDate',
        'EscalatorPricingYear5Price',
    ]
    final_csv.write(','.join(columns) + '\n')

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
        # Escalator Attributes
        escPricingItem_ServiceName = " ".join(re.findall(strRegex, row.get('EscalatorPricingItem_ServiceName', '')))
        serviceSubSectionName = " ".join(re.findall(strRegex, row.get('ServiceSubSectionName', '')))
        stateCode = " ".join(re.findall(strRegex, row.get('StateCode', '')))
        escPricingItem_Pricing = " ".join(re.findall(strRegex, row.get('EscalatorPricingItem_Pricing', '')))
        escPricingItem_CustomPricing = " ".join(re.findall(strRegex, row.get('EscalatorPricingItem_CustomPricing', '')))
        escPricingYear1BeginDate = " ".join(re.findall(strRegex, row.get('EscalatorPricingYear1BeginDate', '')))
        escPricingYear1EndDate = " ".join(re.findall(strRegex, row.get('EscalatorPricingYear1EndDate', '')))
        escPricingYear1Price = " ".join(re.findall(strRegex, row.get('EscalatorPricingYear1Price', '')))
        escPricingYear2BeginDate = " ".join(re.findall(strRegex, row.get('EscalatorPricingYear2BeginDate', '')))
        escPricingYear2EndDate = " ".join(re.findall(strRegex, row.get('EscalatorPricingYear2EndDate', '')))
        escPricingYear2Price = " ".join(re.findall(strRegex, row.get('EscalatorPricingYear2Price', '')))
        escPricingYear3BeginDate = " ".join(re.findall(strRegex, row.get('EscalatorPricingYear3BeginDate', '')))
        escPricingYear3EndDate = " ".join(re.findall(strRegex, row.get('EscalatorPricingYear3EndDate', '')))
        escPricingYear3Price = " ".join(re.findall(strRegex, row.get('EscalatorPricingYear3Price', '')))
        escPricingYear4BeginDate = " ".join(re.findall(strRegex, row.get('EscalatorPricingYear4BeginDate', '')))
        escPricingYear4EndDate = " ".join(re.findall(strRegex, row.get('EscalatorPricingYear4EndDate', '')))
        escPricingYear4Price = " ".join(re.findall(strRegex, row.get('EscalatorPricingYear4Price', '')))
        escPricingYear5BeginDate = " ".join(re.findall(strRegex, row.get('EscalatorPricingYear5BeginDate', '')))
        escPricingYear5EndDate = " ".join(re.findall(strRegex, row.get('EscalatorPricingYear5EndDate', '')))
        escPricingYear5Price = " ".join(re.findall(strRegex, row.get('EscalatorPricingYear5Price', '')))

        line_components = [
            client_id,
            client_name,
            effective_date,
            service_name,
            pricing,
            custom_pricing,
            pa_review_records_pricing,
            pa_review_records_custom_pricing,
            pa_appeal_pricing,
            pa_appeal_custom_pricing,
            comments,
            escPricingItem_ServiceName,
            serviceSubSectionName,
            stateCode,
            escPricingItem_Pricing,
            escPricingItem_CustomPricing,
            escPricingYear1BeginDate,
            escPricingYear1EndDate,
            escPricingYear1Price,
            escPricingYear2BeginDate,
            escPricingYear2EndDate,
            escPricingYear2Price,
            escPricingYear3BeginDate,
            escPricingYear3EndDate,
            escPricingYear3Price,
            escPricingYear4BeginDate,
            escPricingYear4EndDate,
            escPricingYear4Price,
            escPricingYear5BeginDate,
            escPricingYear5EndDate,
            escPricingYear5Price,
        ]

        line = ','.join(line_components) + '\n'
        final_csv.write(line)
    final_csv.close()
    
    return final_csv_path
