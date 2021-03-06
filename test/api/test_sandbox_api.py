# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

from __future__ import absolute_import

import unittest

from douyin.open.sandbox.api.sandbox_api import SandboxApi
from douyin.open.sandbox.rest import ApiException

from douyin.open.sandbox.model.common_response import CommonResponse
from douyin.open.sandbox.model.sandbox_webhook_event_send_body import SandboxWebhookEventSendBody


class TestSandboxApi(unittest.TestCase):
    """SandboxApi unit test stubs"""

    def setUp(self):
        self.api = SandboxApi()

    def tearDown(self):
        pass

    def test_sandbox_webhook_event_send_post(self):
        """Test case for sandbox_webhook_event_send_post

        模拟webhook事件
        """
        body=SandboxWebhookEventSendBody()
        resp = self.api.sandbox_webhook_event_send_post(access_token='clt.943da17996fb5cebfbc70c044c3fc25a57T54DcjT6HNKGqnUdxzy1KcxFnZ', body=body)
        pass


if __name__ == '__main__':
    unittest.main()
