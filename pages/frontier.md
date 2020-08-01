---
layout: page
show_meta: false
title: "Frontier"
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

Scheduled for delivery in 2021, [Frontier]({{vroom.webinfo}}) will exceed 1.5 exaFLOPS and accelerate
innovation in science and technology in high-performance computing and artificial intelligence. 

<center style="font-size:24px"><a href="{{vroom.zoom_link}}">Enter This Virtual Room Zoom Meeting</a></center>
<center style="font-size:18px">Launch Slack for this room in<br><a href="{{vroom.slackweb}}" onclick="window.open(this.href,'newwindow','width=600,height=900'); return false;">new browser window</a> or <a href="{{vroom.slackapp}}">desktop app</a></center>

### Events occuring in this space

{% include agenda room_filter="Frontier" %}

{% include link-shortcuts %}
