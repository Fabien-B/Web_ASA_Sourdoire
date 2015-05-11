L.marker([44.93505,1.75915]).addTo(map)
	.bindPopup("<b>Salut les gens!</b><br />Je suis une borne!!!").openPopup();

L.circle([44.92863,1.72367], 200, {
	color: 'red',
	fillColor: '#f03',
	fillOpacity: 0.5
}).addTo(map).bindPopup("Station de pompage");

L.polygon([
	[44.93383,1.76040],
	[44.93717,1.75188],
	[44.93670,1.76000]
]).addTo(map).bindPopup("Truc qui sert à rien.");
