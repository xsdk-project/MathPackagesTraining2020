---
layout: page
show_meta: false
title: "Viewing Changes Locally"
subheadline: "Detailed instructions in viewing changes locally"
header:
   image_fullwidth: "mesh2.jpg"
permalink: "/how_to_preview_locally/"
---

## Requirements

* github-pages
* bundler
* jekyll

The recommended way of installing these is to use **gem**, the [Ruby](https://www.ruby-lang.org/en/) package manager.

```
$ gem install github-pages
$ gem install bundler
$ gem install jekyll
```

But Ruby version 2.1.0 or higher is required. The version can be checked with
```
$ ruby -v
```

The native Ruby on my Mac (Sierra 10.12.6) is 2.0. So I took the following steps to upgrade it.

1. Open your terminal and run
```
$ \curl -sSL https://get.rvm.io | bash -s stable
```
When this is complete, you need to restart your terminal for the rvm to work.
1. Run
```
$ rvm install ruby-2.4
```
Type ruby -v in the terminal, if it is 2.4, you are done.
1. If it still shows ruby 2.0, run
```
$ rvm use ruby-2.4
```
To set this as the default version, run
```
$ rvm use ruby-2.4 --default
```

## Preview your work using a brower

1. Navigate into the **root** directory of the project
1. Run Jekyll locally
```
$ bundle exec jekyll serve --config _config.yml,_config_dev.yml
Configuration file: _config.yml
Configuration file: _config_dev.yml
Configuration file: _config.yml
Configuration file: _config_dev.yml
            Source: /Users/miller86/fastmath/atpesc17_examples/feeling-responsive
       Destination: /Users/miller86/fastmath/atpesc17_examples/feeling-responsive/_site
 Incremental build: disabled. Enable with --incremental
      Generating... 
                    done in 4.156 seconds.
 Auto-regeneration: enabled for '/Users/miller86/fastmath/atpesc17_examples/feeling-responsive'
Configuration file: _config.yml
Configuration file: _config_dev.yml
    Server address: http://127.0.0.1:4000/
  Server running... press ctrl-c to stop.
```
1. Open your browser, preview the local site at **http://127.0.0.1:4000**
