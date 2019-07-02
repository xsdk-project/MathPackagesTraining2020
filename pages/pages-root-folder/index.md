---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: frontpage
widget1:
  title: "Open</br>Source"
  text: '<a href="https://www.exascaleproject.org"><ul><li>Numerically Rigorous.</li><li>Community Adopted.</li><li>Extremely Scalable.</li><li>Performance Portable.</li></ul></a>'
  video: '<a href="#" data-reveal-id="videoModal1"></a>'
widget2:
  title: "Ease of Use</br>&nbsp;"
  text: '<a href="http://spack.io"><ul><li>Easy Download.</li><li>Easy Configure & Install.</li><li>Easy Dependencies.</li><li>Easy Update.</li></ul></a>'
  video: '<a href="#" data-reveal-id="videoModal2"></a>'
widget3:
  title: "Enhanced</br>Productivity"
  text: '<a href="https://ideas-productivity.org"><ul><li>Development Resources.</li><li>Shared Know-How.</li><li>Common Tools.</li><li>Training.</li></ul></a>'
  video: '<a href="#" data-reveal-id="videoModal3"></a>'
#
# Use the call for action to show a button on the frontpage
#
# To make internal links, just use a permalink like this
# url: /getting-started/
#
# To style the button in different colors, use no value
# to use the main color or success, alert or secondary.
# To change colors see sass/_01_settings_colors.scss
#
callforaction:
  url: https://xsdk.info/faq
  text: How can I get involved?
  style: alert
permalink: /index.html
header:
  image_fullwidth: "shared_values_project_logos_banner2.png"
#
# This is a nasty hack to make the navigation highlight
# this page as active in the topbar navigation
#
homepage: true
---

# Various Projects with Shared Values

The projects highlighted here represent some [DOE](https://science.energy.gov)-funded 
projects with shared values, all of which focus on producing high-quality, well-vetted,
easy to use, sustainable, and scalable numerical packages for developing high-performance scientific simulations.
Each project highlighted on this page addresses a complementary facet of scientific software development and use.
For example, [FASTMath](https://fastmath-scidac.llnl.gov) focuses on the numerical underpinnings
of various packages, while [xSDK](https://xsdk.info) and [Spack](https://spack.io) address ease of use of multiple packages in combination.  Complementary work by the [IDEAS](https://ideas-productivity.org) project and the community-driven organization [Better Scientific Software](https://bssw.io) provides resources to help improve software productivity, quality, and sustainability, as key aspects of increasing overall scientific productivity.  

[//]: # (The stuff below is defining div elements that match the video links above)
[//]: # (Because div elements themselves don't render, this stuff produces no output)
[//]: # (but does provide the target for the video links)

<div id="videoModal1" class="reveal-modal large" data-reveal="">
  <div class="flex-video widescreen vimeo" style="display: block;">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/LBfxK59byxU?start=19" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
  </div>
  <a class="close-reveal-modal">&#215;</a>
</div>
<div id="videoModal2" class="reveal-modal large" data-reveal="">
  <div class="flex-video widescreen vimeo" style="display: block;">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/AgELh5xW-lQ?start=24" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
  </div>
  <a class="close-reveal-modal">&#215;</a>
</div>

<div id="videoModal3" class="reveal-modal large" data-reveal="">
  <div class="flex-video widescreen vimeo" style="display: block;">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/5waBynVgxuc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
  </div>
  <a class="close-reveal-modal">&#215;</a>
</div>
