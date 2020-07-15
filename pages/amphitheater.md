---
layout: page
show_meta: false
title: "Amphitheater"
subheadline: "Virtual venues and teleconference links"
header:
   image_fullwidth: "q_center_main.jpg"
permalink: "/amphitheater/"
---

This is the main meeting room at the [Q-Center](https://qcenter.com/home-guest/)
where [ATPESC](https://extremecomputingtraining.anl.gov) is ordinarily hosted.

{% for vr in site.data.vrooms %}
  {% if vr.name == page.title %}
### [Zoom]({{vr.zoom_link}})
    {% break %}
  {% endif %}
{% endfor %}

## Events occuring in this space

{% include agenda room_filter="Amphitheater" %}

{% include link-shortcuts %}
