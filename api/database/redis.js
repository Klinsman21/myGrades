const Redis = require("ioredis");

const client = new Redis(process.env.REDIS_PORT, process.env.REDIS_HOST);

client.on('connect', (err) =>{
    console.log("Conectado")
})

// redis
const salvarAviso = (disciplina, aviso) => {
    redis.set(disciplina, aviso, 'EX', 7200)
    return true
};

const lerAviso = (request, response) => {
    const disciplina = request.params.disciplina;
    client.get(matricula, (err, res) => {
        if(res != null){
            response.status(200).send(res)
        }
        else{
            response.status(200).send("null")
        }
    })
}


module.exports = {salvarAviso, lerAviso};


