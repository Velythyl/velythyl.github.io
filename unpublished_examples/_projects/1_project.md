---
layout: page
title: ICLR Blog Track
description: Blog posts as conference publications
img: assets/img/12.jpg
importance: 1
category: work
---


This project was sparked by a conversation I had with the professor of my 
Game Theory & Machine Learning class, Gauthier Gidel. 
We were both feeling frustrated with the amount of glaring cherry picking in 
machine learning papers, and about how incremental results get completely discarded 
as useless, even if they offer important new research insights. Our solution was to
incentivize research blog posts, since they allow smaller results to be published, which 
would help reduce cherry picking and boost the reach of incremental results. 

To do so, we wanted them to be formally recognized as scientific achievements. 
We contacted Sebastien Bubeck (Sr. Principal Research Manager at Microsoft),
Claire Vernade (Research Scientist at DeepMind), and David Dobre
(a friend and a MSc student at Mila). Together, we wrote a proposal to ICLR
proposing they let us organise a new conference track, the Blog Track.
They accepted, and we became inaugural track chairs. Being track chair at such a
huge conference at 24 years of age was an extraordinary experience.

Even though it was the first edition of a blog track for our field, it was a resounding 
success. As inaugural track chairs, we accepted 20 posts out of 61, roughly the size
of the first ICLR conference (which is now one of the big ML conferences). Social media 
was abuzz about this track, with overwhelmingly positive feedback.

{% twitter https://twitter.com/iclr_conf/status/1437460881047175169?lang=ca %}

Recently, ICLR also asked G. Gidel, D. Dobre and I to lead the blog track for 
a second year. I am looking forward to it, as ICLR will be in Rwanda in 2023, and
I strongly believe in organizing conferences outside of the usual North American
and European venues.



During the ICLR Blog Track, participating authors had to select a paper from past ICLR runs. They then wrote a blog post
on it, either clarifying it, expanding it, or painting it in a different light. The proposal and the actual organization
were done in collaboration with Sébastien Bubeck (Microsoft), Claire Vernade (Deepmind), Gauthier Gidel (Mila), and David Dobre (Mila).

The ICLR Blog Track 

This first edition of the Blog Track was wildly successful.


originated from a discussion I had with



Every project has a beautiful feature showcase page.
It's easy to include images in a flexible 3-column grid format.
Make your photos 1/3, 2/3, or full width.

To give your project a background in the portfolio page, just add the img tag to the front matter like so:

    ---
    layout: page
    title: project
    description: a project with a background image
    img: /assets/img/12.jpg
    ---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/1.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/3.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Caption photos easily. On the left, a road goes through a tunnel. Middle, leaves artistically fall in a hipster photoshoot. Right, in another hipster photoshoot, a lumberjack grasps a handful of pine needles.
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    This image can also have a caption. It's like magic.
</div>

You can also put regular text between your rows of images.
Say you wanted to write a little bit about your project before you posted the rest of the images.
You describe how you toiled, sweated, *bled* for your project, and then... you reveal it's glory in the next row of images.


<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.html path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.html path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    You can also have artistically styled 2/3 + 1/3 images, like these.
</div>


The code is simple.
Just wrap your images with `<div class="col-sm">` and place them inside `<div class="row">` (read more about the <a href="https://getbootstrap.com/docs/4.4/layout/grid/">Bootstrap Grid</a> system).
To make images responsive, add `img-fluid` class to each; for rounded corners and shadows use `rounded` and `z-depth-1` classes.
Here's the code for the last row of images above:

{% raw %}
```html
<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.html path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.html path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
```
{% endraw %}
