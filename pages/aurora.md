---
layout: page
show_meta: false
title: "Aurora"
header:
   image_fullwidth: "aurora2.png"
permalink: "/aurora/"
---
{% assign vroom = nil %}
{% for vr in site.data.vrooms %}
  {% if vr.name == page.title %}
    {% assign vroom = vr %}
    {% break %}
  {% endif %}
{% endfor %}

When it is fully delivered in 2021, [Aurora]({{vroom.webinfo}}) will be the world’s
first supercomputer able to sustain 1 exaFLOP.

<center style="font-size:24px"><a href="{{vroom.zoom_link}}">Enter This Virtual Room Zoom Meeting</a></center>
<center style="font-size:18px">Launch Slack for this room in<br><a href="{{vroom.slackweb}}" onclick="window.open(this.href,'newwindow','width=600,height=900'); return false;">new browser window</a> or <a href="{{vroom.slackapp}}">desktop app</a></center>

### Events occuring in this room

{% include agenda room_filter="Aurora" %}

{% include link-shortcuts %}
