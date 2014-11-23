class EMR:
    def creating_a_connection(self):
        #Creating a connection
        from boto.emr.connection import EmrConnection
        self.conn = EmrConnection('AKIAJC7QFLHW4EDEZK3Q', 'qG2Inu2MIon3ck7n/PII/e9feD1ZI9kDzz95WBFa')
 
    def creating_streaming_job(self):
        #Creating Streaming JobFlow Steps
        from boto.emr.step import StreamingStep
        self.step = StreamingStep(name='my bigdata task',
            mapper='s3n://eth-src/raw_to_stations.py',
            #mapper='s3n://elasticmapreduce/samples/wordcount/wordSplitter.py',
            reducer='s3n://eth-src/stations_to_features.py',
            #reducer='aggregate',
            input='s3n://eth-input/2007.csv', 
            #input='s3n://elasticmapreduce/samples/wordcount/input',
            output='s3n://eth-middle/2007')

    def creating_jobflows(self):
        #Creating JobFlows
        #import boto.emr
        #self.conn = boto.emr.connect_to_region('eu-west-1')
        job_id = self.conn.run_jobflow(name='My jobflow',
                log_uri='s3://eth-log/jobflow_logs',
                master_instance_type='m3.xlarge',
                slave_instance_type='m1.large',
                num_instances=2,
                steps=[self.step],
                ami_version='3.3.1'
                )

        status = self.conn.describe_jobflow(job_id)
        status.state

    def terminating_jobflows(self, job_id):
        #Terminating JobFlows
        #self.conn = boto.emr.connect_to_region('eu-west-1')
        self.conn.terminate_jobflow(job_id)
