---
layout: page
show_meta: false
title: "Main Room"
header:
   image_fullwidth: "q_center_main.jpg"
permalink: "/main-room/"
---
{% assign vroom = nil %}
{% for vr in site.data.vrooms %}
  {% if vr.name == page.title %}
    {% assign vroom = vr %}
    {% break %}
  {% endif %}
{% endfor %}

This is the main meeting room at the [Q-Center](https://qcenter.com/home-guest/)
in [St. Charles, IL.](https://en.wikipedia.org/wiki/St._Charles,_Illinois)
where [ATPESC](https://extremecomputingtraining.anl.gov) is ordinarily hosted.

<center style="font-size:24px"><a href="{{vroom.zoom_link}}">Enter This Virtual Room Zoom Meeting</a></center>
<center style="font-size:18px">Launch Slack for this room in<br><a href="{{vroom.slackweb}}" onclick="window.open(this.href,'newwindow','width=600,height=900'); return false;">new browser window</a> or <a href="{{vroom.slackapp}}">desktop app</a></center>

### Events occuring in this space

{% include agenda room_filter="Main-Room" %}

{% include link-shortcuts %}
