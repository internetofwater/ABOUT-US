
var data = [];
var siteNumber = '02043433'
const { Client } = require('pg')
const client = new Client({
  host: 'rapid-1304.vm.duke.edu',
  port: 5432,
  database: 'postgres',
  user: 'group3_read',
  password: 'water3all4me',
})

initialFunction( function(result) {
	var dataSet = result;

	for (var i = 0; i < dataSet.length; i++) {
  		data.push(Object.values(dataSet[i]));
	}
	//var myJSON = JSON.stringify(dataSet);
	console.log("result is: ", data);
})

function initialFunction(callback) {
	client.connect()
	client
	  .query("SELECT ts, signal FROM nwis.daily WHERE nwis_site_no = '02043433'")
	  .then(result => callback(result.rows)) //{data = result.rows; console.log(data);})//console.log(result.rows[0]['signal']))
	  .catch(e => console.error(e.stack))
	  .then(() => client.end())
}