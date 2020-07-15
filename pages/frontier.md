---
layout: page
show_meta: false
title: "Frontier"
subheadline: "Virtual venues and teleconference links"
header:
   image_fullwidth: "frontier2.png"
permalink: "/frontier/"
---

{% for vr in site.data.vrooms %}
  {% if vr.name == page.title %}
### [Zoom]({{vr.zoom_link}})
    {% break %}
  {% endif %}
{% endfor %}

## Events occuring in this space

{% include agenda room_filter="Frontier" %}

{% include link-shortcuts %}
