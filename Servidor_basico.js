const http = require("http");
const url = require("url");

async function getData() {
  const response = await fetch("https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json");
  const data = await response.json();
  return data;
}

handleReq = async (req, res) => {
  // Recogemos el valor del pokemon que introducimos en la url
  Name = decodeURI(req.url.substring(1));
  // Buscamos si existe en la Pokédex
  getData().then((pokemon) => {
      const pokemonfound = pokemon.find((p) => p.id == Name || p.name.english == Name || p.name.japanese == Name || p.name.chinese == Name || p.name.french == Name);
      if(pokemonfound){
        // Si existe devolvemos un JSON con los campos que pide el enunciado
        res.writeHead(200, { "Content-Type": "application/json" });
        res.end(
          JSON.stringify({
            Tipo: pokemonfound.type,
            HP: pokemonfound.base.HP,
            Attack: pokemonfound.base.Attack,
            Defense: pokemonfound.base.Defense,
            "Sp.Attack": pokemonfound.base["Sp. Attack"],
            "Sp.Defense": pokemonfound.base["Sp. Defense"],
            Speed: pokemonfound.base.Speed,
          })
        );
      }else{
        // Si no existe informamos sobre ello
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end('El pokemon no existe en la Pokédex');
      }
    })
    .catch((error) => console.error(error));
};

// Creamos el servidor
const server = http.createServer(handleReq);
server.listen(3000, () => {
  console.log("Servidor escuchando en el puerto 3000");
});