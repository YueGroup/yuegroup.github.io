---
title: "Research"
layout: gridlay
sitemap: false
permalink: /research/
---

<style>

  .jumbotron {
    display: flex;
    flex-direction: column;
    align-items: stretch; /* Stretch the div vertically */
    padding: 20px;
    margin-bottom: 20px;
  }

  /* Customize the heading styles */
  h3#researchtitle {
    font-size: 28px; /* Adjust the font size as needed */
    text-align: center;
    margin: 20px 0; /* Add some margin for spacing */
    font-weight: bold; /* Make the text bold */
  }

  h3#researchtext {
    font-size: 20px; /* Adjust the font size as needed */
    text-align: left;
    margin: 20px 10; /* Add some margin for spacing */
    padding: 10 0px; /* Add padding to the text block for spacing */
  }

  /* Center the container and its content using Flexbox */
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 20px; /* Add margin as needed */
  }

/* Styling for Research Blocks */
  .research-section {
    display: flex;
    align-items: flex-start;
  }

  .research-image {
    max-width: 450px;
    max-height: 100%;
  }

  .research-content {
    flex-grow: 1;
    margin-left: 20px;
    font-size: 16px;
  }

  /* Avoid title overlap */
  .research-section h4 {
    margin-top: 0; /* Reset the top margin to remove overlap */
  }

  /* Improved styling for better readability */
  .research-content p {
    text-align: justify;
    line-height: 1.5;
  }

  /* Heading style for Research Blocks */
  h4 {
    margin-top: 10px;
  }

    /* Divider style */
  .research-divider {
    border-top: 2px solid lightgrey;
    margin-top: 20px;
    margin-bottom: 20px;
  }

  /* Responsive layout for narrow screens */
  @media (max-width: 768px) {
    .research-section {
      flex-direction: column; /* Change to a single column layout */
      align-items: center;
    }

    .research-image {
      max-width: 100%; /* Image takes full width in single column layout */
    }

    .research-content {
      margin-left: 0; /* Reset margin for single column layout */
      max-width: 100%; /* Text takes full width in single column layout */
    }

    .research-section.reverse-order {
      flex-direction: column-reverse; /* Change the order in single column layout */
    }
  }

</style>

<center>
<h3 id="researchtitle">Research</h3>

<!-- Overview graphic -->
<div class="jumbotron">
<div class="col-md-12 col-sm-12 mx-auto">
<br/>
<h3 id="researchtext"> We are a computational research group tackling key challenges in <strong>chemical engineering</strong> and <strong>materials design</strong> using <em>multi-scale modeling, machine learning, and statistical mechanics</em>. We aim to build fundamental understanding of molecular scale driving forces in order design materials with tailored properties for applications in <strong>energy storage, catalysis, and desalination</strong>. </h3>
<br/>
<img src="{{ site.url }}{{ site.baseurl }}/images/research_page.svg" width="100%"/>
</div>
</div>


<!-- Research 1: -->
<div class="jumbotron">
  <div class="col-md-12 col-sm-12 mx-auto">
    <div class="research-section reverse-order">
      <img src="{{ site.url }}{{ site.baseurl }}/images/research1.png" alt="Research 1" style="max-width: 450px;" />
      <div class="research-content">
        <h4><strong>ML potential development</strong></h4>
        <p>Molecular simulation is a powerful tool for predicting properties of materials and fluids, but the <em>reliability</em> of these predictions heavily depends on the models used. The challenge in developing these models is a trade-off between the <strong>degree of chemical detail</strong> (level of theory used) and their <strong>computational cost</strong> (how fast they can be evaluated on supercomputers). Our group is tackling this challenge by leveraging machine-learning frameworks trained on quantum mechanical datasets to build models that can predict large-scale <strong style="font-weight: bold;">thermodynamic properties at first-principles levels of accuracy</strong>.</p>
      </div>
    </div>
  </div>
</div>

<!-- Research 2: -->
<div class="jumbotron">
  <div class="col-md-12 col-sm-12 mx-auto">
    <div class="research-section">
      <div class="research-content">
      <h4><strong>Fluids at interfaces and in confinement</strong></h4>
<p style="text-align: justify;"> How molecules behave at an interface or in confinement is <em>vastly different</em> from how they behave in bulk. These types of environments are where analytical theories tend to break down, where chemical reactions are more likely to happen, where timescale trends diverge. Our group seeks to <strong>unravel the intricate relationship between surface features, geometries, and the subsequent influence on fluid behavior.</strong> Ultimately, we are interested in uniquely designing surfaces toward target fluid properties for separations processes and catalysis.</p>
      </div>
      <img src="{{ site.url }}{{ site.baseurl }}/images/research2.png" alt="Research 2" style="max-width: 400px;" />
    </div>
  </div>
</div>

<!-- Research 3: -->
<div class="jumbotron">
  <div class="col-md-12 col-sm-12 mx-auto">
    <div class="research-section reverse-order">
      <img src="{{ site.url }}{{ site.baseurl }}/images/research3.png" alt="Research 3" style="max-width: 450px;" />
      <div class="research-content">
      <h4><strong>Generative design for ion transport</strong></h4>
<p style="text-align: justify;">A key goal in designing energy storage solutions is to identify solvents which enhance charge transport. Rather than relying on a trial-and-error approach to pinpoint optimal solvent molecular structures, we use <strong>generative machine-learning models to directly perform optimization in low-dimentional spaces.</strong> This approach allows us to inversely design materials and electrolyte structures to target improved charge transport. </p>
      </div>
    </div>
  </div>
</div>


