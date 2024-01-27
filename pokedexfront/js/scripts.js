window.onload = function() {
    fetch('http://127.0.0.1:8000/pokemon/list/')
      .then(response => response.json())
      .then(data => {
        let container = document.getElementById('pokemonContainer');
        let row = document.createElement('div');
        row.className = 'row row-cols-2 row-cols-lg-5 g-2 g-lg-3';
        data.forEach(pokemon => {
          let pokemonDiv = document.createElement('div');
          pokemonDiv.className = 'col d-flex justify-content-center';
          let innerDiv = document.createElement('div');
          innerDiv.className = 'p-3 border bg-light text-center';
          innerDiv.style.width = '200px'; // Establece el ancho
          innerDiv.style.height = '225px'; // Establece el alto
          innerDiv.style.borderRadius = '20px'; // Añade bordes redondeados
          innerDiv.style.backgroundColor = '#f8d030'; // Cambia el color de fondo a amarillo
          innerDiv.style.transition = 'transform 0.3s ease-in-out'; // Añade la transición
          let types = pokemon.types.map(type => JSON.parse(type.replace(/'/g, '"')).type.name).join(', ');
          innerDiv.innerHTML = `<p style="color: blue; font-weight: bold;">${pokemon.name}</p>
                                <p>Id: ${pokemon.id}</p>
                                <p>Height: ${pokemon.height}</p>
                                <p>Weight: ${pokemon.weight}</p>
                                <p>Types: ${types}</p>`;
          pokemonDiv.appendChild(innerDiv);
          row.appendChild(pokemonDiv);
        });
        container.appendChild(row);
      })
      .catch(error => console.error('Error:', error));
  };
  
  // Añade el estilo CSS para la transición
  let style = document.createElement('style');
  style.innerHTML = `
    .p-3:hover {
      transform: scale(1.05);
    }
  `;
  document.head.appendChild(style);


