import unittest

from validation import *


class test_code(unittest.TestCase):
    def testcase1(self):
#tast cass one (very week passwords)
    # this password is the same as the username  
        self.assertEqual(calc_strength("adham", "adham"), 
        (["Password is less than 8 characters.",
        "Password does not contain any uppercase letters.",
        "Password does not contain any numbers.",
        "Password does not contain any special characters from the following: !@#$%^&*()-+.",
        "Password should not contain sequences from your username."], "Very Weak"), "it is not correct")

    #this password altho deferen it is still within the user mane and it is a comenly used password as well 
        self.assertEqual(calc_strength("spidermanfan", "spiderman"), 
        (["Password does not contain any uppercase letters.",
        "Password does not contain any numbers.",
        "Password does not contain any special characters from the following: !@#$%^&*()-+.",
        "Password should not contain sequences from your username.",
        "Password is a commonly used password."], "Very Weak"), "it is not correct")

    def testcase2(self):
#test cass two(weak passwords)

        #in this cas only the user name was changed wiych can make a big deferens in hte strangth of the password 
        self.assertEqual(calc_strength("usernam", "spiderman"), 
        (["Password does not contain any uppercase letters.",
        "Password does not contain any numbers.",
        "Password does not contain any special characters from the following: !@#$%^&*()-+.",
        "Password is a commonly used password."], "Weak"), "it is not correct")

        #this password is a repeterd patern 
        self.assertEqual(calc_strength("adham@gmail.com", "123_abc"), 
        (["Password is less than 8 characters.",
        "Password does not contain any uppercase letters.",
        "Password does not contain any special characters from the following: !@#$%^&*()-+.",
        "Password contains a repeated pattern/characters in sequence."], "Weak"), "it is not correct")
        
        #altho the user changed the password a bit the password is still the same as the username and it contains patterns
        self.assertEqual(calc_strength("adham@gmail.com", "Adham_123"), 
        (["Password does not contain any special characters from the following: !@#$%^&*()-+.",
        "Password should not contain sequences from your username.",
        "Password contains a repeated pattern/characters in sequence."], "Weak"), "it is not correct")
        
        #altho the password could be strong it contains some comen text that make it weak
        self.assertEqual(calc_strength("adham@gmail.com", "i_love_gold"), 
        (["Password does not contain any uppercase letters.",
        "Password does not contain any numbers.",
        "Password does not contain any special characters from the following: !@#$%^&*()-+.",
        "Password contains a repeated pattern/characters in sequence."], "Weak"), "it is not correct")
        
        #password dosent contain any letters making it weak
        self.assertEqual(calc_strength("adham@gmail.com", "1267998"), 
        (["Password is less than 8 characters.",
        "Password does not contain any uppercase letters.",
        "Password does not contain any lowercase letters.",
        "Password does not contain any special characters from the following: !@#$%^&*()-+."], "Weak"), "it is not correct")

    def testcase3(self):
#test cass 3 (moderate passwors)
    
    #this pasword is good but it can be improved if the password was not in the username 
        self.assertEqual(calc_strength("adham@gmail.com", "Adham_2004"), 
        (["Password does not contain any special characters from the following: !@#$%^&*()-+.",
        "Password should not contain sequences from your username."], "Moderate"), "it is not correct")
        
        #this pass word  could have been strong if it wasnt for the comen text within it 
        self.assertEqual(calc_strength("adham@gmail.com", "i_love_gold@2009"), 
        (["Password does not contain any uppercase letters.",
        "Password contains a repeated pattern/characters in sequence."], "Moderate"), "it is not correct")
        
        #this pasword has all the elemens of a strong pasword exept for spihcal caracters, and the use of the patern holds it back as well  
        self.assertEqual(calc_strength("adham@gmail.com", "i_love_gold2009"), 
        (["Password does not contain any uppercase letters.",
        "Password does not contain any special characters from the following: !@#$%^&*()-+.",
        "Password contains a repeated pattern/characters in sequence."], "Moderate"), "it is not correct")

        self.assertEqual(calc_strength("work@gmail.com", "Adhampass"), 
        (["Password does not contain any numbers.",
        "Password does not contain any special characters from the following: !@#$%^&*()-+."], "Moderate"), "it is not correct")


    def testclass4(self):
#test cass 4 (strong passwords)
    # this passs word just needs some nubers  
        self.assertEqual(calc_strength("work@gmail.com", "Adham@pass"), 
        (["Password does not contain any numbers."], "Strong"), "it is not correct")

        #this password is very good but is in the user name
        self.assertEqual(calc_strength("work@gmail.com", "work@Pass1"), 
        (["Password should not contain sequences from your username."], "Strong"), "it is not correct")

        #this password has a repeted patern 
        self.assertEqual(calc_strength("work@gmail.com", "I_love@goold123"), 
        (["Password contains a repeated pattern/characters in sequence."], "Strong"), "it is not correct")

        #this password just needs uppercase litters
        self.assertEqual(calc_strength("work@gmail.com", "i_love_you@2"), 
        (["Password does not contain any uppercase letters."], "Strong"), "it is not correct")

        #this password needs special characters
        self.assertEqual(calc_strength("work@gmail.com", "Loveyou154"), 
        (["Password does not contain any special characters from the following: !@#$%^&*()-+."], "Strong"), "it is not correct")


    def testcase5(self):
#test cass 5 (very strong password)
        self.assertEqual(calc_strength("work@gmail.com", "i_Love_you@2"), 
        ([], "Very Strong"), "it is not correct")


if __name__=="__main__":
    unittest.main()