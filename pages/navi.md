---
layout: page
show_meta: false
title: "Navi"
subheadline: "Help! I Need Tech Support"
header:
   image_fullwidth: "amd_instinct.jpg"
permalink: "/navi/"
---
{% assign vroom = nil %}
{% for vr in site.data.vrooms %}
  {% if vr.name == page.title %}
    {% assign vroom = vr %}
    {% break %}
  {% endif %}
{% endfor %}

AMD [Navi]({{vroom.webinfo}}) is based on the new 7nm RDNA graphics architecture. It will be the first
mainstream AMD graphics card to break away from the GCN architecture.

<center style="font-size:24px"><a href="{{vroom.zoom_link}}">Enter Waiting Room</a></center>

{% include link-shortcuts %}
