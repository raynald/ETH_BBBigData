class S3:
    def create_a_connection(self):
        #Creating a Connection
        from boto.s3.connection import S3Connection
        self.conn = S3Connection('AKIAJC7QFLHW4EDEZK3Q', 'qG2Inu2MIon3ck7n/PII/e9feD1ZI9kDzz95WBFa')

    def create_a_bucket(self, name):
        #Creating a Bucket
        bucket = self.conn.create_bucket(name)

    def store_large_data(self, bucket_name, location):
        import math, os
        import boto
        from filechunkio import FileChunkIO
        # Connect to S3
        b = self.conn.get_bucket(bucket_name)
        # Get file info
        source_path = location
        source_size = os.stat(source_path).st_size

        # Create a multipart upload request
        mp = b.initiate_multipart_upload(os.path.basename(source_path))

        # Use a chunk size of 50 MiB (feel free to change this)
        chunk_size = 52428800
        chunk_count = int(math.ceil(source_size / chunk_size))

        # Send the file parts, using FileChunkIO to create a file-like object
        # that points to a certain byte range within the original file. We
        # set bytes to never exceed the original file size.
        for i in range(chunk_count + 1):
            offset = chunk_size * i
            bytes = min(chunk_size, source_size - offset)
            with FileChunkIO(source_path, 'r', offset=offset, bytes=bytes) as fp:
                mp.upload_part_from_file(fp, part_num=i + 1)
        # Finish the upload
        mp.complete_upload()

    def accessing_a_bucket(self, name):
        mybucket = self.conn.get_bucket(name)
        for i in mybucket.list():
            print i

    def deleting_a_bucket(self, name):
        full_bucket = self.conn.get_bucket(name)
        # It's full of keys. Delete them all.
        for key in full_bucket.list():
            key.delete()
        self.conn.delete_bucket(name)

    def listing_all_available_buckets(self):
        rs = self.conn.get_all_buckets()
        for b in rs:
            print b.name

