
// 
    function copy(copyID){
        var $inp=$("<input>");
        $("body").append($inp);
        $inp.val($(""+copyID).text()).select();
        document.execCommand("copy");
        $inp.remove();
        $(".alert").fadeIn(500,
        function(){
            $(".alert").fadeOut();
        });
    }
    $(document).ready(function() {
        $("#copyButton1").click(
            function(){
                copy('#text1');
        });
    });





    function openNav() {
        document.getElementById("myNav").style.width = "100%";
    }
    function closeNav() {
        document.getElementById("myNav").style.width = "0%";
    }


for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}

function myFunctionn() {
        var element = document.getElementById("un");
        element.classList.remove("h");
      }

