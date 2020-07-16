---
layout: page
show_meta: false
title: "Volta"
subheadline: "Help! I Need Tech Support"
header:
   image_fullwidth: "volta1.jpg"
permalink: "/volta/"
---
{% assign vroom = nil %}
{% for vr in site.data.vrooms %}
  {% if vr.name == page.title %}
    {% assign vroom = vr %}
    {% break %}
  {% endif %}
{% endfor %}

NVIDIA Tesla V100 powered by NVIDIA [Volta]({{vroom.webinfo}})<sup>TM</sup>
architecture is the computational engine for scientific computing and
artificial intelligence. 

<center style="font-size:24px"><a href="{{vroom.zoom_link}}">Enter Waiting Room</a></center>

{% include link-shortcuts %}
