const Redis = require("ioredis");

const client = new Redis(process.env.REDIS_PORT, process.env.REDIS_HOST);

client.on('connect', (err) =>{
    console.log("Conectado")
})

// redis
const lerAvisos = (request, response) => {
    client.get("my_grades", (err, res) => {
        if(res != null){
            response.status(200).send(res)
        }
        else{
            response.status(200).send("null")
        }
    })
}

const salvarAvisos = (aviso) => {
    let avisos = 
    client.set("my_grades", aviso, 'EX', 7200)
    return true
};

module.exports = {salvarAvisos, lerAvisos};


