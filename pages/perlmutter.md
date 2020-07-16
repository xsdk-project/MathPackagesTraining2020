---
layout: page
show_meta: false
title: "Perlmutter"
subheadline: "Virtual venues and teleconference links"
header:
   image_fullwidth: "perlmutter2.jpg"
permalink: "/perlmutter/"
---
{% assign vroom = nil %}
{% for vr in site.data.vrooms %}
  {% if vr.name == page.title %}
    {% assign vroom = vr %}
    {% break %}
  {% endif %}
{% endfor %}

<center style="font-size:24px"><a href="{{vroom.zoom_link}}">Enter This Virtual Room</a></center>

## Events occuring in this space

{% include agenda room_filter="Perlmutter" %}

{% include link-shortcuts %}
