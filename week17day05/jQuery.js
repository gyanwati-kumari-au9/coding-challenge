$.ajax({
    url:'https://raw.githubusercontent.com/nshntarora/Indian-Cities-JSON/master/cities.json',
    type: 'get',
    success: function(res){
      res=JSON.parse(res);
        console.log("Finised data retrieval")
        for(var i=0; i < res.length; i++){
          console.log(res[i]);
          var li = '<li>' +res[i].name+'</li>'
          if (res[i].state == 'Gujarat'){
            $('#github').append(li);
          }
        }
    }
});