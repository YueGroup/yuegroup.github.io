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
</style>

<h3 id="people">P</h3>

<h3 id="pi">PI</h3>


<div class="jumbotron">
<!-- Loop through PI members for the first block -->
{% for member in site.data.pi %}
<div class="row">
<div class="col-sm-3">
  <div class="circle-photo">
  <img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" width="100%" style="max-width:250px"/>
  </div>
</div>
<div class="col-sm-9 col-xs-12">
<h4>{{ member.name }}</h4>
<i>{{ member.info }}</i><br>

 <h5>Shuwen Yue</h5>
 <h6><i>Assistant Professor</i>, Robert F. Smith School of Chemical and Biomolecular Engineering, Cornell University <br /><b>Office:</b> Olin Hall 348A <br /><b>Office phone:</b> 607-255-0848 </h6>
 <p><a href="https://www.cheme.cornell.edu/faculty-directory/shuwen-yue" target="_blank"><i class="ai ai-archive-square ai-2x"></i></a>
 <a href="mailto:shuwen.yue@cornell.edu" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a> 
 <a href="/cv/shuwenyue_cv_2023_08_27_2023.pdf" target="_blank"><i class="ai ai-cv-square ai-2x"></i></a> 
 <a href="https://scholar.google.com/citations?user=felc0JkAAAAJ" target="_blank"><i class="ai ai-google-scholar-square ai-2x"></i></a> 
 <a href="https://github.com/shuwenyue" target="_blank"><i class="fab fa-github-square fa-2x"></i></a> 
<ul style="overflow: hidden">
<li> {{ member.education3 }} </li>
<li> {{ member.education2 }} </li>
<li> {{ member.education1 }} </li>
</ul>
</div>
</div>
{% endfor %}
</div>

## Current Students and Postdocs

<div class='jumbotron'>
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-2">
<img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
<div class="col-sm-4 col-xs-12">
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }}<br></i>

  {% if member.website %}<a href="{{ member.website }}" target="_blank"><i class="fa fa-home fa-2x"></i></a> {% endif %}
  {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %}
  {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x"></i></a> {% endif %}
  {% if member.cv %} <a href="{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-2x"></i></a> {% endif %}
  {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-2x"></i></a> {% endif %}
  {% if member.researchgate %} <a href="{{ member.researchgate }}" target="_blank"><i class="ai ai-researchgate-square ai-2x"></i></a> {% endif %}
</div>
<!-- </div> -->

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}
</div>


## Alumni

<div class="jumbotron">
{% assign number_printed = 0 %}
{% for member in site.data.alumni %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-2">
<img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
<div class="col-sm-4 col-xs-12">
  <h4>{{ member.name }}</h4>
  <i>{{ member.duration }} <br> Role: {{ member.info }}</i>
  <ul style="overflow: hidden">
  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}
</div>



