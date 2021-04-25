import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    def setUp(self):
        self.premium_member = Member("Allen", "Kelly", True)
        self.regular_member = Member("Dave", "Taylor", False)

    def test_has_first_name(self):
        self.assertEqual("Allen", self.premium_member.first_name) 