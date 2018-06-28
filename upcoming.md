---
layout: layout
title: "Upcoming Topics"
---

<section class="content">

Upcoming Topics
===============

**Summer 2018**

The next meeting on Monday 16th July from 1-2pm in room G13, Nuffield building, will focus on Git and version control.

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
