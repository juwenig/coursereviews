from django.core.management import call_command
from django.test import TestCase
from reviews.management.commands.padcoursecodes import Command as PadCourseCodes
from reviews.models import Course, Department

class PadcoursecodesTest(TestCase):
    def test_needs_padding_true(self):
        code = 'AMST101'
        self.assertTrue(PadCourseCodes.needs_padding(code))

    def test_needs_padding_false(self):
        code = 'AMST0101'
        self.assertFalse(PadCourseCodes.needs_padding(code))

    def test_pad_code(self):
        code = 'AMST101'
        self.assertEqual(PadCourseCodes.pad_code(code), 'AMST0101')


class PadcoursecodesCommandTest(TestCase):
    def setUp(self):
        dept = Department.objects.create(
            name='American Studies'
        )

        Course.objects.create(
            code='AMST101',
            title='Intro to American Studies',
            dept=dept
        )

    def test_command(self):
        call_command('padcoursecodes')

        course = Course.objects.get(id=1)
        self.assertEqual(course.code, 'AMST0101')
