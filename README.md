# coursework-2-webarebears
###### CW 1 for programming &amp; algorithms 1 module

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
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This program can encrypt/decrypt text using multiple ciphers: Caesar, Vigenere, Autokey, Playfair and Railfence. The program can encrypt and decrypt text from files or user input, generate secure random keys, and output text files to store encrypted/decrypted text and generated keys.
Each cipher can be run by itself using the corresponding `CIPHERNAME.py` file, or by using `main.py` and providing command line arguments to run the desired cipher.

https://user-images.githubusercontent.com/114566375/200607249-531db7af-9d40-419f-9753-e043ebf9f0cb.mp4

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
3. Afterwards, the user will be prompted to enter their password. If they enter a password less than 3 characters long, the program will raise a `alueError` and reprompt the user for their password.
   ```sh
   Password: **
   Password is too short, please enter at least 3 characters.
   Password: *********
   ```
4. Finally, the program will output the password strength, and guide the users about any vulnerabilities found in their password.
   ```sh
   ex:
   python password.py
   Username: John Smith
   Password: Smith75
   Password is less than 8 characters.
   Password does not contain any special characters from the following: !@#$%^&*()-+.
   Password should not contain sequences from your username.
   Password is Weak.
   ```
Note: Do not run `validate.py` as it does not give an output.
_For more examples, please refer to the [Documentation](https://github.com/Coventry-TKH/coursework-2-webarebears/files/9970925/LINKNEWREPORT)_


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] 
Encrypt/decrypt text using 5 different ciphers.
    - [ ] 
    Encrypt/decrypt text of any length, including numbers and special characters.
- [ ] 
Encrypt/decrypt text from user input.
- [ ] 
Read text from a file and output text to a new file.
- [ ] 
Generate secure random keys.
    - [ ] 
    Store keys in separate text files.

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
[Python.js]: https://img.shields.io/badge/python-3.0-pink
[Python-url]: https://www.python.org/
