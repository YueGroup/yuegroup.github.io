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
      display: flex;
      flex-direction: column; /* Change to a single column layout */
      align-items: center;
      padding: 0px;
      margin-bottom: 20px;
      align-items: stretch;
    }

    .research-section .research-image img {
      max-width: 100%; /* Image takes full width in single column layout */
      height: auto; /* Maintain aspect ratio */
      align-items: stretch;
    }

    .research-content {
      margin-left: 0; /* Reset margin for single column layout */
      max-width: 100%; /* Text takes full width in single column layout */
    }

    .research-section.reverse-order {
      flex-direction: column-reverse; /* Change the order in single column layout */
    }

  /* Responsive layout for extremely narrow screens */
  @media (max-width: 480px) {

    .research-section .research-image img {
      max-width: 70%; /* Image takes 70% of the width on extremely small screens */
      display: flex;
      flex-direction: column; /* Change to a single column layout */
      align-items: center;
      padding: 20px;
      margin-bottom: 20px;
      align-items: stretch;
  }
}

</style>

<center>
<h3 id="researchtitle">Research</h3>

<!-- Overview graphic -->
<div class="jumbotron">
<div class="col-md-12 col-sm-12 mx-auto">
<br/>
<h4 id="researchtext" style="color: #ded4cc;"><strong> Our computational molecular science toolkit: </strong></h4>
<br/>
<img src="{{ site.url }}{{ site.baseurl }}/images/research0.svg" style="width: 90%;"/>
</div>
</div>


<!-- Research 1: -->
<div class="jumbotron">
  <div class="col-md-12 col-sm-12 mx-auto">
    <div class="research-section reverse-order">
      <img src="{{ site.url }}{{ site.baseurl }}/images/research1.png" alt="Research 1" style="max-width: 450px;" />
      <div class="research-content">
        <h4 style="color: #ded4cc;"><strong>Physics-inspired ML potentials</strong></h4>
        <p style="font-size: 17px;">Molecular simulation is a powerful tool for predicting properties of materials and fluids, but the <em>reliability</em> of these predictions heavily depends on the models used. The challenge in developing these models is a trade-off between the degree of chemical detail (level of theory used) and their computational cost (how fast they can be evaluated on supercomputers). We leverage <em>physics-inspired</em> machine-learning frameworks to build models that avoid this trade-off to predict large-scale thermodynamic properties at first-principles levels of accuracy.</p>
      </div>
    </div>
  </div>
</div>

<!-- Research 2: -->
<div class="jumbotron">
  <div class="col-md-12 col-sm-12 mx-auto">
    <div class="research-section">
      <div class="research-content">
      <h4 style="color: #ded4cc;"><strong>Fluids at interfaces and in confinement</strong></h4>
<p style="text-align: justify; font-size: 17px;"> How molecules behave at an interface or in confinement is <em>vastly different</em> from how they behave in bulk. These types of environments are where analytical theories tend to break down, where timescale trends diverge, and where chemical reactions are more likely to happen. Our group seeks to decipher the intricate relationships between surface features, geometries, and the subsequent influence on fluid behavior. We aim to design unique surfaces and electrolyte chemistry targetting optimal separations and catalysis processes.</p>
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
      <h4 style="color: #ded4cc;"><strong>Generative design for ion transport</strong></h4>
<p style="text-align: justify; font-size: 17px;">A key goal in designing energy storage solutions is to identify solvents which enhance charge transport and stability. We leverage machine-learning tools to map molecular structures to transport properties and optimize for desired properties in lower dimensional spaces. This approach allows us to greatly accelerate the exploration and discovery of <em>new</em> electrolytes chemistry that can unlock ion transport behavior surpassing conventional limitations. </p>
      </div>
    </div>
  </div>
</div>


