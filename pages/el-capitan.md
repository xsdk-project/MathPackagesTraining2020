---
layout: page
show_meta: false
title: "El-Capitan"
header:
   image_fullwidth: "el-capitan3.jpg"
permalink: "/el-capitan/"
---
{% assign vroom = nil %}
{% for vr in site.data.vrooms %}
  {% if vr.name == page.title %}
    {% assign vroom = vr %}
    {% break %}
  {% endif %}
{% endfor %}

[El Capitan]({{vroom.webinfo}}) is projected to be the world’s most powerful supercomputer when it is
fully deployed in 2023 and is expected to exceed 2 exaFLOPS.

<center style="font-size:24px"><a href="{{vroom.zoom_link}}">Enter This Virtual Room Zoom Meeting</a></center>
<center style="font-size:18px">Launch Slack for this room in<br><a href="{{vroom.slackweb}}" onclick="window.open(this.href,'newwindow','width=600,height=900'); return false;">new browser window</a> or <a href="{{vroom.slackapp}}">desktop app</a></center>

### Events occuring in this room

{% include agenda room_filter="El-Capitan" %}

{% include link-shortcuts %}
