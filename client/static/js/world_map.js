document.addEventListener('DOMContentLoaded', () => {
    const cuisineLocations = [
        {label: "Italian", name: "Italian", lat: 41.8719, lng: 12.5674},
        {label: "Asian", name: "Asian", lat: 34.0479, lng: 100.6197},
        {label: "American", name: "American", lat: 37.0902, lng: -95.7129},
        {label: "Mexican", name: "Mexican", lat: 23.6345, lng: -102.5528},
        {label: "Mediterranean", lat: 35.1264, lng: 33.4299},
        {label: "Pakistani", name: "Pakistani", lat: 30.3753, lng: 69.3451},
        {label: "Japanese", name: "Japanese", lat: 36.2048, lng: 138.2529},
        {label: "Moroccan", name: "Moroccan", lat: 31.7917, lng: -7.0926},
        {label: "Korean", name: "Korean", lat: 35.9078, lng: 127.7669},
        {label: "Greek", name: "Greek", lat: 39.0742, lng: 21.8243},
        {label: "Thai", name: "Thai", lat: 15.8700, lng: 100.9925},
        {label: "Indian", name: "Indian", lat: 20.5937, lng: 78.9629},
        {label: "Turkish", name: "Turkish", lat: 38.9637, lng: 35.2433},
        {label: "Smoothie", name: "Smoothie", lat: 25.7617, lng: -80.1918},
        {label: "Russian", name: "Russian", lat: 61.5240, lng: 105.3188},
        {label: "Lebanese", name: "Lebanese", lat: 33.8547, lng: 35.8623},
        {label: "Brazilian", name: "Brazilian", lat: -14.2350, lng: -51.9253},
        {label: "Spanish", name: "Spanish", lat: 40.4637, lng: -3.7492},
        {label: "Vietnamese", name: "Vietnamese", lat: 14.0583, lng: 108.2772},
        {label: "Cocktail", name: "Cocktail", lat: -17.7134, lng: 178.0650},
        {label: "Hawaiian", name: "Hawaiian", lat: 19.8968, lng: -155.5828}
    ];

    const globeDiv = document.getElementById('globeViz');

    const globe = Globe()(globeDiv)
        .globeImageUrl('https://cdn.jsdelivr.net/npm/three-globe/example/img/earth-dark.jpg')
        //.hexPolygonsData(cuisineLocations)
        //.hexPolygonResolution(3)
        //.hexPolygonMargin(0.4)
        //.hexPolygonUseDots(true)
        //.hexPolygonColor(() => `#${Math.round(Math.random() * Math.pow(2, 24))
        //.toString(16)
        //.padStart(6, '0')}`)
        //.hexPolygonLabel(({ properties: d }) => `<b>${d.name}</b>`)
        .labelsData(cuisineLocations)
        .labelSize(1.4)
        .labelDotRadius(0.3)
        .labelText('label')
        .pointsData(cuisineLocations)
        .pointAltitude(0.04)
        .pointColor(() => 'white')
        .pointLabel(d => d.name)
        .onPointClick(d => {
            window.location.href = `campaign/${d.name}`
    });

    globe.controls().autoRotate = true;
    globe.controls().autoRotateSpeed = 0.3;
});
//}

function getCuisine(){

}