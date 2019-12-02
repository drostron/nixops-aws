import boto3
import os
import nixops.util
import nixopsaws.ec2_utils

class EFSCommonState():

    _client = None
    _session = None

    def _get_client(self, access_key_id=None, region=None, profile=None):
        if self._client: return self._client

        (access_key_id, secret_access_key) = nixopsaws.ec2_utils.fetch_aws_secret_key(access_key_id or self.access_key_id)

        if not self._session:
            self._session = nixopsaws.ec2_utils.session(**{
                "region_name": self.region,
                "profile_name": profile,
                "aws_access_key_id": access_key_id,
                "aws_secret_access_key": secret_access_key,
                "aws_session_token": os.environ.get('AWS_SESSION_TOKEN')
            })

        self._client = self._session.client('efs')

        return self._client