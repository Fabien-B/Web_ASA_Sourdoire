var map_releves = L.map('map').setView([44.98,1.7315], 13);
create_map(map_releves);
get_network(map_releves,onEach_upReleve);


function onEach_upReleve(feature, layer) {
    if (feature.properties && feature.properties["altitude"]) {
    	var texte = String("Altitude: " + feature.properties["altitude"] + "m");
		layer.on('click', function(e) {oncompteurClick(this,feature.properties["id"]);});
    }
}


//modifier cette fonction pour mettre à jour la borne quand on entre un relevé.
function oncompteurClick(compteur,id_compteur) {
	change_combo_box(id_compteur);
	update_index_deb_releve(-1,id_compteur);
	compteur.setIcon(selectedIcon);
}