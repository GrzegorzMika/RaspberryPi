from google.cloud import storage
import pandas as pd
from io import StringIO

storage_client = storage.Client.from_service_account_json('/home/data/secretgc.json')

df = pd.read_csv('/home/data/test.csv')
f = StringIO()
df.to_csv(f)
f.seek(0)

bucket = storage_client.bucket('airly_data')
blob = bucket.blob('docker_test.csv')

blob.upload_from_file(f, content_type='text/csv')