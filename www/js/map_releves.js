var map_releves = L.map('map').setView([44.98,1.7315], 13);
create_map(map_releves);
get_network(map_releves,onEach_upReleve);


function onEach_upReleve(feature, layer) {
    if (feature.properties && feature.properties["altitude"]) {
    	var texte = String("Altitude: " + feature.properties["altitude"] + "m");
		layer.bindPopup(texte).on('dblclick', function(e) {oncompteurClick(feature.properties["altitude"]);});
    }
}


//modifier cette fonction pour mettre à jour la borne quand on entre un relevé.
function oncompteurClick(aze) {
	alert(aze);
}