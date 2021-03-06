import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    def setUp(self):
        self.premium_member = Member("Allen", "Kelly", "allen@kelly.com", True, False)
        self.regular_member = Member("Dave", "Taylor","dt@taylor.com", False)
    
    def test_member_id_is_none(self):
        self.assertTrue(self.premium_member.id == None)

    def test_has_first_name(self):
        self.assertEqual("Allen", self.premium_member.first_name)

    def test_has_last_name(self):
        self.assertEqual("Kelly", self.premium_member.last_name)

    def test_has_email(self):
        self.assertEqual("allen@kelly.com", self.premium_member.email)

    def test_is_premium_member(self):
        self.assertTrue(self.premium_member.premium)

    def test_is_not_premium_member(self):
        self.assertFalse(self.regular_member.premium)

    def test_account_active(self):
        self.assertTrue(self.regular_member.active)

    def test_account_inactive(self):
        self.assertFalse(self.premium_member.active)

# test methods
    def test_has_full_name(self):
        self.assertEqual("Allen Kelly", self.premium_member.full_name())