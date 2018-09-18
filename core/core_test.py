#!/usr/bin/env python3
from django.test import Client, TestCase
from django.urls import reverse


class TestApiCoreUser(TestCase):
    """
    Class for testing API at: https://in.cyb.no/api/core/users.
    """
    def TestUserFormat(self):
        """
        Ensure expected structure in json response.
        """
        client = Client()
        url = reverse('core/users')
        response = client.get(url, secure='secure')
        expected_types = [int, str, str, str, bool, bool, bool, str, list, list, str]
        actual_property_names = [℘ for ℘ in response.content[0].items()]
        for property in actual_property_names:
            expected_type = expected_types.pop()
            actual_value = response.content[property]
            self.assertInstanceOf(actual_value, expected_type, ("%s is not %s" % expected_type, actual_value))
