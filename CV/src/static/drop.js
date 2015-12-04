function fillPhones(){

    phones.options.length = 0;

    var e = document.getElementById("phones");
    var brand = document.getElementById("brand").selectedIndex

    switch (brand) {

        case 1:
        var arr = new Array("Select...","Bar Staff F/T,"Cabin Crew
        F/T,"Warehouse Assistant F/T");
        fillList(arr, e);
        break;

        case 2:
        var arr = new Array("Select...","Bar Staff P/T,"Cabin Crew
        P/T",Warehouse Assitant P/T");
        fillList(arr, e);
        break;

        }
      }

        function fillList(arr ,e){
          e.options.length = 0;
          for (var i = 0; i < arr.length; i++){
              option = new Option(arr[i] , arr[i]);
              e.options[i] = option;

      }
        }


