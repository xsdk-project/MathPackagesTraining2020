---
layout: page
show_meta: false
title: "Amphitheater"
subheadline: "Virtual venues and teleconference links"
header:
   image_fullwidth: "q_center_main.jpg"
permalink: "/amphitheater/"
---
{% assign vroom = nil %}
{% for vr in site.data.vrooms %}
  {% if vr.name == page.title %}
    {% assign vroom = vr %}
    {% break %}
  {% endif %}
{% endfor %}

This is the main meeting room at the [Q-Center](https://qcenter.com/home-guest/)
where [ATPESC](https://extremecomputingtraining.anl.gov) is ordinarily hosted.

<center style="font-size:24px"><a href="{{vroom.zoom_link}}">Enter This Virtual Room</a></center>

## Events occuring in this space

{% include agenda room_filter="Amphitheater" %}

{% include link-shortcuts %}
