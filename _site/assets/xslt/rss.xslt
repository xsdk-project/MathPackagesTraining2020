<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" >
<xsl:output method="html" encoding="utf-8" />
<xsl:template match="/rss">
	<xsl:text disable-output-escaping="yes">&lt;!DOCTYPE html &gt;</xsl:text>
	<html>
	<head>
		<xsl:text disable-output-escaping="yes"><![CDATA[
		<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>RSS Feed (Styled)</title>

    <link rel="stylesheet" type="text/css" href="http://localhost:4000/assets/css/styles_feeling_responsive.css">

  

	<script src="http://localhost:4000/assets/js/modernizr.min.js"></script>

	<script src="https://ajax.googleapis.com/ajax/libs/webfont/1.5.18/webfont.js"></script>
	<script>
		WebFont.load({
			google: {
				families: [ 'Lato:400,700,400italic:latin', 'Volkhov::latin' ]
			}
		});
	</script>

	<noscript>
		<link href='http://fonts.googleapis.com/css?family=Lato:400,700,400italic%7CVolkhov' rel='stylesheet' type='text/css'>
	</noscript>


	<!-- Search Engine Optimization -->
	<meta name="description" content="Software Carpentry Style Lessons for Numerical Libraries">
	<meta name="google-site-verification" content="Vk0IOJ2jwG_qEoG7fuEXYqv0m2rLa8P778Fi_GrsgEQ">
	<meta name="msvalidate.01" content="0FB4C028ABCF07C908C54386ABD2D97F" >
	
	<link rel="author" href="https://plus.google.com/u/0/118311555303973066167">
	
	
	<link rel="canonical" href="http://localhost:4000/assets/xslt/rss.xslt">


	<!-- Facebook Open Graph -->
	<meta property="og:title" content="RSS Feed (Styled)">
	<meta property="og:description" content="Software Carpentry Style Lessons for Numerical Libraries">
	<meta property="og:url" content="http://localhost:4000/assets/xslt/rss.xslt">
	<meta property="og:locale" content="en_EN">
	<meta property="og:type" content="website">
	<meta property="og:site_name" content="ATPESC 2018 Math Library Hands On Exercises">
	
	<meta property="article:author" content="https://www.facebook.com/phlow.media">


	
	<!-- Twitter -->
	<meta name="twitter:card" content="summary">
	<meta name="twitter:site" content="phlow">
	<meta name="twitter:creator" content="phlow">
	<meta name="twitter:title" content="RSS Feed (Styled)">
	<meta name="twitter:description" content="Software Carpentry Style Lessons for Numerical Libraries">
	
	

	<link type="text/plain" rel="author" href="http://localhost:4000/humans.txt">

	

	

	<link rel="icon" sizes="32x32" href="http://localhost:4000/assets/img/favicon-32x32.png">

	<link rel="icon" sizes="192x192" href="http://localhost:4000/assets/img/touch-icon-192x192.png">

	<link rel="apple-touch-icon-precomposed" sizes="180x180" href="http://localhost:4000/assets/img/apple-touch-icon-180x180-precomposed.png">

	<link rel="apple-touch-icon-precomposed" sizes="152x152" href="http://localhost:4000/assets/img/apple-touch-icon-152x152-precomposed.png">

	<link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://localhost:4000/assets/img/apple-touch-icon-144x144-precomposed.png">

	<link rel="apple-touch-icon-precomposed" sizes="120x120" href="http://localhost:4000/assets/img/apple-touch-icon-120x120-precomposed.png">

	<link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://localhost:4000/assets/img/apple-touch-icon-114x114-precomposed.png">

	
	<link rel="apple-touch-icon-precomposed" sizes="76x76" href="http://localhost:4000/assets/img/apple-touch-icon-76x76-precomposed.png">

	<link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://localhost:4000/assets/img/apple-touch-icon-72x72-precomposed.png">

	<link rel="apple-touch-icon-precomposed" href="http://localhost:4000/assets/img/apple-touch-icon-precomposed.png">	

	<meta name="msapplication-TileImage" content="http://localhost:4000/assets/img/msapplication_tileimage.png">

	<meta name="msapplication-TileColor" content="#fabb00">


	

        

		]]></xsl:text>
	</head>
	<body id="top-of-page">
		<xsl:text disable-output-escaping="yes"><![CDATA[
		
<div id="navigation" class="sticky">
  <nav class="top-bar" role="navigation" data-topbar>
    <ul class="title-area">
      <li class="name">
      <h1 class="show-for-small-only"><a href="http://localhost:4000" class="icon-tree"> ATPESC 2018 Math Library Hands On Exercises</a></h1>
    </li>
       <!-- Remove the class "menu-icon" to get rid of menu icon. Take out "Menu" to just have icon alone -->
      <li class="toggle-topbar menu-icon"><a href="#"><span>Nav</span></a></li>
    </ul>
    <section class="top-bar-section">

      <ul class="right">
        
              

              

          
          
        
              

              

          
          
        
              

              

          
          
        
              

              

          
          
        
        
      </ul>

      <ul class="left">
        
              

              

          
          

            
            

              <li class="has-dropdown">
                <a  href="http://localhost:4000/">Intro</a>

                  <ul class="dropdown">
                    

                      

                      <li><a  href="http://localhost:4000/about_your_day/">About Your Day</a></li>
                    

                      

                      <li><a  href="http://localhost:4000/setup_instructions/">Setup Instructions</a></li>
                    

                      

                      <li><a  href="http://localhost:4000/atpesc_2018_agenda/">Today&#39;s Agenda</a></li>
                    

                      

                      <li><a  href="https://www.alcf.anl.gov/user-guides" target="_blank">ALCF User Guides</a></li>
                    

                      

                      <li><a  href="https://hangouts.google.com/group/wuWDDdPe4mX1u0v83" target="_blank">Open Chat</a></li>
                    

                      

                      <li><a  href="http://localhost:4000/pages/one_on_one_schedule.html">One-on-One Schedule</a></li>
                    

                      

                      <li><a  href="https://goo.gl/forms/B7UFpBvEOJbC58oJ2" target="_blank">Submit a Show Your Work</a></li>
                    
                  </ul>

              </li>
              <li class="divider"></li>
            
          
        
              

              

          
          

            
            

              <li class="has-dropdown">
                <a  href="http://localhost:4000/lessons/">Lessons</a>

                  <ul class="dropdown">
                    

                      

                      <li><a  href="http://localhost:4000/lessons/hand_coded_heat/">Hand Coded Heat</a></li>
                    

                      

                      <li><a  href="http://localhost:4000/lessons/mfem_convergence/">Meshing and Discretization (MFEM)</a></li>
                    

                      

                      <li><a  href="http://localhost:4000/lessons/pumi/">MFEM+PUMI Adaptive Workflow</a></li>
                    

                      

                      <li><a  href="http://localhost:4000/lessons/time_integrators/">Time Integration &amp; Non-Linear Solvers</a></li>
                    

                      

                      <li><a  href="http://localhost:4000/lessons/krylov_amg/">Krylov Solvers and Algebraic Multigrid</a></li>
                    

                      

                      <li><a  href="http://localhost:4000/lessons/superlu_mfem/">Sparse Direct Solvers</a></li>
                    

                      

                      <li><a  href="http://localhost:4000/lessons/adjoint/">Numerical Optimization (Adjoint)</a></li>
                    

                      

                      <li><a  href="http://localhost:4000/lessons/obstacle_tao">Numerical Optimization</a></li>
                    
                  </ul>

              </li>
              <li class="divider"></li>
            
          
        
              

              

          
          

            
            

              <li class="has-dropdown">
                <a  href="https://fastmath-scidac.org/software-catalog.html" target="_blank">Packages</a>

                  <ul class="dropdown">
                    

                      

                      <li><a  href="http://mfem.org" target="_blank">MFEM</a></li>
                    

                      

                      <li><a  href="https://www.scorec.rpi.edu/pumi" target="_blank">PUMI</a></li>
                    

                      

                      <li><a  href="https://www.mcs.anl.gov/petsc/" target="_blank">PETSc</a></li>
                    

                      

                      <li><a  href="https://computation.llnl.gov/projects/hypre-scalable-linear-solvers-multigrid-methods" target="_blank">HYPRE</a></li>
                    

                      

                      <li><a  href="http://crd-legacy.lbl.gov/~xiaoye/SuperLU" target="_blank">SuperLU</a></li>
                    

                      

                      <li><a  href="http://www.mcs.anl.gov/research/projects/tao/tao-deprecated/index.html" target="_blank">Tao</a></li>
                    
                  </ul>

              </li>
              <li class="divider"></li>
            
          
        
              

              

          
          

            
            

              <li class="has-dropdown">
                <a  href="http://localhost:4000/contributing_guide/">Contributing</a>

                  <ul class="dropdown">
                    

                      

                      <li><a  href="http://localhost:4000/contributing_guide/">Contributing Guide</a></li>
                    

                      

                      <li><a  href="http://localhost:4000/info/">Why the new theme?</a></li>
                    

                      

                      <li><a  href="http://localhost:4000/headers/">Many Header Styles</a></li>
                    

                      

                      <li><a  href="http://localhost:4000/design/">Many Design Options</a></li>
                    

                      

                      <li><a  href="http://localhost:4000/documentation/">Full Documentation</a></li>
                    
                  </ul>

              </li>
              <li class="divider"></li>
            
          
        
        
      </ul>
    </section>
  </nav>
</div><!-- /#navigation -->

		

<div id="masthead-no-image-header">
	<div class="row">
		<div class="small-12 columns">
			<a id="logo" href="http://localhost:4000/" title="ATPESC 2018 Math Library Hands On Exercises – So my code will see the future">
				<img src="http://localhost:4000/assets/img/logo.png" alt="ATPESC 2018 Math Library Hands On Exercises – So my code will see the future">
			</a>
		</div><!-- /.small-12.columns -->
	</div><!-- /.row -->
</div><!-- /#masthead -->








		


<div class="alert-box warning text-center"><p>This <a href="https://en.wikipedia.org/wiki/RSS" target="_blank">RSS feed</a> is meant to be used by <a href="https://en.wikipedia.org/wiki/Template:Aggregators" target="_blank">RSS reader applications and websites</a>.</p>
</div>



		]]></xsl:text>
		<header class="t30 row">
	<p class="subheadline"><xsl:value-of select="channel/description" disable-output-escaping="yes" /></p>
	<h1>
		<xsl:element name="a">
			<xsl:attribute name="href">
				<xsl:value-of select="channel/link" />
			</xsl:attribute>
			<xsl:value-of select="channel/title" disable-output-escaping="yes" />
		</xsl:element>
	</h1>
</header>
<ul class="accordion row" data-accordion="">
	<xsl:for-each select="channel/item">
		<li class="accordion-navigation">
			<xsl:variable name="slug-id">
				<xsl:call-template name="slugify">
					<xsl:with-param name="text" select="guid" />
				</xsl:call-template>
			</xsl:variable>
			<xsl:element name="a">
				<xsl:attribute name="href"><xsl:value-of select="concat('#', $slug-id)"/></xsl:attribute>
				<xsl:value-of select="title"/>
				<br/>
				<small><xsl:value-of select="pubDate"/></small>
			</xsl:element>
			<xsl:element name="div">
				<xsl:attribute name="id"><xsl:value-of select="$slug-id"/></xsl:attribute>
				<xsl:attribute name="class">content</xsl:attribute>
				<h1>
					<xsl:element name="a">
						<xsl:attribute name="href"><xsl:value-of select="link"/></xsl:attribute>
						<xsl:value-of select="title"/>
					</xsl:element>
				</h1>
				<xsl:value-of select="description" disable-output-escaping="yes" />
			</xsl:element>
		</li>
	</xsl:for-each>
</ul>

		<xsl:text disable-output-escaping="yes"><![CDATA[
		    <div id="up-to-top" class="row">
      <div class="small-12 columns" style="text-align: right;">
        <a class="iconfont" href="#top-of-page">&#xf108;</a>
      </div><!-- /.small-12.columns -->
    </div><!-- /.row -->


    <footer id="footer-content" class="bg-grau">
      <div id="footer">
        <div class="row">
          <div class="medium-6 large-5 columns">
            <h5 class="shadow-black">About This Site</h5>

            <p class="shadow-black">
              <a href="https://software-carpentry.org">Software Carpentry</a> Style Lessons for Numerical Libraries
              <a href="http://localhost:4000/info/">More ›</a>
              Created by <a href="https://github.com/markcmiller86">Mark C Miller</a> with <a href="http://jekyllrb.com/" target="_blank">Jekyll</a> based on <a href="http://phlow.github.io/feeling-responsive/">Feeling Responsive</a>.</p>
            </p>
          </div><!-- /.large-6.columns -->

          <div class="small-6 medium-3 large-3 columns">
            <ul class="inline-list social-icons">
            
              <li><a href="https://fastmath-scidac.llnl.gov" target="_blank" class="icon-home" title="FASTMath"></a></li>
            
              <li><a href="https://www.youtube.com/playlist?list=PLGj2a3KTwhRZKjI7pRFxQDBORsswJAdJt" target="_blank" class="icon-youtube" title="ATPESC-2017 Numerical Libaries"></a></li>
            
              <li><a href="https://www.youtube.com/channel/UCEkJLPAMOUsjC_RXGFcVq-A/videos" target="_blank" class="icon-youtube" title="IDEAS on YouTube"></a></li>
            
              <li><a href="http://twitter.com/exascaleproject" target="_blank" class="icon-twitter" title="Exascale Project on Twitter"></a></li>
            
            </ul>

                        <a class="button left r15 tiny radius" href="https://github.com/xsdk-project/ATPESC2018HandsOnLessons/edit/gh-pages/assets/xslt/rss.xslt">Edit This Page On GitHub</a>



          </div><!-- /.large-3.columns -->
        </div><!-- /.row -->

      </div><!-- /#footer -->

    </footer>

		


<script src="http://localhost:4000/assets/js/javascript.min.js"></script>














		]]></xsl:text>
	</body>
	</html>
</xsl:template>
<xsl:template name="slugify">
	<xsl:param name="text" select="''" />
	<xsl:variable name="dodgyChars" select="' ,.#_-!?*:;=+|&amp;/\\'" />
	<xsl:variable name="replacementChar" select="'-----------------'" />
	<xsl:variable name="lowercase" select="'abcdefghijklmnopqrstuvwxyz'" />
	<xsl:variable name="uppercase" select="'ABCDEFGHIJKLMNOPQRSTUVWXYZ'" />
	<xsl:variable name="lowercased"><xsl:value-of select="translate( $text, $uppercase, $lowercase )" /></xsl:variable>
	<xsl:variable name="escaped"><xsl:value-of select="translate( $lowercased, $dodgyChars, $replacementChar )" /></xsl:variable>
	<xsl:value-of select="$escaped" />
</xsl:template>
</xsl:stylesheet>
