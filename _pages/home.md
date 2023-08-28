---
title: "Home"
layout: default
sitemap: false
permalink: /
---

<style>
.jumbotron{
    padding:3%;
    padding-bottom:10px;
    padding-top:10px;
    margin-top:10px;
    margin-bottom:30px;
}

</style>

<div id="homeid" class="container-fluid col-sm-12 col-xs-12">

<div id="particles-js"></div>

<script src="particles.js"></script>

<script src="{{ 'particles.js' | relative_url }}"></script>
<script>
  particlesJS.load('particles-js', '{{ 'assets/particles.json' | relative_url }}', function() {
    console.log('callback - particles.js config loaded');
  });
</script>

{% include particles-home.html %}

Our group works at the interface of molecular simulation, machine-learning, statistical mechanics, and quantum mechanics towards the design of novel electrolytes and materials for energy and sustainability. test

</div>
