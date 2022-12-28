---
# Documentation: https://wowchemy.com/docs/managing-content/

title: When do short-range atomistic machine-learning models fall short?
subtitle: ''
summary: ''
authors:
- sy593
- Maria Carolina Muniz
- Marcos F Calegari Andrade
- Linfeng Zhang
- Roberto Car
- Athanassios Z Panagiotopoulos
tags: []
categories: []
date: '2021-01-01'
lastmod: 2022-12-26T21:56:35-06:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2022-12-27T03:56:35.400532Z'
publication_types:
- '2'
abstract: We explore the role of long-range interactions in atomistic machine-learning models by analyzing the effects on fitting accuracy, isolated cluster properties, and bulk thermodynamic properties. Such models have become increasingly popular in molecular simulations given their ability to learn highly complex and multi-dimensional interactions within a local environment; however, many of them fundamentally lack a description of explicit long-range interactions. In order to provide a well-defined benchmark system with precisely known pairwise interactions, we chose as the reference model a flexible version of the Extended Simple Point Charge (SPC/E) water model. Our analysis shows that while local representations are sufficient for predictions of the condensed liquid phase, the short-range nature of machine-learning models falls short in representing cluster and vapor phase properties. These findings provide an improved understanding of the role of long-range interactions in machine learning models and the regimes where they are necessary.
publication: '*The Journal of Chemical Physics*, **154**, 034111. (2021)'
links:
- name: URL
  url: https://aip.scitation.org/doi/10.1063/5.0031215
- name: Video
  url: https://www.youtube.com/watch?v=EMFWuNMs0pk
---
