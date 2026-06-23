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
  font-weight: 500; /* Make the text bold */
  padding: 0 20px; /* Adjust the padding for left and right sides */
  text-align: center;
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

<br/>
<div class="bottom-text" style="color: white;">
We develop physics-aware machine learning and molecular simulation methods to understand and control chemistry in <em style="color:#E2C8A8;">realistic, dynamic, and messy</em> environments
</div>
<br/>
<br/>

</div>
