---
layout: page
show_meta: false
title: "El-Capitan"
subheadline: "Virtual venues and teleconference links"
header:
   image_fullwidth: "el-capitan3.jpg"
permalink: "/el-capitan/"
---
{% assign vroom = nil %}
{% for vr in site.data.vrooms %}
  {% if vr.name == page.title %}
    {% assign vroom = vr %}
    {% break %}
  {% endif %}
{% endfor %}

[El Capitan]({{vroom.webinfo}}) is projected to be the world’s most powerful supercomputer when it is
fully deployed in 2023 and is expected to exceed 2 exaFLOPS.

<center style="font-size:24px"><a href="{{vroom.zoom_link}}">Enter This Virtual Room</a></center>

## Events occuring in this room

{% include agenda room_filter="El-Capitan" %}

{% include link-shortcuts %}
