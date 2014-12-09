import S3 as s

s3 = s.S3()
s3.create_a_connection()
for i in range(1763, 2015):
    if i == 2007:
        continue
    s3.store_large_data('eth-input', '/local/www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/'+str(i)+'.csv')

