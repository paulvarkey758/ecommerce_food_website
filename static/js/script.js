function categoryButton(x){
    var cat_list= document.getElementsByClassName("category-btn")
    for(var i=0;i<cat_list.length;i++)
    {
        cat_list[i].style.backgroundColor="white"
        cat_list[i].style.color="rgb(65, 121, 243)"
    }
    x.style.backgroundColor="rgb(65, 121, 243)"
    x.style.color="white"
    
}
function backButton(){
    window.history.back();
}