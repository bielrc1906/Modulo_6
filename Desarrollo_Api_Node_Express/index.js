const express = require('express');
const app = express();
const axios = require('axios');
const mongoose = require('mongoose');
const cookieParser = require('cookie-parser');

app.use(cookieParser())

const PORT = 3000;

require("./database");

app.use(express.json());


const FactSchema = new mongoose.Schema({
    created_at: { type: String, required: true },
    value: { type: String, required: true },
})

var Fact = mongoose.model('Fact', FactSchema);

app.get('/jokes', async (req, res) => {
    try{
        const favs = await Fact.find();
        res.send(favs);
    }catch(error){
        res.status(500).send({error: error.message})
    }
});


app.get("/jokes/:id", async (req, res) => {
    try {
      const facts = await Fact.findById(req.params.id);
      if (!facts) {
        return res.status(404).send({ error: "Broma no existente" });
      }
      res.send(facts);
    } catch (error) {
      res.status(500).send({ error: error.message });
    }
  });

  
app.get('/jokes_por_tiempo', async (req, res) => {
try{
    const filtroTime = req.query.time || req.cookies.lastTime|| null;
    const filtro = filtroTime ? {created_at: filtroTime} : {};
    if(filtroTime){
        res.cookie('lastTime', filtroTime);
    }
    const facts = await Fact.find(filtro);
    res.send(facts);
}catch(error){
    res.status(500).send({error: error.message});
}
});


app.post("/jokes/:category", async (req, res) => {
    try{
        const response = await axios.get(
            `https://api.chucknorris.io/jokes/random?${req.params.category}`
          );
          const resp = response.data
          const addFact = Fact(resp);
          await addFact.save();
          res.status(201).send(addFact);
    }catch(error){
        res.status(400).send({error: error.message})
    }
});


app.delete('/jokes/:id', async (req, res) => {
    try{
        const facts = await Fact.findByIdAndDelete(req.params.id);
        if (!facts){
            return res.status(404).send({error: 'Broma no encontrada'});
        }
        res.send(facts);
    }catch(error){
        res.status(500).send({error: error.message});
    }
});

app.put('/jokes/:id', async (req, res) => {
    try{
        const fact = await Fact.findByIdAndUpdate(req.params.id, req.body);
        if(!fact) {
            return res.status(404).send({error: 'Broma no encontrada'});
        }
        res.send(fact);
    }catch(error){
        res.status(500).send({error: error.message});
    }
});


app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`)
});