from django.test import TestCase
from cr_admin.models import AdminQuota

class AdminQuotaManagerTestCase(TestCase):
    def setUp(self):
        # Create and delete an AdminQuota to make sure we use the first
        # AdminQuota object even if its pk isn't 1.
        quota = AdminQuota.objects.create()
        quota.delete()

        AdminQuota.objects.create()

    def test_quota(self):
        quota = AdminQuota.objects.quota()
        self.assertEqual(quota.new_quota, 2)
