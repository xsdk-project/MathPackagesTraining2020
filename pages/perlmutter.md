---
layout: page
show_meta: false
title: "Perlmutter"
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

[Perlmutter]({{vroom.webinfo}}) will be a heterogeneous system comprising both CPU-only
and GPU-accelerated nodes. It will include a number of innovations designed to meet the
diverse computational and data analysis needs of NERSC’s user base.

<center style="font-size:24px"><a href="{{vroom.zoom_link}}">Enter This Virtual Room</a></center>
<center style="font-size:24px"><a href="{{vroom.slack}}">Launch Slack Chat for This room</a></center>

## Events occuring in this space

{% include agenda room_filter="Perlmutter" %}

{% include link-shortcuts %}
