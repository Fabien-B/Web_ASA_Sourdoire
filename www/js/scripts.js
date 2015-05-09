/**
 * icebrrrg.js
 * 
 * The main javascript for Icebrrrg.
 * 
 * Copyright 2012 Opendesigns.
 * http://www.opendesigns.org/design/icebrrrg/
 * 
 */

jQuery(document).ready(function(){
	
	$("#update_releves").click(update_conso);
	
/* FLEX SLIDER */
	var $flexSlider = $('.flexslider');
	$flexSlider.flexslider({
		animation: "slide",
		controlsContainer: ".flex-container",
		prevText: "&larr;",
		nextText: "&rarr;",
		controlNav: false,
directionNav: true,
		before:	function($slider){
			$slider.find('.flex-caption').fadeOut('fast');			
		},
		after: function($slider){
			$slider.find('.flex-caption').fadeIn();			
		},
		
	});
	
	
  $(window).load(function() {
    $('.flexslider').flexslider({
			animation: "slide",
          controlsContainer: ".flex-container"
	});
  });
	
	/* prettyPhoto */
	
	$("a[rel^='prettyPhoto']").prettyPhoto({
		
		social_tools: false,
		
		
	});
	
});

function update_conso() {
   $.ajax({
		type:"get",
		url:'../page_conso.py/conso_table',   // fonction python appelée
		data: {'date_debut':document.getElementById('date_debut').value, 'date_fin':document.getElementById('date_fin').value}, // parametres passes a cette fonction
		success:function(reponse){  // recup dans reponse du return fait par la fonction corps_page_connecte
			$("#conso_content").html(reponse);   // maj sur la page 
		},
		error:function(){ alert("erreur lors de la recuperation de la page");}
	});	   
}

//End document.ready
