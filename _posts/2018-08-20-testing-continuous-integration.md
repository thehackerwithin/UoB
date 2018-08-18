---
layout: post
title: Testing and continuous integration
comments: true
category: upcoming
tags: meeting <+ tags +>
---

* when: Monday 20 July, 1-2.30pm.
* where: Muirhead 112
* what: Testing and continuous integration

## Getting set up

Make sure you have these two things on your computer:

* A Python distribution.  If you haven't got one already, and particularly if
  you are on Windows, I recommend [the Anaconda distribution
  installer](https://www.anaconda.com/distribution/).  Choose the Python 3.6
  version, not the Python 2.7 version.  You do not need to install VSCode,
  when that option comes up.
* [Git version control
  software](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).  I
  suggest you choose the option to use the Nano editor by default, instead of
  Vim (I use Vim, but if you are not used to it, it's a terrible choice for
  getting started as quickly as possible).

## Preparing to use Github

*   Go to [https://github.com](https://github.com)
*   If you haven't got an account, make one now.  Use your `.bham.ac.uk`
    address, it gives you access to some education features (if you ask for
    them).
*   Navigate to
    [https://github.com/matthew-brett/play-poker](https://github.com/matthew-brett/play-poker)
*   Click on the "Fork" button just below the top right of the screen.  Wait
    for a bit.  You should now be looking at your own *fork* of my
    `play-poker` repository.
*   Select the URL of your new forked repository from the URL bar, and copy
    it.  The URL will be of form
    ``https://github.com/your-user-name/play-poker``.
*   Open the terminal (Cmd-spacebar "Terminal" on Mac, Start key "git bash"
    on Windows)
*   Change directory to the Desktop:

    ```
    cd Desktop
    ```

*   Clone your new repository with the following at the terminal:

    ```
    git clone https://github.com/your-user-name/play-poker
    ```

    where `your-user-name` is your Github username.

*   Change directory to the repository directory.

    ```
    cd play-poker
    ```

## Ready for poker

*   If you're on Windows - press the "Start key" then type "Spyder" (no
    quotes).  Press return.  The Spyder editor should start.  Click on File,
    select Open, navigate to the Desktop `play-poker` folder, and select
    `poker.py`. Click the green run (play) icon to run the file.
*   On Mac, in Terminal.app, check you are in the ``Desktop/play-poker`
    directory with:

    ```
    pwd
    ```

    Now run your `poker.py` script with:

    ```
    python poker.py
    ```

*   You should see the printout of "Running tests", and "Finished".
    Congratulations, you are all set for some test-driven development.
