---
layout: layout
title: "Upcoming Topics"
---

<section class="content">

Upcoming Topics
===============

**Summer 2018**

The next meeting on Monday 25th June from 1-2pm in room UG07, Murray Learning Centre will be a "language gallery" where a champion for each language will highlight its potential uses, followed by questions.

We'll be talking about these 4 popular languages, each of which are more or less essential in their own niche:

* Python
* R
* Javascript
* Matlab

We're proposing to have a 10 minute talk on each, in which someone who uses the language says something about what the language is good for, why it's good, and when it's not so good.

If you would like to volunteer as a speaker, please email Matthew Brett (m.brett@bham.ac.uk).


In addition to these topics, Lightning Talks are welcome at the end of every session, so please don't hesitate to bring some tidbit to share. Also, if you would like to contribute to a topic, contact the volunteer in charge of that topic to see if they would like to collaborate.

<ul class="listing">
  {% assign upcoming = site.posts | where: "category" , "upcoming" %}
  {% for post in upcoming reversed %}
  <li>
  <span>{{ post.date | date: "%B %e, %Y" }}</span> <a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a>
  </li>
  {% endfor %}
</ul>
</section>
