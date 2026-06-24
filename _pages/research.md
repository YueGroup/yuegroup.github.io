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
<h4 id="researchtext" style="color: #E2C8A8;"><strong> Our Mission </strong></h4>
<p style="font-size: 18px;">
We are entering a new era of scientific discovery, where machine learning is transforming how we study and design molecules and materials. Our research focuses on using these advances to understand, predict, and ultimately control chemical behavior across functional materials, catalytic interfaces, and electrochemical systems. A central theme of our work is understanding chemistry in <em>realistic, dynamic, and often messy</em> environments, where fluctuations, collective behavior, and electronic complexity determine chemical outcomes.
</p>
</div>
</div>

<!-- Research 1: -->
<div class="jumbotron">
  <div class="col-md-12 col-sm-12 mx-auto">
    <div class="research-section reverse-order">
      <img src="{{ site.url }}{{ site.baseurl }}/images/research1.png" alt="Research 1" style="max-width: 350px;" />
      <div class="research-content">
        <h4 style="color: #E2C8A8;"><strong>Physics-Aware Machine Learning</strong></h4>
        <p style="font-size: 17px;">Machine learning models are now a routine workhorse for atomistic simulation and molecular design. The real test comes when these models are applied to complex chemical environments. Chemistry in the real world is messy and electronically complicated, and getting these systems right often requires more than just bigger models and more data. Can physical knowledge bridge this gap, and how should it be incorporated? Our group develops <em>physics-aware</em> machine learning algorithms and tools to tackle these challenges, including machine learning interatomic potentials (MLIPs), active learning strategies, and generative models for molecular simulation and design.</p>
      </div>
    </div>
  </div>
</div>

<!-- Research 2: -->
<div class="jumbotron">
  <div class="col-md-12 col-sm-12 mx-auto">
    <div class="research-section">
      <div class="research-content">
      <h4 style="color: #E2C8A8;"><strong>Engineering Functional Materials</strong></h4>
<p style="text-align: justify; font-size: 17px;">Designing better materials can often feel like a game of whack-a-mole. Improving activity may reduce stability, increasing selectivity may decrease conversion, and small changes in composition can lead to dramatically different behavior. Our group studies the molecular and electronic origins of these tradeoffs and looks for opportunities to break them.  We use these insights to guide the forward design of heterogeneous catalysts, 2D materials, and other functional materials for energy and sustainability applications. </p>
      </div>
      <img src="{{ site.url }}{{ site.baseurl }}/images/research2.png" alt="Research 2" style="max-width: 450px;  margin-left: 30px;" />
    </div>
  </div>
</div>



<!-- Research 3: -->
<div class="jumbotron">
  <div class="col-md-12 col-sm-12 mx-auto">
    <div class="research-section reverse-order">
      <img src="{{ site.url }}{{ site.baseurl }}/images/research3.png" alt="Research 3" style="max-width: 300px;" />
      <div class="research-content">
      <h4 style="color: #E2C8A8;"><strong>Engineering Interfaces and Solvents</strong></h4>
<p style="text-align: justify; font-size: 17px;"> Catalysts often get all the attention, but it is only half the story. The surrounding electrolyte can be <em>just as much of a catalyst</em> as the catalyst itself! The challenge is that these environments are dynamic, collective, and often difficult to characterize from experiments alone. Our group combines statistical mechanics and first principles theory to understand how solvents, interfaces, and electric fields determine chemical behavior. We use these insights to engineer new <em>electrolyte</em>-design knobs for controlling catalysis, separations, and electrochemical processes. </p>
      </div>
    </div>
  </div>
</div>


