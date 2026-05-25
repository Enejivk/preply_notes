
const musicData = {
    "volume": "Blaring",
    "current": {
        "band": "rednex",
        "song": "cotton eye joe",
        "members": [
            {"firstName": "Kent", "lastName": "Olander"},
            {"firstName": "Urban", "lastName": "Lundgren"},
            {"firstName": "Jonas", "lastName": "Lundstrom"},
            {"firstName": "Tor", "lastName": "Nilsson"}
        ]
    },
    "next": {
        "band": "the dubliners",
        "song": "finnegan's wake",
        "members": [
            {"firstName": "Ronnie", "lastName": "Drew"},
            {"firstName": "Luke", "lastName": "Kelly"},
            {"firstName": "Ciaran", "lastName": "Bourke"},
            {"firstName": "Barney", "lastName": "McKenna"}
        ]
    }
}


let arr = new Array();

console.log(musicData.current.members[0].firstName);
