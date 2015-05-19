var map = L.map('map').setView([44.98,1.7315], 13);

//L.tileLayer('https://{s}.tiles.mapbox.com/v3/{id}/{z}/{x}/{y}.png', {
L.tileLayer('http://tile.openstreetmap.org/{z}/{x}/{y}.png', {
	maxZoom: 18,
	attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
		'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
		//'Imagery © <a href="http://mapbox.com">Mapbox</a>',
		'Imagery © <a href="http://openstreetmap.org">OpenSteetMap</a>',
	id: 'examples.map-i875mjb7'
}).addTo(map);


var popup = L.popup();

/*function onMapClick(e) {
	popup
		.setLatLng(e.latlng)
		.setContent("Tu as cliqué ici: " + e.latlng.lat.toString() + ', ' + e.latlng.lng.toString())
		.openOn(map);
}

map.on('click', onMapClick);*/

//addCompteur(44.93405,1.76915,2);
//addCompteur(0,1.76915,2);
//addCompteur(44.93405,1.86915,2);

function addCompteur(lat,lon,alt) {
	if(lat != 0 && lon != 0){
	L.marker([lat,lon]).addTo(map);
	}
}


var tt = get_network(24);
function get_network(id_ex) {
	
   $.ajax({
		type:"get",
		url:'../page_reseau.py/get_json_compteurs',   // fonction python appelée
		data: {'id_ex':id_ex}, // parametres passes a cette fonction
		success:function(reponse){  // recup dans reponse du return fait par la fonction corps_page_connecte
			var donns = $.parseJSON(reponse);
			L.geoJson(donns, {onEachFeature: onEachFeature}).addTo(map);
		},
		error:function(){ alert("erreur lors de la recuperation des données");}
	}); 
}

function onEachFeature(feature, layer) {
    if (feature.properties && feature.properties["altitude"]) {
    	var texte = String("Altitude: " + feature.properties["altitude"] + "m");
		layer.bindPopup(texte);
    }
}