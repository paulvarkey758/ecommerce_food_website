function selection(n)
  {
      var list=['all','sw','ff','mls','sn','cu'];
      for(var i=0;i<6;i++)
      {
	  if(n==list[i])
	  {
	      document.getElementById(n).style="background-color:#ffde00;";
	  }
	  else
	  {
	      document.getElementById(list[i]).style="background-color:#ffb700;";
	  }   
      }  
  }
