var map_compteur = L.map('map').setView([44.98,1.7315], 13);
create_map(map_compteur);
//get_network(map_network,onEach_popup,null);

var popup = L.popup();
map_compteur.on('click', onMapClick);

/*function onEach_popup(feature, layer) {
    if (feature.properties && feature.properties["altitude"]) {
		layer.on('click', function(e) {oncompteurClick(feature.properties["id"]);});
    }
}*/

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("latitude: "+e.latlng.lat.toFixed(5) + ",  longitude: "+e.latlng.lng.toFixed(5))
        .openOn(map_compteur);
    update_lat_lon_field(e.latlng.lat.toFixed(5), e.latlng.lng.toFixed(5));
}

function add_marker(lat,lon,texte) {
L.marker([lat,lon]).addTo(map_compteur)
	.bindPopup(texte).openPopup();
}