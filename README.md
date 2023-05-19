# Password Strength Checker
###### KH4061CEM Programming and Algorithms 1 at TKH-Coventry                      

<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This program can measure the strength of a password by calculating a strength index that depends on multiple factors including: password length, whether it includes an uppercase or lower character, a number and a special character, whether it is a commonly used password, and if it contains any repeated patterns/sequence of characters from the username.
<br>The program outputs the strength of the password, and the vulnerabilities found.

The functions used can be found in `validation.py`, running it does not give an output. The program can be used by running `password.py`.





https://github.com/IryVk/Password-Strength-Checker/assets/114566375/0ca2ba0c-631a-4a18-966c-da25939d1ab3





<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.js]][Python-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
### Running the program
1. The program can be run by writing the following into the terminal:
   ```sh
   python password.py
   ```
2. The user will then be prompted to enter their password.
   ```sh
   Username: ######
   ```
3. Afterwards, the user will be prompted to enter their password. If they enter a password less than 3 characters long, the program will raise a `ValueError` and reprompt the user for their password.
   ```sh
   Password: **
   Password is too short, please enter at least 3 characters.
   Password: *********
   ```
4. Finally, the program will output the password strength, and guide the user about any vulnerabilities found in their password.<br>
Running example:
   ```sh
   coursework-2-webarebears> python password.py
   Username: John Smith
   Password: Smith75
   Password is less than 8 characters.
   Password does not contain any special characters from the following: !@#$%^&*()-+.  
   Password should not contain sequences from your username.
   Password is Weak.
   ```
   <br>
Note: Do not run `validate.py` as it does not give an output.<br>
_For more examples, please refer to the [Documentation](https://github.com/Coventry-TKH/coursework-2-webarebears/files/10263577/Course-Work-2-Report.pdf)_


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- FEATURES -->
## Features

- [ ] 
Runs a list of checks:
  - [x] 
  Checks if password contains at least one uppercase letter.
  - [ ] 
  Checks if password contains at least one lowercase letter.
  - [ ] 
  Checks if password contains at least number.
  - [ ] 
  Checks if password contains at least one special character from the following: !@#$%^&*()-+.
- [ ] 
Compares password with a database of commonly used passwords.
- [ ] 
Compares password with username to find any repeated sequence.
- [ ] 
Calculates strength index based on all the checks.
- [ ] 
Compiles a list of vulnerabilities found in the password.


See the [open issues](https://github.com/Coventry-TKH/coursework-2-webarebears/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Arwa Essam Abdelaziz - aa2101585@tkh.edu.eg

Begad Hatem Diab - bd2101453@tkh.edu.eg

Adham Heshame Mounir - am2101322@tkh.edu.eg

Project Link: [https://github.com/Coventry-TKH/coursework-2-webarebears](https://github.com/Coventry-TKH/coursework-2-webarebears)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/Coventry-TKH/coursework-2-webarebears.svg?style=for-the-badge
[contributors-url]: https://github.com/Coventry-TKH/coursework-2-webarebears/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Coventry-TKH/coursework-2-webarebears.svg?style=for-the-badge
[forks-url]: https://github.com/Coventry-TKH/coursework-2-webarebears/network/members
[stars-shield]: https://img.shields.io/github/stars/Coventry-TKH/coursework-2-webarebears.svg?style=for-the-badge
[stars-url]: https://github.com/Coventry-TKH/coursework-2-webarebears/stargazers
[issues-shield]: https://img.shields.io/github/issues/Coventry-TKH/coursework-2-webarebears.svg?style=for-the-badge
[issues-url]: https://github.com/Coventry-TKH/coursework-2-webarebears/issues
[license-shield]: https://img.shields.io/github/license/Coventry-TKH/coursework-2-webarebears.svg?style=for-the-badge
[license-url]: https://github.com/Coventry-TKH/coursework-2-webarebears/blob/master/LICENSE.txt
[Python.js]: https://img.shields.io/badge/python-3.2-pink
[Python-url]: https://www.python.org/
