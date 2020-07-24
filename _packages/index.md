---
layout: page
show_meta: false
title: "ATPESC 2020 Packages"
not_active: true
package: false
header:
   image_fullwidth: "llnl_machine.jpg"
permalink: /packages/
---

<table>
{% for item in site.packages %}
    {% if item.package %}
        {% if item.not_active %}
            {% continue %}
        {% endif %}
        <tr>
        <td><a href="{{ site.url }}{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a></td>
        <td>{{ item.teaser }}</td>
        {% if item.website %}
            <td><a href="{{ item.website }}">Website</a></td>
        {% else %}
            <td>N/A</td>
        {% endif %}
        </tr>
    {% endif %}
{% endfor %}
</table>

## Other Numerical Packages
<table>
{% for item in site.packages %}
    {% if item.package %}
        {% if item.not_active %}
            <tr>
            <td><a href="{{ site.url }}{{ site.baseurl }}{{ item.url }}">{{ item.title }}</a></td>
            <td>{{ item.teaser }}</td>
            {% if item.website %}
                <td><a href="{{ item.website }}">Website</a></td>
            {% else %}
                <td>N/A</td>
            {% endif %}
            </tr>
        {% endif %}
    {% endif %}
{% endfor %}
</table>

<!-- * [ButterflyPACK]() -- Fast direct solvers with low-rank and butterfly compression
* [Chombo]() -- Scalable adaptive mesh refinement framework
* [DataTransferKit]() -- Open source library for parallel solution transfer
* [deal.II]() -- Open source finite element library
* [libEnsemble]() -- A Python library to coordinate the evaluation of dynamic ensembles of calculations
* [MAGMA]() -- Linear algebra solvers and spectral decompositions for hardware accelerators 
* [MATSuMoTo]() -- Efficient optimization of computationally-expensive black-box problems
* [PHIST]() -- Hybrid-parallel Iterative Sparse Eigenvalue and linear solvers
* [PLASMA]() -- Linear algebra solvers and spectral decompositions for multicore processors
* [SLEPc]() -- Scalable Library for Eigenvalue Problem Computations
* [Trilinos]() -- Optimal kernels to optimal solutions
* [Zoltan/Zoltan2]() -- Parallel partitioning & load-balancing library -->