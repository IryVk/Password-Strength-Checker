import unittest

from validation import *


class test_methods(unittest.TestCase):
    # Test the length check
    def test_length(self):
        self.assertTrue(check_length("12345678"))
        self.assertFalse(check_length("1234"))

    # Test the uppercase check
    def test_upper(self):
        self.assertTrue(check_upper("Abcde"))
        self.assertFalse(check_upper("abcde"))

    # Test the lowercase check
    def test_lower(self):
        self.assertTrue(check_lower("abcde"))
        self.assertFalse(check_lower("ABCDE"))

    # Test the digits check
    def test_digit(self):
        self.assertTrue(check_digit("12345"))
        self.assertFalse(check_digit("abcde"))

    # Test the special check
    def test_special(self):
        self.assertTrue(check_special("abcde#@!"))
        self.assertFalse(check_special("abcde"))

    # Test the unique from username check
    def test_unique(self):
        self.assertTrue(check_unique("username", "password"))
        self.assertFalse(check_unique("username", "username123"))

    # Test if common password check
    def test_common(self):
        self.assertTrue(check_common("AbDer1#__0!"))
        self.assertFalse(check_common("1234"))

    # Test the sequence/pattern check
    def test_seq(self):
        self.assertTrue(check_seq("BIK076#@"))
        self.assertFalse(check_seq("Arwa123"))


class test_strength(unittest.TestCase):
    def testcase1(self):  # Very weak passwords
        # Password same as username
        self.assertEqual(
            calc_strength("adham", "adham"),
            (
                [
                    "Password is less than 8 characters.",
                    "Password does not contain any uppercase letters.",
                    "Password does not contain any numbers.",
                    "Password does not contain any special characters from the following: !@#$%^&*()-+.",
                    "Password should not contain sequences from your username.",
                ],
                "Very Weak",
            ),
            "Test failed :c",
        )

        # Commonly used password + similar to username
        self.assertEqual(
            calc_strength("spidermanfan", "spiderman"),
            (
                [
                    "Password does not contain any uppercase letters.",
                    "Password does not contain any numbers.",
                    "Password does not contain any special characters from the following: !@#$%^&*()-+.",
                    "Password should not contain sequences from your username.",
                    "Password is a commonly used password.",
                ],
                "Very Weak",
            ),
            "Test failed :c",
        )

    def testcase2(self):  # Weak passwords
        # Username is different but password only contains lowercase characters
        self.assertEqual(
            calc_strength("username", "spiderman"),
            (
                [
                    "Password does not contain any uppercase letters.",
                    "Password does not contain any numbers.",
                    "Password does not contain any special characters from the following: !@#$%^&*()-+.",
                    "Password is a commonly used password.",
                ],
                "Weak",
            ),
            "Test failed :c",
        )

        # Repeated pattern
        self.assertEqual(
            calc_strength("adham@gmail.com", "123_abc"),
            (
                [
                    "Password is less than 8 characters.",
                    "Password does not contain any uppercase letters.",
                    "Password does not contain any special characters from the following: !@#$%^&*()-+.",
                    "Password contains a repeated pattern/characters in sequence.",
                ],
                "Weak",
            ),
            "Test failed :c",
        )

        # Similar to username, and has repeated patterns
        self.assertEqual(
            calc_strength("adham@gmail.com", "Adham_123"),
            (
                [
                    "Password does not contain any special characters from the following: !@#$%^&*()-+.",
                    "Password should not contain sequences from your username.",
                    "Password contains a repeated pattern/characters in sequence.",
                ],
                "Weak",
            ),
            "Test failed :c",
        )

        # Common text
        self.assertEqual(
            calc_strength("adham@gmail.com", "i_love_gold"),
            (
                [
                    "Password does not contain any uppercase letters.",
                    "Password does not contain any numbers.",
                    "Password does not contain any special characters from the following: !@#$%^&*()-+.",
                    "Password contains a repeated pattern/characters in sequence.",
                ],
                "Weak",
            ),
            "Test failed :c",
        )

        # Only numbers
        self.assertEqual(
            calc_strength("adham@gmail.com", "1267998"),
            (
                [
                    "Password is less than 8 characters.",
                    "Password does not contain any uppercase letters.",
                    "Password does not contain any lowercase letters.",
                    "Password does not contain any special characters from the following: !@#$%^&*()-+.",
                ],
                "Weak",
            ),
            "Test failed :c",
        )

    def testcase3(self):  # Moderate passwords

        # Good password, but similar to username
        self.assertEqual(
            calc_strength("adham@gmail.com", "Adham_2004"),
            (
                [
                    "Password does not contain any special characters from the following: !@#$%^&*()-+.",
                    "Password should not contain sequences from your username.",
                ],
                "Moderate",
            ),
            "Test failed :c",
        )

        # Good, but no uppercase and common language
        self.assertEqual(
            calc_strength("adham@gmail.com", "i_love_gold@2009"),
            (
                [
                    "Password does not contain any uppercase letters.",
                    "Password contains a repeated pattern/characters in sequence.",
                ],
                "Moderate",
            ),
            "Test failed :c",
        )

        # No special or uppercase characters
        self.assertEqual(
            calc_strength("adham@gmail.com", "i_love_gold2009"),
            (
                [
                    "Password does not contain any uppercase letters.",
                    "Password does not contain any special characters from the following: !@#$%^&*()-+.",
                    "Password contains a repeated pattern/characters in sequence.",
                ],
                "Moderate",
            ),
            "Test failed :c",
        )

        # No numbers or special characters
        self.assertEqual(
            calc_strength("work@gmail.com", "Adhampass"),
            (
                [
                    "Password does not contain any numbers.",
                    "Password does not contain any special characters from the following: !@#$%^&*()-+.",
                ],
                "Moderate",
            ),
            "Test failed :c",
        )

    def testclass4(self):  # Strong password

        # Password missing only numbers
        self.assertEqual(
            calc_strength("work@gmail.com", "Adham@pass"),
            (["Password does not contain any numbers."], "Strong"),
            "Test failed :c",
        )

        # Good password, but similar to username
        self.assertEqual(
            calc_strength("work@gmail.com", "work@Pass1"),
            (["Password should not contain sequences from your username."], "Strong"),
            "Test failed :c",
        )

        # Password has repeated pattern
        self.assertEqual(
            calc_strength("work@gmail.com", "I_love@goold123"),
            (
                ["Password contains a repeated pattern/characters in sequence."],
                "Strong",
            ),
            "Test failed :c",
        )

        # No uppercase characters
        self.assertEqual(
            calc_strength("work@gmail.com", "i_love_you@2"),
            (["Password does not contain any uppercase letters."], "Strong"),
            "Test failed :c",
        )

        # Password missing special characters
        self.assertEqual(
            calc_strength("work@gmail.com", "Loveyou154"),
            (
                [
                    "Password does not contain any special characters from the following: !@#$%^&*()-+."
                ],
                "Strong",
            ),
            "Test failed :c",
        )

    def testcase5(self):  # Very strong

        # Password meets all criteria
        self.assertEqual(
            calc_strength("work@gmail.com", "i_Love_you@2"),
            ([], "Very Strong"),
            "Test failed :c",
        )


if __name__ == "__main__":
    unittest.main()
