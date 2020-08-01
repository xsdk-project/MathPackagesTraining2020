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

<center style="font-size:24px"><a href="{{vroom.zoom_link}}">Enter This Virtual Room Zoom Meeting</a></center>
<center style="font-size:18px">Launch Slack for this room in<br><a href="{{vroom.slackweb}}" onclick="window.open(this.href,'newwindow','width=600,height=900'); return false;">new browser window</a> or <a href="{{vroom.slackapp}}">desktop app</a></center>

### Events occuring in this space

{% include agenda room_filter="Perlmutter" %}

{% include link-shortcuts %}
