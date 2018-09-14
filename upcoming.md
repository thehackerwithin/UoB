---
layout: layout
title: "Upcoming Topics"
---

<section class="content">

Upcoming Topics
===============

**Summer 2018**

See below for upcoming meetings.

The next meeting of The Hacker Within takes place on Monday 17th September from 1-2pm in Murray Learning Centre room UG07.

Here are the presentation details:

Title: "A brief introduction to data.table" or "If Thor was an R Programmer, His Hammer Would Be data.table"

Abstract: 
                In this 20-minutes talk, I will present basic examples of the use of `data.table`
                which is an R package that provides an enhanced version of data.frames.
                I will also share some of my experiences with data.table and ggplot2
                for time-series analyses.
                Slides and exercise are available here:    https://github.com/mxochicale/thw-r-datatable
                
Presenter: 
Miguel P Xochicale (twitter: @_mxochicale), 
                Final Year Doctoral Researcher doing Human-Robot Interaction, 
                Nonlinear Dynamics, Deep Learning and Open Science.


If you would like to volunteer as a speaker, please email Matthew Brett (m.brett@bham.ac.uk).


<ul class="listing">
  {% assign upcoming = site.posts | where: "category" , "upcoming" %}
  {% for post in upcoming reversed %}
  <li>
  <span>{{ post.date | date: "%B %e, %Y" }}</span> <a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a>
  </li>
  {% endfor %}
</ul>
</section>
