---
layout: page
show_meta: false
title: "El Capitan"
subheadline: "Virtual venues and teleconference links"
header:
   image_fullwidth: "el-capitan3.jpg"
permalink: "/el-capitan/"
---

{% for vr in site.data.vrooms %}
  {% if vr.name == page.title %}
### [Zoom]({{vr.zoom_link}})
    {% break %}
  {% endif %}
{% endfor %}

## Events occuring in this space

{% include agenda room_filter="El-Capitan" %}

{% include link-shortcuts %}
