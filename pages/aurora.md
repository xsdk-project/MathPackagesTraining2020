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

<center style="font-size:24px"><a href="{{vroom.zoom_link}}">Enter This Virtual Room</a></center>
<center style="font-size:24px"><a href="{{vroom.slack}}">Launch Slack Chat for This room</a></center>

[app link](slack://channel?team={TMW2FLNCQ}&id={C01886F33FE})

## Events occuring in this room

{% include agenda room_filter="Aurora" %}

{% include link-shortcuts %}
