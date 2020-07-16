---
layout: page
show_meta: false
title: "Frontier"
subheadline: "Virtual venues and teleconference links"
header:
   image_fullwidth: "frontier2.png"
permalink: "/frontier/"
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

{% include agenda room_filter="Frontier" %}

{% include link-shortcuts %}
