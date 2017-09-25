# Fresh Tomatoes
Fresh Tomatoes is a simple website which displays your favourite movies and their trailers.

# Installation
Clone the GitHub repository. Ensure the following files are located in the same directory:
* fresh_tomatoes.py
* media.py
* entertainment_center.py

# Requirements
Python 2.7 or 3.6 is required to run `entertainment_center.py`.

A web browser is required to display the Fresh Tomatoes web page. While Chrome (Version 60.0.3112.113) is recommended, adventurous users are welcome to use Internet Explorer 7.0.

# Editing the List of Movies
## Changing the order in which movies are displayed
In the `entertainment_center.py` file, change the order in which class instances appear in the `movies` variable.

## Adding a movie
In the `entertainment_center.py`, create an instance of the class Movie.

Example:
```
movie_name = (
  'title',
  'poster_image_url',
  'trailer_youtube_url'
  )
```
Append the newly-initialized movie class to the `movies` variable.
Save changes to and run `entertainment_center.py`.

## Removing a movie
In the `entertainment_center.py`, delete the selected class instance from the `movies` variable.
Delete the class instance from `entertainment_center.py`.
Save changes to and run `entertainment_center.py`.

# Issues
Certain YouTube links may have their playback restricted on external websites.

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
