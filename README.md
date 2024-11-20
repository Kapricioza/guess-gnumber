# geuss-number
## Overview

Simple guessing game bulit in python. If player don't guess correctly, the program provides feedback and keeps track of their attempts.
The game has also plays background music and shows images for incorrect guesses. Game is made in polish language.

## Installation Requirements
Python Version

Make sure you have Python 3.x installed on your system.
Required Libraries

To run the game, you will need to install the following Python libraries:

    * pygame
    * requests
    * Pillow
    * psutil
    * ttkbootstrap

To install these libraries, run the following command in your terminal:

pip install pygame requests pillow ttkbootstrap psutil

### Other libraries
  os
  shutil
  random
  tkinter
These libraries are built in python so you don't need to download them.


# How to Play the Game

    1.Run the game by executing the Python script (papaj_game.py or whatever filename you choose).
    2.Click the Start button in the window to begin the game.
    3.Input your guesses in the provided text box and click Enter.
    4.If your guess is incorrect, the game will provide a hint (either "Za dużo!" or "Za mało!") and show an image for your attempt.
    5.After guessing correctly, the game will display how many attempts it took to guess the correct number and stop the background music.
    6.Play again or exit the game after completing a round.

# Important Notes

    *The game creates a folder (Zgadywanie) on your computer's main drive to store images of incorrect guesses. 
     If the drive does not exist, the game will automatically create a folder on the drive with the most available storage.
    
    *The program uses an image from the internet (at the URL: https://kropa.pl/data/gfx/pictures/large/7/4/110147_1.jpg) which will be downloaded when you first run the game.
    
    *The game use music in mp3 format and a gif. The music are in folder music/papiez.mp3 and a gif is in folder gif/papiez.gif .
    Make sure that you redirected (if you need) these files in a code to avoids errors








    
