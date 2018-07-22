var a=document.getElementById("add");
var del=document.getElementById("delete");
var submit=document.getElementById("submit");

var arr=[];
var i=1;
  var j=0;
submit.addEventListener("click",function(){
  var orderno=document.getElementsByClassName("ordered").value;
  var obj={"orderno":orderno,
           "billdetail":arr};
           //when sending data to a web server, the data has to be a string
  jsonob=JSON.stringify(obj);
  //create a json file which is automatically downloaded on click of submit button
   var el = document.createElement('a');
   el.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(jsonob));
   el.setAttribute('download', 'backup.JSON');
   el.click();
  console.log(jsonob);
})

del.addEventListener("click",function(){

})
a.addEventListener("click",function(){

  var row = document.createElement('tr');
        var col1 = document.createElement('td');
        var col2 = document.createElement('td');
          var col3 = document.createElement('td');
            var col4 = document.createElement('td');
            row.setAttribute("class","row");
            col1.setAttribute("class","col-sm-3");
            col2.setAttribute("class","col-sm-3");
            col3.setAttribute("class","col-sm-3");
            col4.setAttribute("class","col-sm-3");
            //  var col5 = document.createElement('td');
          var input1=document.createElement('input');
          var input2=document.createElement('input');
          var input3=document.createElement('input');
          var input4=document.createElement('input');
          //  var input5=document.createElement('input');
          input1.setAttribute("class","class"+i);
          input2.setAttribute("class","class"+i);
          input3.setAttribute("class","class"+i);
          input4.setAttribute("class","class"+i);
          //input5.setAttribute("class","class"+i);
          col1.appendChild(input1);
            col2.appendChild(input2);
            col3.appendChild(input3);
            col4.appendChild(input4);
            //col5.appendChild(input5);
        row.appendChild(col1);
        row.appendChild(col2);
        row.appendChild(col3);
        row.appendChild(col4);
        //row.appendChild(col5);
        var tab = document.getElementById("tables");
        tab.appendChild(row);
        i++;

    var ob={
     "cdn":document.getElementsByClassName("class"+j)[0].value,
     "name":document.getElementsByClassName("class"+j)[1].value,
      "unitCost":document.getElementsByClassName("class"+j)[2].value,
     "qty":document.getElementsByClassName("class"+j)[3].value,
     "amount":""

   }

   //var orderno=document.getElementsByClassName("order").value;
  // arr.push(orderno)
    arr.push(ob);
console.log(arr);

j++;
})
