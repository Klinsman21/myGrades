const Redis = require("ioredis");

const client = new Redis(process.env.REDIS_PORT, process.env.REDIS_HOST);

client.on('connect', (err) =>{
    console.log("Redis Conectado")
})

// redis
const lerAvisos = (request, response) => {
    client.get("my_grades", (err, res) => {
        if(res != null){
            response.status(200).send(res)
        }
        else{
            response.status(200).send("")
        }
    })
}

const salvarAvisos = async(aviso) => {
    let avisos = []
    avisos.push(aviso)
    let local = await client.get("my_grades")
    if(local != '' && local != null){
        avisos.push(local)
    }
    client.set("my_grades", avisos.toString())
    return true
};

const removerAvisos = async(aviso) => {
    let avisos = await client.get("my_grades")
    avisos = avisos.split(",");
    for (let item = 0; item < avisos.length; item++) {
        if (avisos[item] === aviso) {
            avisos.splice(item, 1); 
        }
    }
    client.set("my_grades", avisos.toString())
    
    return true
};

//client.set("my_grades", '')

module.exports = {salvarAvisos, lerAvisos, removerAvisos};


