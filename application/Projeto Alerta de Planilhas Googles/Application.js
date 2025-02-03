function checkLastModification() {
  var spreadsheetId = '1IC';
  var sheetName = 'MAIN';
  var jaInformadoSheetName = 'JA_INFORMADO';
  
  var spreadsheet = SpreadsheetApp.openById(spreadsheetId);
  var sheet = spreadsheet.getSheetByName(sheetName);
  var jaInformadoSheet = spreadsheet.getSheetByName(jaInformadoSheetName);
  
  var data = sheet.getRange(1, 1, sheet.getLastRow(), sheet.getLastColumn()).getValues();
  var headers = data[0];

  var columnsToCheck = [
    {index: 22, subject: "Alerta: o contrato de N° %s está com o seguinte indicativo: %s", body: "O seguinte problema foi encontrado: %s , no contrato de N° %s, foi lançado Por %s, Por favor, verifique!"},
    {index: 23, subject: "Alerta: o contrato de N° %s está com o seguinte indicativo: %s", body: "O seguinte problema foi encontrado: %s , no contrato de N° %s, foi lançado Por %s, Por favor, verifique!"},
    {index: 24, subject: "Alerta: o contrato de N° %s está com o seguinte indicativo: %s", body: "O seguinte problema foi encontrado: %s , no contrato de N° %s, foi lançado Por %s, Por favor, verifique!"}
  ];
  
  for (var i = 1; i < data.length; i++) { 
    var contractNumber = data[i][1]; 
    //Logger.log('Verificando linha: %s', i + 1);

    if (checkIfRowExists(i + 1)) {
      //Logger.log('Linha %s já foi informada. Pulando envio de e-mail.', i + 1);
      continue;
    }

    for (var j = 0; j < columnsToCheck.length; j++) {  
      var column = columnsToCheck[j];
      var columnHeader = headers[column.index]; 
      
      //Logger.log('Verificando coluna: %s (índice %s)', column.index + 1, column.index);
      //Logger.log('Linha %s, Coluna %s (índice %s): %s', i + 1, column.index + 1, column.index, data[i][column.index]);
      
      if (data[i][column.index] == "SIM") {
        //Logger.log('Encontrado "SIM" na linha %s, coluna %s (índice %s)', i + 1, column.index + 1, column.index);
        
        var recipient = 'alertaemissao@.com.br';
        var subject = Utilities.formatString(column.subject, contractNumber, columnHeader);
        var body = Utilities.formatString(column.body,columnHeader, contractNumber, data[i][20]);
        
        MailApp.sendEmail(recipient, subject, body);

        var lastRow = jaInformadoSheet.getLastRow();

        // Converter os valores de data[i] em strings com apóstrofo para evitar reformatação
        var stringData = data[i].map(function(value) {
            return "'" + String(value);
        });

        // Colar apenas os valores convertidos em strings
        jaInformadoSheet.getRange(lastRow + 1, 1, 1, stringData.length).setValues([stringData]);

      }
    }
  }
}