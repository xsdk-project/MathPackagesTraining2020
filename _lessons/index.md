---
layout: page
show_meta: false
title: "ATPESC 2019 Hands On Lessons"
header:
   image_fullwidth: "llnl_machine.jpg"
permalink: /lessons/
---

<table>
{% for item in site.lessons %}
    {% if item.title == "ATPESC 2019 Hands On Lessons" %}
        {% continue %}
    {% endif %}
    {% if item.title == "Lesson Template" %}
        {% continue %}
    {% endif %}
    <tr>
    <td><a href="{{ site.url }}{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a></td>
    <td>{{ item.subheadline }}</td>
    {% if item.youtube %}
        <td><a href="{{ item.youtube }}">YouTube</a></td>
    {% else %}
        <td>No Video</td>
    {% endif %}
    </tr>
{% endfor %}
</table>

# Previous Lessons
* [Lessons from ATEPSC 2017](https://xsdk-project.github.io/HandsOnLessons/lessons/lessons.html)
* [Lessons from ATPESC 2018](https://xsdk-project.github.io/ATPESC2018HandsOnLessons/)
