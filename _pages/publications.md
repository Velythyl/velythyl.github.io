---
layout: page
permalink: /publications/
title: publications
description: 
years: [2022]
nav: true
nav_order: 1
---
<!-- _pages/publications.md -->

## Accepted submissions

<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>

## Currently under review

A work on adversarial training for reinforcement learning I first-authored is currently under review


## In progress

- I am currently working on an adversarial learning work for reinforcement learning (as part of my Master's Thesis)
- After that, I will tackle an unsupervised RL setting using trajectory relabeling to enable better exploration for unsupervised reward techniques
