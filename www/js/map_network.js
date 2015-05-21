var map_network = L.map('map').setView([44.98,1.7315], 13);
create_map(map_network);
get_network(map_network,onEach_popup,null);


function onEach_popup(feature, layer) {
    if (feature.properties && feature.properties["altitude"]) {
    	var texte = String("Altitude: " + feature.properties["altitude"] + "m");
		layer.bindPopup(texte).on('click', function(e) {oncompteurClick(feature.properties);});
    }
}

function oncompteurClick(aze) {
	alert(aze);
}