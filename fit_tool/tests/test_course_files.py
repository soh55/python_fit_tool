# nosetests --nocapture  tests/test_field.py
import logging
import os
import sys
import unittest

from fit_tool.fit_file import FitFile
from fit_tool.utils.logging import formatter, logger


class TestCourseFiles(unittest.TestCase):

    def setUp(self):
        super().setUp()
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    def shortDescription(self):
        return None

    def test_decode_course_file_with_developer_fields(self):
        """Test decoding course file with developer fields
        """
        path = os.path.join(os.path.dirname(__file__), 'data/stagesLink_28832.fit')

        with open(path, 'rb') as file_object:
            bytes_buffer = file_object.read()
            fit_file = FitFile.from_bytes(bytes_buffer)
            print(f'Profile version: {fit_file.header.profile_version}')
            fit_file.to_rows()
