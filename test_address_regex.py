from typing import Optional
from dataclasses import dataclass
from unittest import TestCase
import re

from scrape_latest_sales_prices import address_pattern


@dataclass
class Case:
    raw: str
    street: str
    number: str
    floor: Optional[str]
    zip_code: str
    city: str

class TestRegex(TestCase):
    cases = [
        Case(
            'Obstruphøjen 8B 8320 Mårslet',
            'Obstruphøjen',
            '8B',
            '8320',
            'Mårslet'
        )
    ]

    def test_matches(self):
        for case in self.cases:
            m = re.match(address_pattern, case.raw)
            self.assertIsNotNone(m, f'no match for {case}')
            self.assertEqual(m.group('street').strip(), case.street)
            self.assertEqual(m.group('number').strip(), case.number)
            floor = (m.group('floor').strip() 
                     if m.group('floor') is not None 
                     else None)
            self.assertEqual(floor, case.floor)
            self.assertEqual(m.group('street').strip(), case.street)
            self.assertEqual(m.group('zip').strip(), case.zip_code)
            self.assertEqual(m.group('city').strip(), case.city)
