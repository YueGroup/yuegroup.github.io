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

.top-text {
  font-size: 30px; /* Adjust the font size as needed */
  font-weight: bold; /* Make the text bold */
}

.bottom-text {
  font-size: 20px; /* Adjust the font size as needed */
  font-weight: bold; /* Make the text bold */
  padding: 0 20px; /* Adjust the padding for left and right sides */
}

@media (min-width: 768px) {
    /* Adjust styles for larger screens here */
    .top-text {
        font-size: 40px; /* Example: Increase font size for wider screens */
    }

    .bottom-text {
        font-size: 24px; /* Example: Increase font size for wider screens */
    }
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

<div class="top-text">
{% include particles-home.html %}
</div>

<div class="bottom-text" style="color: #ded4cc;">
Our group works at the interface of molecular simulation, machine-learning, statistical mechanics, and quantum mechanics towards the design of novel electrolytes and materials for energy and sustainability.
</div>
<br/>
<br/>

</div>
