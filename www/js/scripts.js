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

/*filter conso by date*/
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

/*change default text inputf for index debut releve*/
function update_index_deb_releve(id_compteur) {
   $.ajax({
		type:"get",
		url:'../page_releves.py/part_index_debut',   // fonction python appelée
		data: {'id_compteur':id_compteur}, // parametres passes a cette fonction
		success:function(reponse){  // recup dans reponse du return fait par la fonction corps_page_connecte
			$("#index_debut_releves").html(reponse);   // maj sur la page 
		},
		error:function(){ alert("erreur lors de la recuperation de la page");}
	}); 
}

/*Change selected compteur in combo box*/
function change_combo_box(id_compteur){
	combo = document.getElementById('combo_compteur_releves')
	var l = combo.options.length;
	var index_combo = 0;
	for (var i=0; i < l; i++){
		var val =  combo.options[i].value;
		if (val == id_compteur) {
			index_combo = i;
		}
	}
	combo.options[index_combo].selected=true;
}

/*update detail compteur on page "Le réseau d'irrigation"*/
function update_details_compteur(id_compteur) {
   $.ajax({
		type:"get",
		url:'../page_reseau.py/detail',   // fonction python appelée
		data: {'id_compteur':id_compteur}, // parametres passes a cette fonction
		success:function(reponse){  // recup dans reponse du return fait par la fonction corps_page_connecte
			$("#detail_compteur").html(reponse);   // maj sur la page 
		},
		error:function(){ alert("erreur lors de la recuperation de la page");}
	}); 
}

/*update info exploitant on page "Gestion des membres"*/
function update_info_exploitant(selec,index) {
	var id_ex =  selec.options[index].value;
   $.ajax({
		type:"get",
		url:'../page_gestion_exploitant.py/get_details',   // fonction python appelée
		data: {'id_ex':id_ex}, // parametres passes a cette fonction
		success:function(reponse){  // recup dans reponse du return fait par la fonction corps_page_connecte
			$("#infosexploitant").html(reponse);   // maj sur la page 
		},
		error:function(){ alert("erreur lors de la recuperation de la page");}
	});
}

/*change exploitant to see conso (for the administrator)*/
function change_exploitant_conso(selec,index) {
	var id_ex =  selec.options[index].value;
	alert(id_ex);
   $.ajax({
		type:"get",
		url:'../page_conso.py/conso_table',   // fonction python appelée
		data: {'date_debut':document.getElementById('date_debut').value, 'date_fin':document.getElementById('date_fin').value, 'id_ex':id_ex}, // parametres passes a cette fonction
		success:function(reponse){  // recup dans reponse du return fait par la fonction corps_page_connecte
			$("#conso_content").html(reponse);   // maj sur la page 
		},
		error:function(){ alert("erreur lors de la recuperation de la page");}
	});
}

function verif_releve(fin_input){
	debut_input = document.getElementById('index_debut')
	var conso = parseInt(fin_input.value) - parseInt(debut_input.value);
	if (conso < 0) {
		alert("Attention, l'index de fin est inférieur à celui de début. Ce relevé n'est pas valide !");
	}
}

function update_exploitant_releve(selec,index){
	var id_ex =  selec.options[index].value;
	$.ajax({
		type:"get",
		url:'../page_releves.py/get_compteur_combo_box',   // fonction python appelée
		data: {'id_ex':id_ex}, // parametres passes a cette fonction
		success:function(reponse){  // recup dans reponse du return fait par la fonction corps_page_connecte
			$("#combo_compteur_releves").html(reponse);   // maj sur la page 
		},
		error:function(){ alert("erreur lors de la recuperation de la page");}
	});
	
	var combo = document.getElementById('combo_compteur_releves')
	var id_compteur = parseInt(combo.options[0].value);
	update_index_deb_releve(id_compteur);
}

function change_combo_box(opt_check){
	$.ajax({
		type:"get",
		url:'../page_evenement.py/get_combo_box',   // fonction python appelée
		data: {'opt_check':opt_check}, // parametres passes a cette fonction
		success:function(reponse){  // recup dans reponse du return fait par la fonction corps_page_connecte
			$("#combo_compteur_evenement").html(reponse);   // maj sur la page 
		},
		error:function(){ alert("erreur lors de la recuperation de la page");}
	});
}

//End document.ready
