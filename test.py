import unittest

from validation import *


class test_code(unittest.TestCase):
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
