# coursework-1-IryVk
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



<!-- GETTING STARTED -->
## Getting Started

To get started: 
1. Open with GitHub Desktop 
2. Clone the repository
3. Open in Visual Studio Code 

Refer to the below sections for instructions and more details.

### Prerequisites

Pytest Package is needed to run the unit tests.
* pytest
  ```sh
  pip install pytest
  ```

### Installation

1. Run Visual Studio Code
2. Open a new terminal window
3. Install pytest package
   ```sh
   pip install pytest
   ```
   

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
### Running Individual Ciphers
1. Each cipher in this project can be run individually by typing the following into the terminal
   ```sh
   python (cipher).py
   ex: python caesar.py
   ```
2. The user will then be prompted to choose whether to encrypt or decrypt.
   ```sh
   Do you want to encrypt or decrypt? ex: encrypt
   ```
3. Afterwards, the user will be prompted to choose whether to read from a file or to write text manually in the terminal. Type `f` to read file, or `w` to write. If the user fails to choose one of these options, an error message will be printed and the user will be re-prompted.
   ```sh
   Read from (f)ile or (w)rite text here?(f/w) ex: f
   ```
   If the user chooses to read from a file, they will be asked to enter the text file name. Make sure to include the file extension `.txt` and avoid any spelling mistakes.  In   case the text file is not in the same folder, write the full path to the file. If the program cannot find the file, the user will be re-prompted.
   ```sh
   File name? ex: C:/Users/NAME/Documents/EXAMPLE.txt
   ```
4. Next, the user will be asked if they want to provide the key, or to randomly generate a key, or -in case of decrypting from a file- read the key from a file. Type `p` to provide the key manually or `r` to generate a random key/read key from a file. 
   ```sh
   If you are decrypting from a file created by this program choose 'r'. Otherwise feel free to choose.
   (P)rovide key or use (r)andom key/
                        (r)ead key from file?(p/r) ex: p
   ```
   If the user chooses to provide the key themselves, they must provide a valid key according to the cipher.
   ```sh
   caesar.py : key has to be an integer between 1 - 95
   autokey.py and vigenere.py : key can be any sequence of characters
   playfair.py : key can be any sequence of letters
   railfence.py : key can be any integer less than the length of the text and greater than 1
   ```
5. Finally, the program will output the encrypted/decrypted text, in case the key was randomly generated, it will be outputted as well. If the text was read from a file, two new text files will be made; one to store the key, and the other to store the output text.

### Running main.py
`main.py` can be used to run any cipher. `main.py` takes two command line arguments. The first is the function you want to do `encrypt` or `decrypt` and the second is `CIPHERNAME`.
   ```sh
   python main.py (encrypt/decrypt) (type of cipher)
   ex: python main.py encrypt caesar
   ```
Next, refer to steps 3-5 from the previous section.

### Running `unittests` package
Before running the unit tests, make sure to install pytest (refer to [Installation](#installation)).
To run all tests, type the following into the command line
   ```sh
   pytest unittests
   ```
 To run a single test on a particular cipher
   ```sh
   pytest unittests/test_CIPHERNAME.py
   ex: pytest unittests/test_playfair.py
   ```
Note: Do not open the "unittests" folder in the terminal before you run. Path should look like this
   ```sh
   Correct Usage: C:\Users\arwaw\Documents\GitHub\coursework-1-IryVk> pytest unittests
   Incorrect Usage: C:\Users\arwaw\Documents\GitHub\coursework-1-IryVk\unittests> pytest unittests
   ```
_For more examples, please refer to the [Documentation](https://github.com/Coventry-TKH/coursework-1-IryVk/files/9970925/Arwa.Abdelaziz.202101585.CW1.Report.pdf)_


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

See the [open issues](https://github.com/Coventry-TKH/coursework-1-IryVk/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Arwa Essam Abdelaziz - aa2101585@tkh.edu.eg

Project Link: [https://github.com/Coventry-TKH/coursework-1-IryVk](https://github.com/Coventry-TKH/coursework-1-IryVk)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/Coventry-TKH/coursework-1-IryVk.svg?style=for-the-badge
[contributors-url]: https://github.com/Coventry-TKH/coursework-1-IryVk/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Coventry-TKH/coursework-1-IryVk.svg?style=for-the-badge
[forks-url]: https://github.com/Coventry-TKH/coursework-1-IryVk/network/members
[stars-shield]: https://img.shields.io/github/stars/Coventry-TKH/coursework-1-IryVk.svg?style=for-the-badge
[stars-url]: https://github.com/Coventry-TKH/coursework-1-IryVk/stargazers
[issues-shield]: https://img.shields.io/github/issues/Coventry-TKH/coursework-1-IryVk.svg?style=for-the-badge
[issues-url]: https://github.com/Coventry-TKH/coursework-1-IryVk/issues
[license-shield]: https://img.shields.io/github/license/Coventry-TKH/coursework-1-IryVk.svg?style=for-the-badge
[license-url]: https://github.com/Coventry-TKH/coursework-1-IryVk/blob/master/LICENSE.txt
[Python.js]: https://img.shields.io/badge/python-3.0-pink
[Python-url]: https://www.python.org/
