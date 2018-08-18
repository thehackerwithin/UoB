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
  installer](https://www.anaconda.com/distribution/).
* [Git version control software](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Getting started

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
*   Clone your new repository with the following at the terminal:

    ```
    git clone https://github.com/your-user-name/play-poker
    ```

    where `your-user-name` is your Github username.

*   Change directory in the repository.

    ```
    cd play-poker
    ```
