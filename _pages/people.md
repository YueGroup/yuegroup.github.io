---
title: "People"
layout: gridlay
sitemap: false
permalink: /people/
---

<style>
  /* Add custom styles here */
  .circle-photo img {
    border-radius: 50%;
  }

  .circle-icon {
    border-radius: 50%;
    background-color: #f2f2f2;
    padding: 10px;
  }

  /* Customize the heading styles */
  h3#pi,
  h3#current-students {
    font-size: 24px; /* Adjust the font size as needed */
    text-align: center;
    margin: 20px 0; /* Add some margin for spacing */
  }
</style>

<h3 id="pi">Principle Investigator</h3>

{% for member in site.data.pi %}

<div class="jumbotron">
<div class="row">
<div class="col-sm-4">
<div class="circle-photo">
  <img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
</div>
<div class="col-sm-12 col-xs-12">
<h4>{{ member.name }}</h4>
<i>{{ member.info }}</i><br>
<p> {{ member.location }} </p>
  {% if member.website %}<a href="{{ member.website }}" target="_blank"><i class="fa fa-home fa-2x"></i></a> {% endif %}
  {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %}
  {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x"></i></a> {% endif %}
  {% if member.cv %} <a href="{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-2x"></i></a> {% endif %}
  {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-2x"></i></a> {% endif %}
  {% if member.linkedin %} <a href="{{ member.linkedin }}" target="_blank"><i class="fa fa-linkedin-square fa-2x"></i></a> {% endif %}
  {% if member.twitter %}<a href="{{ member.twitter }}" target="_blank"><i class="fa fa-twitter-square fa-2x"></i></a> {% endif %}
  {% if member.education1 %} <p> {{ member.education1 }} </p> {% endif %}
  {% if member.education2 %} <p> {{ member.education2 }} </p> {% endif %}
  {% if member.education3 %} <p> {{ member.education3 }} </p> {% endif %}
</div>
</div>
</div>

{% endfor %}


<h3 id="current-students">Group Members</h3>

{% for member in site.data.people %}

<div class="jumbotron">
<div class="row">
<div class="col-sm-4">
<div class="circle-photo">
  <img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
</div>
<div class="col-sm-12 col-xs-12">
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }}<br></i>
  <p> {{ member.location }} </p>
  {% if member.website %}<a href="{{ member.website }}" target="_blank"><i class="fa fa-home fa-2x"></i></a> {% endif %}
  {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %}
  {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x"></i></a> {% endif %}
  {% if member.cv %} <a href="{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-2x"></i></a> {% endif %}
  {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-2x"></i></a> {% endif %}
  {% if member.linkedin %} <a href="{{ member.linkedin }}" target="_blank"><i class="fa fa-linkedin-square fa-2x"></i></a> {% endif %}
  {% if member.twitter %}<a href="{{ member.twitter }}" target="_blank"><i class="fa fa-twitter-square fa-2x"></i></a> {% endif %}
  {% if member.education1 %} <p> {{ member.education1 }} </p> {% endif %}
  {% if member.education2 %} <p> {{ member.education2 }} </p> {% endif %}
  {% if member.education3 %} <p> {{ member.education3 }} </p> {% endif %}
</div>
</div>
</div>


{% endfor %}

