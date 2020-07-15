---
layout: page
show_meta: false
title: "Perlmutter"
subheadline: "Virtual venues and teleconference links"
header:
   image_fullwidth: "perlmutter2.jpg"
permalink: "/perlmutter/"
---

{% for vr in site.data.vrooms %}
  {% if vr.name == page.title %}
### [Zoom]({{vr.zoom_link}})
    {% break %}
  {% endif %}
{% endfor %}

## Events occuring in this space

{% include agenda room_filter="Perlmutter" %}

{% include link-shortcuts %}
