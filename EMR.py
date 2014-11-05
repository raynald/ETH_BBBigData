#Creating a connection
from boto.emr.connection import EmrConnection

conn = EmrConnection('AKIAJC7QFLHW4EDEZK3Q', 'qG2Inu2MIon3ck7n/PII/e9feD1ZI9kDzz95WBFa')

#Creating Streaming JobFlow Steps
from boto.emr.step import StreamingStep
step = StreamingStep(name='My wordcount example',
        ...                      mapper='s3n://elasticmapreduce/samples/wordcount/wordSplitter.py',
        ...                      reducer='aggregate',
        ...                      input='s3n://elasticmapreduce/samples/wordcount/input',
        ...                      output='s3n://<my output bucket>/output/wordcount_output')
#<my output bucket>

#Creating Custom Jar Job Flow Steps
from boto.emr.step import JarStep
step = JarStep(name='Coudburst example',
        ...                jar='s3n://elasticmapreduce/samples/cloudburst/cloudburst.jar',
        ...                step_args=['s3n://elasticmapreduce/samples/cloudburst/input/s_suis.br',
        ...                           's3n://elasticmapreduce/samples/cloudburst/input/100k.br',
        ...                           's3n://<my output bucket>/output/cloudfront_output',
        ...                            36, 3, 0, 1, 240, 48, 24, 24, 128, 16])

#Creating JobFlows
import boto.emr
conn = boto.emr.connect_to_region('us-west-2')
jobid = conn.run_jobflow(name='My jobflow',
        ...                          log_uri='s3://<my log uri>/jobflow_logs',
        ...                          steps=[step])

status = conn.describe_jobflow(jobid)
status.state

#Terminating JobFlows
conn = boto.emr.connect_to_region('us-west-2')
conn.terminate_jobflow('<jobflow id>')
