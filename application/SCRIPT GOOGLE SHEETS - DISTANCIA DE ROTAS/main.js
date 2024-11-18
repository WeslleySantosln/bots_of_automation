function distance() {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getActiveSheet();
    var Inicio = 2;       // Linha de início dos dados
    var colDistancia = 5;  // Coluna onde a distância será armazenada
    var colTempo = 6;      // Coluna onde o tempo será armazenado

    var lr = sheet.getLastRow();

    Logger.log(lr);

    Logger.log("Irá iniciar na linha " + Inicio);

    for (var i = Inicio; i <= lr; i++) {
        var distanciaCelula = sheet.getRange(i, colDistancia).getValue();
        var tempoCelula = sheet.getRange(i, colTempo).getValue();
        
        // Verifica se a célula de distância está vazia
        if (distanciaCelula == "" && tempoCelula == "") {
            var origem = sheet.getRange(i, 1).getValue() + " " + sheet.getRange(i, 2).getValue(); // CIDADE ORIGEM + UF
            var destino = sheet.getRange(i, 3).getValue() + " " + sheet.getRange(i, 4).getValue(); // CIDADE DESTINO + UF

            var mapObj = Maps.newDirectionFinder();
            mapObj.setOrigin(origem);
            mapObj.setDestination(destino);

            try {
                var directions = mapObj.getDirections();

                if (directions && directions.routes && directions.routes.length > 0 && directions.routes[0].legs && directions.routes[0].legs.length > 0) {
                    var km = directions.routes[0].legs[0].distance.value / 1000;
                    var tempo = directions.routes[0].legs[0].duration.text;

                    sheet.getRange(i, colDistancia).setValue(km);
                    sheet.getRange(i, colTempo).setValue(tempo);
                } else {
                    throw new Error("Respostas inesperadas da API");
                }
            } catch (e) {
                Logger.log("Erro ao obter direções para linha " + i + ": " + e.message + ". Origem: " + origem + ", Destino: " + destino);
            }
        }
    }
}
