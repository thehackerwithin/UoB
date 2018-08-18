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
*   Make you're at the home page [https://github.com](https://github.com).
*   Click on the "+" at top right of the screen.  Choose "New repository".
*   Set "play-poker" as the repository name.
*   Put anything you like (or nothing) into the "Description" field.
*   Check the checkbox for "Initialize this repository with a README".
*   In the "Add a license" list box, select "BSD 2-Clause 'Simplified'
    License" 
*   Click the big green "Create repository" button.
*   You should be on your new repository home page.
*   Select the URL of your repository from the URL bar, and copy it.  The URL
    will be of form ``https://github.com/your-user-name/play-poker``.
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
    select Save As, navigate to the `Desktop/play-poker` directory, and change
    the name to `poker.py`.  Save.
*   On Mac - in the Terminal, type `nano poker.py`.

*   On Windows or Mac, clear the current contents of `poker.py` if there is
    any, and replace with:

    ```python
    """ Make poker hands
    """


    def test_new_deck():
        # Test new_deck function
        return None


    if __name__ == "__main__":
        test_new_deck()
    ```

    Save.

*   On Windows, in Spyder, click the green run (play) icon.
*   On Mac, start a new tab in Terminal (Shell menu, New tab).  In that tab,
    check you are in the ``Desktop/play-poker` directory with

    ```
    pwd
    ```

    Now run your `poker.py` script with:

    ```
    python poker.py
    ```
