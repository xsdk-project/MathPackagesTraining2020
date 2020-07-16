---
layout: page
show_meta: false
title: "Vega"
subheadline: "Help! I Need Tech Support"
header:
   image_fullwidth: "amd_gpu.jpg"
permalink: "/vega/"
---
{% assign vroom = nil %}
{% for vr in site.data.vrooms %}
  {% if vr.name == page.title %}
    {% assign vroom = vr %}
    {% break %}
  {% endif %}
{% endfor %}

[Vega]({{vroom.webinfo}}) 7nm Graphics Technology delivers improved performance per watt,
and optimized deep learning operations.

<center style="font-size:24px"><a href="{{vroom.zoom_link}}">Enter Waiting Room</a></center>

{% include link-shortcuts %}
