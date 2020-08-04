---
layout: page
show_meta: false
title: "ATPESC 2020 Hands On Lessons"
not_active: true
header:
   image_fullwidth: "llnl_machine.jpg"
permalink: /lessons/
---

{% assign ordered_lessons = site.lessons | sort:"order" %}
<table>
{% for item in ordered_lessons %}
    {% if item.not_active %}
        {% continue %}
    {% endif %}
    <tr>
    <td><a href="{{ site.url }}{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a></td>
    <td>{{ item.teaser }}</td>
    {% if item.youtube %}
        <td><a href="{{ item.youtube }}">YouTube</a></td>
    {% else %}
        <td>Video to be added</td>
    {% endif %}
    </tr>
{% endfor %}
</table>

# Previous Lessons
* [Lessons from ATEPSC 2019](https://xsdk-project.github.io/MathPackagesTraining/)
* [Lessons from ATPESC 2018](https://xsdk-project.github.io/ATPESC2018HandsOnLessons/)
* [Lessons from ATEPSC 2017](https://xsdk-project.github.io/HandsOnLessons/lessons/lessons.html)
