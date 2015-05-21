function create_map(my_map) {
//L.tileLayer('https://{s}.tiles.mapbox.com/v3/{id}/{z}/{x}/{y}.png', {
L.tileLayer('http://tile.openstreetmap.org/{z}/{x}/{y}.png', {
	maxZoom: 18,
	attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
		'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
		//'Imagery © <a href="http://mapbox.com">Mapbox</a>',
		'Imagery © <a href="http://openstreetmap.org">OpenSteetMap</a>',
	id: 'examples.map-i875mjb7'
}).addTo(my_map);
};

function get_network(map,fctonfeature,ex) {
   $.ajax({
		type:"get",
		url:'../page_reseau.py/get_json_compteurs',   // fonction python appelée
		data: {'ex':ex}, // parametres passes a cette fonction
		success:function(reponse){  // recup dans reponse du return fait par la fonction corps_page_connecte
			var donns = $.parseJSON(reponse);
			L.geoJson(donns, {onEachFeature: fctonfeature}).addTo(map);
		},
		error:function(){ alert("erreur lors de la recuperation des données");}
	});
}
