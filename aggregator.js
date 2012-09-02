matches=[];db.requests.distinct('name').forEach(function(e) 
	{if (db.titles.find({name:{ $regex: new RegExp("^" + e.toLowerCase(), "i")}}).count() > 0) 
	{matches.push(e)}})
print(matches)

//print out list of matches by typing:
//	>>matches
//in the mongo shell