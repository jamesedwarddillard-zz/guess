bls_api_url = 'http://api.bls.gov/publicAPI/v2/timeseries/data/'
bls_api_headers = {'Content-type': 'application/json'}

# how to create series ids http://www.bls.gov/developers/api_faqs.htm#signatures3

prefix = 'CE'
seasonal = 'S'
supersector = '00'
industry = '000000'
data_type = '01'

bls_api_series_id = [prefix + seasonal + supersector + industry + data_type]
