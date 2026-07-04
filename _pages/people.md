---
title: "People"
layout: gridlay
sitemap: false
permalink: /people/
---

<style>
  /* Add custom styles here */
  .circle-photo img {
    max-width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    object-position: center;
    border-radius: 0%; /* change this for icon square 0% to circle 50%*/
    border: 2px solid grey;
    /* #ded4cc */

  }

  .circle-photo.contain img {
  object-fit: contain;    /* show whole image */
  }

  .circle-photo.no-border img {
    border: none;
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

  a.alumni-link:hover {
    text-decoration: underline !important;
  }

  .jumbotron h4 {
    color: #E2C8A8;
    font-weight: 700;
}
/* People page icon colors */
.people-icon-email {
  color: #EEE0CB;
}

.people-icon-scholar {
  color: #EEE0CB;
}

.people-icon-cv {
  color: #EEE0CB;
}

.people-icon-github {
  color: #EEE0CB;
}

.people-icon-linkedin {
  color: #EEE0CB;
}

.people-icon-twitter {
  color: #EEE0CB;
}

.people-icon-website {
  color: #EEE0CB;
}
</style>

<h3 id="pi">Principle Investigator</h3>

{% for member in site.data.pi %}

<div class="jumbotron">
<div class="row">
<div class="col-sm-3">
<div class="circle-photo" style="text-align: center;">
  <img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" width="90%" style="max-width:250px"/>
</div>
</div>
<div class="col-sm-9 col-xs-12">
<h4>{{ member.name }}</h4>
<i>{{ member.info }}</i>
{% if member.affiliations %}
{% for affiliation in member.affiliations %}
<i style="color: white; display: block; margin: 0;">{{ affiliation }}</i>
{% endfor %}
{% endif %}
<p> {{ member.location }} </p>
{% if member.website %}<a class="people-icon-website" href="{{ member.website }}" target="_blank"><i class="ai ai-archive-square ai-2x"></i></a> {% endif %} {% if member.email %}<a class="people-icon-email" href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %} {% if member.scholar %} <a class="people-icon-scholar" href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x"></i></a> {% endif %} {% if member.cv %} <a class="people-icon-cv" href="{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-2x"></i></a> {% endif %} {% if member.github %} <a class="people-icon-github" href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-2x"></i></a> {% endif %} {% if member.twitter %}<a class="people-icon-twitter" href="{{ member.twitter }}" target="_blank"><i class="fa fa-twitter-square fa-2x"></i></a> {% endif %}{% if member.linkedin %}<a class="people-icon-linkedin" href="{{ member.linkedin }}" target="_blank"><i class="fa fa-linkedin-square fa-2x"></i></a> {% endif %}
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
<div class="circle-photo {{ member.photo_class }}">
<img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
</div>
<div class="col-sm-4 col-xs-12">
  <h4>{{ member.name }}</h4>
  <p>{% if member.info1 %} <i> {{ member.info1 }} </i> {% endif %}</p>
  <p>{% if member.info2 %} <i> {{ member.info2 }} </i> {% endif %}</p>
  <p> {{ member.location }} </p>
  {% if member.email %}<a class="people-icon-email" href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %}{% if member.scholar %}<a class="people-icon-scholar" href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x"></i></a> {% endif %}{% if member.cv %}<a class="people-icon-cv" href="{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-2x"></i></a> {% endif %}{% if member.github %}<a class="people-icon-github" href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-2x"></i></a> {% endif %}{% if member.linkedin %}<a class="people-icon-linkedin" href="{{ member.linkedin }}" target="_blank"><i class="fa fa-linkedin-square fa-2x"></i></a> {% endif %}{% if member.twitter %}<a class="people-icon-twitter" href="{{ member.twitter }}" target="_blank"><i class="fa fa-twitter-square fa-2x"></i></a> {% endif %}{% if member.website %}<a class="people-icon-website" href="{{ member.website }}" target="_blank"><i class="fa fa-external-link-square fa-2x"></i></a> {% endif %}

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

<!--
<div class="text-center" style="margin-top: 30px;">
  <a class="alumni-link" href="{{ site.baseurl }}/alumni/" style="font-size: 18px; color: #f6d635; text-decoration: none; font-weight: bold;">
    <strong>→ Group Alumni</strong>
  </a>
</div>
-->

</div>


<div class="jumbotron">
<div class="col-md-12 col-sm-12 mx-auto">
<h5 style="font-size: 18px; margin-bottom: 10px; color: #E2C8A8;"><b>Group Openings -- We are looking for highly motivated, creative, and independent researchers to join our team!</b> </h5>

<p style="font-size: 18px;">
<strong>Postdocs:</strong> We currently have a postdoc position open. Candidates skilled in <em><strong>machine learning method development</strong></em> in particular are strongly encouraged to apply. Please send Shuwen a CV and contact info for 2 references. Candidates are also encouraged to apply for the <a href='https://science.ai.cornell.edu/schmidt-postdoc-fellows/' style='color: #A1CF8D;'>Schmidt AI in Science Postdoctoral Fellowship</a>, <a href='https://postdocs.cornell.edu/prospective-postdocs/cornell-postdoctoral-fellowship-programs/' style='color: #A1CF8D;'>Cornell internal postdoc fellowships</a>, and <a href='https://research.jhu.edu/rdt/funding-opportunities/postdoctoral/' style='color: #A1CF8D;'>external postdoc fellowships</a>.
</p>

<p style="font-size: 18px;">
<strong>Grad students:</strong> We welcome interested students from engineering, math, chemistry, physics, computer science, and beyond! All prospective grad students must be admitted through <a href='https://gradschool.cornell.edu/admissions/' style='color: #A1CF8D;'>department level admissions</a> before being considered for a specific research group.
</p>
</div>
</div>

