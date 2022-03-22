require('dotenv').config();
const{MongoClient} = require('mongodb');

const usuario = new MongoClient(`mongodb://${process.env.MONGO_HOST}:${process.env.MONGO_PORT}`,
    {useUnifiedTopology: true});

async function getLocalizacao(matricula) {
    let latlng = [];
    try {
        await usuario.connect();
        const database = usuario.db(process.env.MONGO_DATABASE);
        const localizacoes = database.collection('localizacao');

        await localizacoes.find({'matricula': matricula}).forEach(p => latlng.push(p));
    }
    finally {
        await usuario.close();
        return latlng;
    }
}

async function deleteLocalizacao(matricula) {
    try {
        await usuario.connect();
        const database = usuario.db(process.env.MONGO_DATABASE);
        const localizacoes = database.collection('localizacao');

        await localizacoes.deleteOne({"matricula": matricula})
    }
    finally {
        await usuario.close();
    }
}

const obterLocalizacao = async(request, response) => {
    const matricula = request.params.matricula;
    let latlng = await getLocalizacao(matricula);
    response.status(200).json(latlng);
}

async function salvarLocalizacao(obj) {
    try {
        await usuario.connect();
        const database = usuario.db(process.env.MONGO_DATABASE);
        const localizacoes = database.collection('localizacao');

        await localizacoes.insertOne(obj).then(console.log('OK'))
    }
    finally {
        await usuario.close();
        return true;
    }
}


module.exports = {obterLocalizacao, salvarLocalizacao, deleteLocalizacao};

