# Fresh Tomatoes
Fresh Tomatoes is a simple website which displays your favourite movies and their trailers.

# Requirements
* Python (version 2.7 or 3.6).
* Web browser is required to display the Fresh Tomatoes web page. Although Chrome (Version 60.0.3112.113) is recommended, adventurous users are welcome to use Internet Explorer 7.0.
* Terminal emulator (e.g., macOS Terminal, Windows cmd, Windows PowerShell) is required to run the `entertainment_center.py` file.

# Installation
Clone the GitHub repository.

```
git clone https://github.com/mundexis/ud036_StarterCode.git
```

Confirm  the following files are located in the same directory:
* fresh_tomatoes.py
* media.py
* entertainment_center.py

```
host:dir user$ cd ud036_StarterCode
host:ud036_StarterCode user$ ls -la
-rw-r--r--   1 user  staff  2948 Sep 25 05:05 README.md
-rw-r--r--   1 user  staff  3274 Sep 25 04:26 entertainment_center.py
-rw-r--r--   1 user  staff  5514 Sep 25 02:33 fresh_tomatoes.py
-rw-r--r--   1 user  staff   655 Sep 25 02:42 media.py
```

# Creating the Website
Using a terminal emulator, navigate to the project directory.

```
host:dir user$ cd ud036_StarterCode
```

Using Python, run the `entertainment_center.py` file.

```
host:ud036_StarterCode user$ python entertainment_center.py
```

# Editing the List of Movies
## Changing the order in which movies are displayed
In the `entertainment_center.py` file, change the order in which class instances appear in the `movies` list.

## Adding a Movie
In the `entertainment_center.py`, create an instance of the class Movie.

Example:
```
# movie_name movie: title, link to the poster image, and link to the movie trailer.
movie_name = (
  'title',
  'poster_image_url',
  'trailer_youtube_url'
  )
```
Append the newly-initialized class instance to the `movies` list.

Save changes to and run `entertainment_center.py`.

## Removing a Movie
In the `entertainment_center.py`, delete the selected class instance from the `movies` list.

Delete the class instance from `entertainment_center.py`.
Save changes to and run `entertainment_center.py`.

# Known Issues
Certain YouTube links may restrict playback on external websites. Alternative links to movie trailers may be required.

# License
This project is available under the MIT License.

Copyright (c) 2017, Artur Maximenco

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
