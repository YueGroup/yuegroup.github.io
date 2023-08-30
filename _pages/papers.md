---
title: "Papers"
layout: gridlay
sitemap: false
permalink: /papers/
years: [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
---

<div class="jumbotron">

<style>
  /* Customize the heading styles */
  h3#papers {
    font-size: 24px; /* Adjust the font size as needed */
    text-align: center;
    margin: 20px 0; /* Add some margin for spacing */
  }
</style>

<h3 id="papers">Papers</h3>

### Refereed journal articles
{% bibliography --query @article @*[selected!=True] %}

</div>

