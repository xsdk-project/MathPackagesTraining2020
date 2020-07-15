---
layout: page
show_meta: false
title: "El-Capitan"
subheadline: "Virtual venues and teleconference links"
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

### [Info]({{vroom.webinfo}})

<iframe style="border:1px;" width="80%" src="{{vroom.webinfo}}"></iframe>

## Events occuring in this space

{% include agenda room_filter="El-Capitan" %}

{% include link-shortcuts %}
