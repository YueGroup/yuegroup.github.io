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
    border: 5px solid grey;
    /* #ded4cc */

  }

  .circle-icon {
    border-radius: 50%;
    background-color: #f2f2f2;
    padding: 10px;
    text-align: center;
    border: thick thin;
    border-color: gray;
  }

  /* Customize the heading styles */
  h3#pi,
  h3#current-students {
    font-size: 24px; /* Adjust the font size as needed */
    text-align: center;
    margin: 20px 0; /* Add some margin for spacing */
    font-weight: bold; /* Make the text bold */
  }

  .member-group {
  margin-bottom: 20px; /* Adjust this value to control the vertical spacing */
}
</style>

<h3 id="pi">Principle Investigator</h3>

{% for member in site.data.pi %}

<div class="jumbotron">
<div class="row">
<div class="col-sm-3">
<div class="circle-photo">
  <img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" width="80%" style="max-width:250px"/>
</div>
</div>
<div class="col-sm-9 col-xs-12">
<h4>{{ member.name }}</h4>
<i>{{ member.info }}</i>
<p> {{ member.location }} </p>
{% if member.website %}<a href="{{ member.website }}" target="_blank"><i class="ai ai-archive-square ai-2x"></i></a> {% endif %} {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %} {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x"></i></a> {% endif %} {% if member.cv %} <a href="{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-2x"></i></a> {% endif %} {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-2x"></i></a> {% endif %} {% if member.twitter %}<a href="{{ member.twitter }}" target="_blank"><i class="fa fa-twitter-square fa-2x"></i></a> {% endif %}
<p> {{ member.education1 }} </p>
<p> {{ member.education2 }} </p>
<p> {{ member.education3 }} </p>
</div>
</div>
</div>

{% endfor %}


<h3 id="current-students">Group Members</h3>

<div class='jumbotron'>
{% assign number_printed = 0 %}
{% for member in site.data.people %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row member-group"> <!-- Add the "member-group" class here -->
{% endif %}

<div class="col-sm-2 text-center">
<div class="circle-photo">
<img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
</div>
<div class="col-sm-4 col-xs-12">
  <h4>{{ member.name }}</h4>
  <p>{% if member.info1 %} <i> {{ member.info1 }} </i> {% endif %}</p>
  <p>{% if member.info2 %} <i> {{ member.info2 }} </i> {% endif %}</p>
  <p> {{ member.location }} </p>
  {% if member.website %}<a href="{{ member.website }}" target="_blank"><i class="fa fa-home fa-2x"></i></a> {% endif %} {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %} {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x"></i></a> {% endif %} {% if member.cv %} <a href="{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-2x"></i></a> {% endif %} {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-2x"></i></a> {% endif %} {% if member.linkedin %} <a href="{{ member.linkedin }}" target="_blank"><i class="fa fa-linkedin-square fa-2x"></i></a> {% endif %} {% if member.twitter %}<a href="{{ member.twitter }}" target="_blank"><i class="fa fa-twitter-square fa-2x"></i></a> {% endif %}
  {% if member.education1 %} <p> {{ member.education1 }} </p> {% endif %}
  {% if member.education2 %} <p> {{ member.education2 }} </p> {% endif %}
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

<div class="jumbotron">
<div class="col-md-12 col-sm-12 mx-auto">
<h5 style="font-size: 18px; margin-bottom: 10px; color: #f6d635"><b>Group Openings -- We are looking for highly motivated, creative, and independent researchers to join our team!</b> </h5>

<p style="font-size: 18px;">
<strong>Postdocs:</strong> We currently have multiple postdoc positions open for Summer/Fall 2025. Candidates skilled in <em><strong>machine learning</strong></em> and <em><strong>advanced sampling techniques</strong></em> in particular are strongly encouraged to apply. Please send Shuwen a CV, research summary, and contact info for 3 references. Candidates are also encouraged to apply for the <a href='https://science.ai.cornell.edu/schmidt-postdoc-fellows/' style='color: #A1CF8D;'>Schmidt AI in Science Postdoctoral Fellowship</a>, <a href='https://postdocs.cornell.edu/prospective-postdocs/cornell-postdoctoral-fellowship-programs/' style='color: #A1CF8D;'>Cornell internal postdoc fellowships</a>, and <a href='https://research.jhu.edu/rdt/funding-opportunities/postdoctoral/' style='color: #A1CF8D;'>external postdoc fellowships</a>.
</p>

<p style="font-size: 18px;">
<strong>Grad students:</strong> We welcome interested students from chemical engineering, chemistry, materials science, mechanical engineering, computer science, and beyond! All prospective grad students must be admitted through <a href='https://gradschool.cornell.edu/admissions/' style='color: #A1CF8D;'>department level admissions</a> before being considered for a specific research group.
</p>
</div>
</div>

