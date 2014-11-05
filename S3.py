#Creating a Connection
from boto.s3.connection import S3Connection

conn = S3Co('AKIAJC7QFLHW4EDEZK3Q', 'qG2Inu2MIon3ck7n/PII/e9feD1ZI9kDzz95WBFa')

#Creating a Bucket
bucket = conn.create_bucket('mybucket')

#Creating a Bucket In Another Location
from boto.s3.connection import Location
print '\n'.join(i for i in dir(Location) if i[0].isupper())

conn.create_bucket('mybucket', location=Location.EU)

#Storing Data
from boto.s3.key import Key
k = Key(bucket)
k.key = 'foobar'
k.set_contents_from_string('This is a test of S3')

#Validate
import boto
c = boto.connect_s3()
b = c.get_bucket('mybucket') # substitute your bucket name here
from boto.s3.key import Key
k = Key(b)
k.key = 'foobar'
k.get_contents_as_string()


#store and retrieve
k = Key(b)
k.key = 'myfile'
k.set_contents_from_filename('foo.jpg')
k.get_contents_to_filename('bar.jpg')

#Storing Large Data
#....
