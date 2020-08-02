---
layout: page
show_meta: false
title: "Getting help"
header:
   image_fullwidth: "tech_support8.jpg"
permalink: "/getting-help/"
---
{% assign vroom = nil %}
{% for vr in site.data.vrooms %}
  {% if vr.name == "Amphitheater" %}
    {% assign vroom = vr %}
    {% break %}
  {% endif %}
{% endfor %}

Use the *#numerical* slack channel for general help and it support.

<center style="font-size:18px">Launch #numerical Slack in<br><a href="{{vroom.slackweb}}" onclick="window.open(this.href,'newwindow','width=600,height=900'); return false;">new browser window</a> or <a href="{{vroom.slackapp}}">desktop app</a></center>

### IT Support Zoom Rooms
Also individual tech support is available from specialists in these Zoom rooms...

* [Ampere]
* [Volta]
* [Navi] (morning sessions only; viz-tool issues only)
* [Vega] (morning sessions only; viz-tool issues only)

{% include link-shortcuts %}
