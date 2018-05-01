---
layout: layout
title: "Upcoming Topics"
---

<section class="content">

Upcoming Topics
===============

**Spring 2018**

Monday 13th May - Andrew (Ed) Edmondson will be presenting on Good Software Practices.

In addition to these topics, Lightning Talks are welcome at the end of every session, so please don't hesitate to bring some tidbit to share. Also, if you would like to contribute to a topic, contact the volunteer in charge of that topic to see if they would like to collaborate.

<ul class="listing">
  {% assign upcoming = (site.posts | where: "category" , "upcoming") %}
  {% for post in upcoming reversed %}
  <li>
  <span>{{ post.date | date: "%B %e, %Y" }}</span> <a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a>
  </li>
  {% endfor %}
</ul>
</section>
