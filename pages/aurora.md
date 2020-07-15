---
layout: page
show_meta: false
title: "Aurora"
subheadline: "Virtual venues and teleconference links"
header:
   image_fullwidth: "aurora2.png"
permalink: "/aurora/"
---

{% for vr in site.data.vrooms %}
  {% if vr.name == page.title %}
### [Zoom]({{vr.zoom_link}})
    {% break %}
  {% endif %}
{% endfor %}

## Events occuring in this space

{% include agenda room_filter="Aurora" %}

{% include link-shortcuts %}
